#!/usr/bin/env python3
"""
多线程索引构建脚本 - 加速构建过程
用法: python build_index_multithread.py [--config config.yaml] [--workers 8]
"""

import os
import sys
import json
import glob
import re
import time
import argparse
import threading
from typing import List, Dict, Any
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue

import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))
try:
    from elasticsearch import Elasticsearch, helpers
except ImportError:
    print("请安装 elasticsearch: pip install elasticsearch")
    sys.exit(1)


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
            "elasticsearch": {"host": "http://localhost:9200", "index": "db_meta"},
            "embedding": {"url": "", "max_length": 512, "batch_size": 32},
            "index": {"json_dir": "output/", "batch_size": 100}
        }

    def _parse_env_value(self, value):
        if not isinstance(value, str):
            return value
        pattern = r'\$\{([^}:]+)(?::-([^}]*))?\}'
        def replace_env(match):
            return os.environ.get(match.group(1), match.group(2) or "")
        return re.sub(pattern, replace_env, value)

    def get(self, *keys, default=None, env_var: str = None):
        if env_var and env_var in os.environ:
            return os.environ[env_var]
        value = self._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        value = self._parse_env_value(value)
        return value if value is not None else default


class BatchEmbeddingClient:
    """批量Embedding客户端 - 支持并发请求和主备切换"""
    def __init__(self, config: Config, max_workers: int = 8):
        self.url = config.get("embedding", "url")
        self.fallback_url = config.get("embedding", "fallback_url")
        self.max_length = config.get("embedding", "max_length", default=512)
        self.timeout = config.get("embedding", "timeout", default=30)
        self.max_workers = max_workers
        self._lock = threading.Lock()
        self._cache = {}
        self._request_count = 0
        self._fail_count = 0
        self._primary_failed = False  # 标记主接口是否失败

    def _call_embedding(self, url: str, text: str) -> List[float]:
        """调用单个embedding接口"""
        headers = {"Content-Type": "application/json"}
        data = {
            "return_sparse": False,
            "return_colbert_vecs": False,
            "return_dense": True,
            "max_length": self.max_length,
            "batch_size": 1,
            "sentences": [text]
        }
        resp = requests.post(url, json=data, headers=headers, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()['dense_vecs'][0]

    def get_embedding(self, text: str, max_retries: int = 2) -> List[float]:
        """获取单个文本的embedding，支持主备切换"""
        with self._lock:
            if text in self._cache:
                return self._cache[text]

        if len(text) > self.max_length * 2:
            text = text[:self.max_length * 2]

        # 如果主接口之前失败过，直接用备用接口
        if self._primary_failed and self.fallback_url:
            try:
                embedding = self._call_embedding(self.fallback_url, text)
                with self._lock:
                    self._cache[text] = embedding
                    self._request_count += 1
                return embedding
            except Exception as e:
                with self._lock:
                    self._fail_count += 1
                return [0.0] * 1024

        # 尝试主接口
        for attempt in range(max_retries):
            try:
                embedding = self._call_embedding(self.url, text)
                with self._lock:
                    self._cache[text] = embedding
                    self._request_count += 1
                return embedding
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(0.5)
                    continue

                # 主接口失败，标记并尝试备用接口
                with self._lock:
                    self._primary_failed = True

                if self.fallback_url:
                    try:
                        embedding = self._call_embedding(self.fallback_url, text)
                        with self._lock:
                            self._cache[text] = embedding
                            self._request_count += 1
                        return embedding
                    except Exception as e2:
                        pass

                with self._lock:
                    self._fail_count += 1
                return [0.0] * 1024

        return [0.0] * 1024

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
    """从remark中提取表关联关系"""
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


class MultiThreadIndexBuilder:
    """多线程索引构建器"""
    def __init__(self, config: Config, workers: int = 8):
        self.config = config
        self.workers = workers

        # ES配置
        self.es_host = config.get("elasticsearch", "host", env_var="ES_HOST")
        self.es_index = config.get("elasticsearch", "index", env_var="ES_INDEX")
        self.es_username = config.get("elasticsearch", "username", env_var="ES_USERNAME")
        self.es_password = config.get("elasticsearch", "password", env_var="ES_PASSWORD")

        # 索引配置
        self.json_dir = config.get("index", "json_dir", default="output/")
        self.batch_size = config.get("index", "batch_size", default=500)

        self.embedding_client = BatchEmbeddingClient(config, max_workers=workers)
        self.relation_extractor = TableRelationExtractor()
        self.es = None

        # 进度统计
        self._lock = threading.Lock()
        self._processed = 0
        self._skipped = 0
        self._failed = 0

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
        print(f"成功连接ES: {self.es_host}")

    def create_index(self):
        """创建索引"""
        if self.es.indices.exists(index=self.es_index):
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
        print(f"创建索引: {self.es_index}")

    def process_table(self, data: dict) -> List[dict]:
        """处理单张表，返回所有文档"""
        try:
            actions = []
            table_id = data["id"]
            table_name = data.get('tableName', 'unknown')

            # 检查是否已存在
            if self.es.exists(index=self.es_index, id=f"table_{table_id}"):
                with self._lock:
                    self._skipped += 1
                return []
        except Exception as e:
            with self._lock:
                self._failed += 1
            return []

        try:
            # 构建表文档
            search_text = f"{data['tableChiName']} {data['tableName']} {data.get('description', '')} {data.get('path', '')}"
            relations = []
            for col in data.get("columns", []):
                relations.extend(self.relation_extractor.extract(col.get("remark") or ""))

            table_embedding = self.embedding_client.get_embedding(search_text)
            actions.append({
                "_index": self.es_index,
                "_id": f"table_{table_id}",
                "_source": {
                    "type": "table",
                    "table_id": table_id,
                    "table_name": data["tableName"],
                    "table_chi_name": data["tableChiName"],
                    "path": data.get("path", ""),
                    "description": data.get("description", ""),
                    "relations": list(set(relations)),
                    "search_text": search_text,
                    "vectors": table_embedding
                }
            })

            # 收集所有字段的文本，批量获取embedding
            columns = data.get("columns", [])
            col_texts = [f"{col['columnChiName']} {col['columnName']} {col.get('remark') or ''}" for col in columns]
            col_embeddings = self.embedding_client.get_embeddings_batch(col_texts)

            # 构建字段文档
            for col, embedding, search_text in zip(columns, col_embeddings, col_texts):
                actions.append({
                    "_index": self.es_index,
                    "_id": f"column_{table_id}_{col['columnOrderId']}",
                    "_source": {
                        "type": "column",
                        "table_id": table_id,
                        "table_name": data["tableName"],
                        "table_chi_name": data["tableChiName"],
                        "path": data.get("path", ""),
                        "column_name": col["columnName"],
                        "column_chi_name": col["columnChiName"],
                        "column_type": col.get("columnType", ""),
                        "remark": col.get("remark") or "",
                        "search_text": search_text,
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

    def load_json_files(self) -> List[dict]:
        """加载所有JSON文件"""
        json_files = glob.glob(os.path.join(self.json_dir, "*.json"))
        print(f"找到 {len(json_files)} 个JSON文件")

        all_data = []
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    all_data.append(json.load(f))
            except Exception as e:
                print(f"加载文件失败 {json_file}: {e}")
        return all_data

    def build(self):
        """构建索引"""
        print("=" * 50)
        print(f"开始构建索引 (多线程版本, workers={self.workers})")
        print("=" * 50)

        self.connect_es()
        self.create_index()

        all_data = self.load_json_files()
        total_tables = len(all_data)
        print(f"共 {total_tables} 张表需要处理")

        existing_count = self.es.count(index=self.es_index)['count']
        print(f"索引中已有 {existing_count} 条文档")

        start_time = time.time()
        all_actions = []

        # 使用线程池并行处理
        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {executor.submit(self.process_table, data): data for data in all_data}

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
                    eta = (total_tables - i) / speed if speed > 0 else 0
                    current_count = self.es.count(index=self.es_index)['count']
                    print(f"进度: {i}/{total_tables} ({i*100//total_tables}%) | ES文档: {current_count} | 速度: {speed:.1f}张/秒 | ETA: {eta/60:.1f}分钟")

        # 写入剩余数据
        if all_actions:
            helpers.bulk(self.es, all_actions)

        # 最终统计
        final_count = self.es.count(index=self.es_index)['count']
        elapsed = time.time() - start_time
        print("=" * 50)
        print(f"索引构建完成!")
        print(f"总文档数: {final_count}")
        print(f"处理表数: {self._processed}")
        print(f"跳过表数: {self._skipped}")
        print(f"失败表数: {self._failed}")
        print(f"Embedding请求: {self.embedding_client._request_count}")
        print(f"Embedding失败: {self.embedding_client._fail_count}")
        print(f"总耗时: {elapsed:.1f}秒")
        print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="多线程构建数据库元数据索引")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--workers", "-w", type=int, default=8, help="并发线程数")
    args = parser.parse_args()

    config = Config(args.config)
    builder = MultiThreadIndexBuilder(config, workers=args.workers)
    builder.build()


if __name__ == "__main__":
    main()
