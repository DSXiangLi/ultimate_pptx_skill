#!/usr/bin/env python3
"""
建索引脚本 - 完整保留原有功能，新增数据可用性支持
用法: python build_index.py [--availability availability_check.json] [--workers 8]
"""

import os
import sys
import json
import glob
import re
import time
import argparse
import threading
from typing import List, Dict, Any, Optional
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
import yaml
from elasticsearch import Elasticsearch, helpers

sys.path.insert(0, str(Path(__file__).parent.parent))


def parse_env(value: str) -> str:
    """解析 ${VAR:-default} 格式"""
    if not isinstance(value, str):
        return value
    pattern = r'\$\{([^}:]+):-([^}]*)\}'
    match = re.search(pattern, value)
    if match:
        return os.environ.get(match.group(1), match.group(2) or "")
    return value


class Config:
    """配置管理"""
    def __init__(self, config_path: str = None):
        self.config_path = config_path or self._find_config()
        self._load_config()

    def _find_config(self) -> str:
        possible_paths = [
            Path(__file__).parent.parent / "config" / "config.yaml",
            Path(__file__).parent / "config.yaml",
            Path.cwd() / "config.yaml",
        ]
        for p in possible_paths:
            if p.exists():
                return str(p)
        return None

    def _load_config(self):
        if self.config_path and Path(self.config_path).exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = yaml.safe_load(f)
        else:
            self._config = self._default_config()

    def _default_config(self) -> dict:
        return {
            "elasticsearch": {"host": os.environ.get("GIL_ES_HOST", ""), "index": os.environ.get("GIL_ES_INDEX", "")},
            "embedding": {"url": "", "max_length": 512, "batch_size": 32},
            "index": {"json_dir": "../../output", "batch_size": 100}
        }

    def get(self, *keys, default=None, env_var: str = None):
        if env_var and env_var in os.environ:
            return os.environ[env_var]
        value = self._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return parse_env(value) if isinstance(value, str) else value


class BatchEmbeddingClient:
    """批量Embedding客户端 - 支持并发请求"""
    def __init__(self, config: Config, max_workers: int = 8):
        self.url = config.get("embedding", "url")
        self.max_length = config.get("embedding", "max_length", default=512)
        self.timeout = config.get("embedding", "timeout", default=30)
        self.max_workers = max_workers
        self._lock = threading.Lock()
        self._cache = {}
        self._request_count = 0
        self._fail_count = 0

    def _call_embedding(self, url: str, text: str) -> Optional[List[float]]:
        """调用单个embedding接口"""
        headers = {"Content-Type": "application/json"}
        data = {
            "return_sparse": True,
            "return_colbert_vecs": True,
            "return_dense": True,
            "max_length": 8192,
            "batch_size": 1,
            "sentences": [text]
        }
        try:
            resp = requests.post(url, json=data, headers=headers, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            if 'dense_vecs' in result and len(result['dense_vecs']) > 0:
                return result['dense_vecs'][0]
        except Exception as e:
            pass
        return None

    def get_embedding(self, text: str, max_retries: int = 2) -> Optional[List[float]]:
        """获取单个文本的embedding"""
        with self._lock:
            if text in self._cache:
                return self._cache[text]

        if len(text) > self.max_length * 2:
            text = text[:self.max_length * 2]

        # 尝试主接口
        for attempt in range(max_retries):
            embedding = self._call_embedding(self.url, text)
            if embedding:
                with self._lock:
                    self._cache[text] = embedding
                    self._request_count += 1
                return embedding
            
            if attempt < max_retries - 1:
                time.sleep(0.3)

        # 标记失败
        with self._lock:
            self._fail_count += 1
        
        return None

    def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """并发获取多个文本的embedding"""
        results = [None] * len(texts)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_idx = {executor.submit(self.get_embedding, text): i for i, text in enumerate(texts)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                results[idx] = future.result()

        return results


class TableRelationExtractor:
    """从remark中提取表关联关系（与原有实现一致）"""
    def extract(self, remark: str) -> List[str]:
        if not remark:
            return []
        relations = []
        patterns = [
            r'与[（(]?([A-Z]+_[A-Za-z]+)[）)]?表',
            r'关联[表项]*[（(]?([A-Z]+_[A-Za-z]+)[）)]?',
            r'([A-Z]+_[A-Za-z]+)表',
        ]
        for pattern in patterns:
            relations.extend(re.findall(pattern, remark))
        return list(set(r for r in relations if len(r) > 3))


class IndexBuilder:
    """索引构建器 - 多线程版本，完整保留原有功能"""

    def __init__(self, config: Config, workers: int = 8):
        self.config = config
        self.workers = workers

        # ES配置
        self.es_host = config.get("elasticsearch", "host", env_var="ES_HOST")
        self.es_index = config.get("elasticsearch", "index", env_var="ES_INDEX")
        self.es_username = config.get("elasticsearch", "username", env_var="ES_USERNAME")
        self.es_password = config.get("elasticsearch", "password", env_var="ES_PASSWORD")

        # 索引配置
        self.batch_size = config.get("index", "batch_size", default=500)

        # 客户端
        self.embedding_client = BatchEmbeddingClient(config, max_workers=workers)
        self.relation_extractor = TableRelationExtractor()
        self.es = None

        # 可用性数据
        self.availability = {}

        # 进度统计
        self._lock = threading.Lock()
        self._processed = 0
        self._skipped = 0
        self._failed = 0

    def load_availability(self, availability_file: str):
        """加载表可用性数据"""
        if not availability_file or not Path(availability_file).exists():
            print(f"警告: 可用性文件不存在 {availability_file}")
            return

        with open(availability_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.availability = data.get("results", {})
        print(f"✓ 加载可用性数据: {len(self.availability)} 个表")

    def get_data_status(self, table_name: str) -> dict:
        """获取表的可用性状态"""
        info = self.availability.get(table_name, {})
        return {
            "available": info.get("accessible", False),
            "exists": info.get("exists", False),
            "row_count": info.get("row_count", 0),
            "error": info.get("error"),
            "checked_at": info.get("checked_at")
        }

    def connect_es(self):
        """连接ES"""
        if self.es_username and self.es_password:
            self.es = Elasticsearch(
                self.es_host,
                basic_auth=(self.es_username, self.es_password),
                request_timeout=30,
                retry_on_timeout=True,
                max_retries=3
            )
        else:
            self.es = Elasticsearch(self.es_host)
        self.es.info()
        print(f"✓ 连接ES: {self.es_host}")

    def create_index(self, force: bool = False):
        """创建索引"""
        if self.es.indices.exists(index=self.es_index):
            if force:
                print(f"删除已存在的索引: {self.es_index}")
                self.es.indices.delete(index=self.es_index)
            else:
                print(f"索引 {self.es_index} 已存在")
                return

        mapping = {
            "mappings": {
                "properties": {
                    "type": {"type": "keyword"},
                    "table_id": {"type": "integer"},
                    "table_name": {"type": "keyword"},
                    "table_chi_name": {"type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
                    "path": {"type": "text", "analyzer": "ik_max_word"},
                    "description": {"type": "text", "analyzer": "ik_max_word", "search_analyzer": "ik_smart"},
                    "relations": {"type": "keyword"},

                    # 数据可用性状态（新增）
                    "data_status": {
                        "properties": {
                            "available": {"type": "boolean"},
                            "exists": {"type": "boolean"},
                            "row_count": {"type": "long"},
                            "error": {"type": "keyword"},
                            "checked_at": {"type": "date"}
                        }
                    },

                    # 字段特有字段
                    "column_name": {"type": "keyword"},
                    "column_chi_name": {"type": "text", "analyzer": "ik_max_word"},
                    "column_type": {"type": "keyword"},
                    "remark": {"type": "text", "analyzer": "ik_max_word"},

                    "search_text": {"type": "text", "analyzer": "ik_max_word"},
                    "vectors": {
                        "type": "dense_vector",
                        "dims": 1024,
                        "index": True,
                        "similarity": "cosine",
                        "index_options": {"type": "hnsw", "m": 48, "ef_construction": 500}
                    }
                }
            }
        }
        self.es.indices.create(index=self.es_index, body=mapping)
        print(f"✓ 创建索引: {self.es_index}")

    def process_table(self, data: dict) -> List[dict]:
        """处理单张表，返回所有文档（表+字段）"""
        try:
            actions = []
            table_id = data.get("id")
            table_name = data.get("tableName")

            if not table_id or not table_name:
                return []

            # 检查是否已存在（增量）
            try:
                if self.es.exists(index=self.es_index, id=f"table_{table_id}"):
                    with self._lock:
                        self._skipped += 1
                    return []
            except Exception as e:
                pass

            # 获取可用性状态
            data_status = self.get_data_status(table_name)

            # 提取关联表
            relations = []
            for col in data.get("columns", []):
                relations.extend(self.relation_extractor.extract(col.get("remark") or ""))

            # 构建表搜索文本
            search_text = f"{data.get('tableChiName', '')} {table_name} {data.get('description', '')} {data.get('path', '')}"
            table_embedding = self.embedding_client.get_embedding(search_text)
            if table_embedding is None:
                table_embedding = [0.0] * 1024

            # 1. 表文档
            actions.append({
                "_index": self.es_index,
                "_id": f"table_{table_id}",
                "_source": {
                    "type": "table",
                    "table_id": table_id,
                    "table_name": table_name,
                    "table_chi_name": data.get("tableChiName", ""),
                    "path": data.get("path", ""),
                    "description": data.get("description", ""),
                    "relations": list(set(relations)),
                    "data_status": data_status,  # 新增
                    "search_text": search_text,
                    "vectors": table_embedding
                }
            })

            # 收集字段文本，批量获取embedding
            columns = data.get("columns", [])
            col_texts = [f"{col.get('columnChiName', '')} {col.get('columnName', '')} {col.get('remark') or ''}" for col in columns]
            col_embeddings = self.embedding_client.get_embeddings_batch(col_texts)

            # 2. 字段文档
            for col, emb, col_search_text in zip(columns, col_embeddings, col_texts):
                embedding = emb if emb is not None else [0.0] * 1024
                actions.append({
                    "_index": self.es_index,
                    "_id": f"column_{table_id}_{col.get('columnOrderId', 0)}",
                    "_source": {
                        "type": "column",
                        "table_id": table_id,
                        "table_name": table_name,
                        "table_chi_name": data.get("tableChiName", ""),
                        "path": data.get("path", ""),
                        "column_name": col.get("columnName"),
                        "column_chi_name": col.get("columnChiName"),
                        "column_type": col.get("columnType", ""),
                        "remark": col.get("remark") or "",
                        "data_status": data_status,  # 字段继承表状态
                        "search_text": col_search_text,
                        "vectors": embedding
                    }
                })

            with self._lock:
                self._processed += 1

        except Exception as e:
            with self._lock:
                self._failed += 1
            print(f"处理表 {table_name} 失败: {e}")

        return actions

    def build(self, json_dir: str, force: bool = False):
        """构建索引 - 多线程版本"""
        print("=" * 60)
        print(f"开始构建索引 (多线程版本, workers={self.workers})")
        print("=" * 60)

        self.connect_es()
        self.create_index(force=force)

        # 读取所有JSON
        json_files = sorted(glob.glob(os.path.join(json_dir, "*.json")))
        print(f"✓ 找到 {len(json_files)} 个JSON文件\n")

        # 检查现有文档数
        existing_count = self.es.count(index=self.es_index)['count']
        print(f"索引中已有 {existing_count} 条文档")

        start_time = time.time()
        all_actions = []

        # 使用线程池并行处理
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self.process_table, data): data for data in self._load_json_files(json_dir)}

            for i, future in enumerate(as_completed(futures), 1):
                actions = future.result()
                all_actions.extend(actions)

                # 批量写入ES
                if len(all_actions) >= self.batch_size:
                    try:
                        helpers.bulk(self.es, all_actions)
                        all_actions = []
                    except Exception as e:
                        print(f"批量写入失败: {e}")

                # 显示进度
                if i % 50 == 0:
                    elapsed = time.time() - start_time
                    speed = i / elapsed if elapsed > 0 else 0
                    current_count = self.es.count(index=self.es_index)['count']
                    print(f"进度: {i}/{len(json_files)} ({i*100//len(json_files)}%) | "
                          f"ES文档: {current_count} | 速度: {speed:.1f}张/秒")

        # 写入剩余数据
        if all_actions:
            helpers.bulk(self.es, all_actions)

        # 最终统计
        final_count = self.es.count(index=self.es_index)['count']
        elapsed = time.time() - start_time

        print("\n" + "=" * 60)
        print("索引构建完成!")
        print("=" * 60)
        print(f"总文档数: {final_count}")
        print(f"处理表数: {self._processed}")
        print(f"跳过表数: {self._skipped}")
        print(f"失败表数: {self._failed}")
        print(f"Embedding请求: {self.embedding_client._request_count}")
        print(f"Embedding失败: {self.embedding_client._fail_count}")
        print(f"总耗时: {elapsed:.1f}秒")
        print("=" * 60)

    def _load_json_files(self, json_dir: str) -> List[dict]:
        """加载所有JSON文件"""
        json_files = sorted(glob.glob(os.path.join(json_dir, "*.json")))
        all_data = []
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get("id") and data.get("tableName"):
                        all_data.append(data)
            except Exception as e:
                print(f"加载文件失败 {json_file}: {e}")
        return all_data


def main():
    parser = argparse.ArgumentParser(description="构建ES索引")
    parser.add_argument("--json-dir", default="../../output", help="JSON文件目录")
    parser.add_argument("--availability", default="../../availability_check.json", help="可用性检查结果")
    parser.add_argument("--config", default="../config/config.yaml", help="配置文件")
    parser.add_argument("--index", help="索引名(覆盖配置)")
    parser.add_argument("--workers", "-w", type=int, default=8, help="并发线程数")
    parser.add_argument("--force", action="store_true", help="强制重建索引")
    args = parser.parse_args()

    config = Config(args.config)
    if args.index:
        config._config["elasticsearch"]["index"] = args.index

    builder = IndexBuilder(config, workers=args.workers)
    builder.load_availability(args.availability)
    builder.build(args.json_dir, force=args.force)


if __name__ == "__main__":
    main()
