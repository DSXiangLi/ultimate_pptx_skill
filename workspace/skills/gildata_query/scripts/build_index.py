#!/usr/bin/env python3
"""
索引构建脚本 - 将表结构元数据导入ES并生成embedding向量
用法: python build_index.py [--config config.yaml]
"""

import os
import sys
import json
import glob
import re
import argparse
from typing import List, Dict, Any
from pathlib import Path

import requests
import yaml

# 添加父目录到路径以便导入配置
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
        """查找配置文件"""
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
        """加载配置"""
        if self.config_path and Path(self.config_path).exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = yaml.safe_load(f)
        else:
            self._config = self._default_config()

    def _default_config(self) -> dict:
        """默认配置"""
        return {
            "elasticsearch": {
                "host": "http://localhost:9200",
                "index": "db_meta"
            },
            "embedding": {
                "url": "http://algoplatform.thfund.work/assistant/bge-embedding/get_embedding",
                "max_length": 512,
                "batch_size": 32
            },
            "index": {
                "json_dir": "output/",
                "batch_size": 100
            }
        }

    def _parse_env_value(self, value):
        """解析环境变量占位符 ${VAR} 或 ${VAR:-default}"""
        if not isinstance(value, str):
            return value

        # 匹配 ${VAR} 或 ${VAR:-default}
        pattern = r'\$\{([^}:]+)(?::-([^}]*))?\}'

        def replace_env(match):
            var_name = match.group(1)
            default_val = match.group(2) if match.group(2) is not None else ""
            return os.environ.get(var_name, default_val)

        return re.sub(pattern, replace_env, value)

    def get(self, *keys, default=None, env_var: str = None):
        """
        获取配置值
        优先级: 环境变量 > 配置文件 > 默认值

        Args:
            *keys: 配置键路径
            default: 默认值
            env_var: 环境变量名，如果指定则优先从环境变量读取
        """
        # 1. 优先从环境变量读取
        if env_var and env_var in os.environ:
            return os.environ[env_var]

        # 2. 从配置文件读取
        value = self._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default

        # 3. 解析环境变量占位符
        value = self._parse_env_value(value)

        return value if value is not None else default


class EmbeddingClient:
    """Embedding接口客户端"""
    def __init__(self, config: Config):
        self.url = config.get("embedding", "url")
        self.max_length = config.get("embedding", "max_length", default=512)
        self.batch_size = config.get("embedding", "batch_size", default=32)
        self._cache = {}  # 简单缓存避免重复计算
        self._request_count = 0

    def get_embedding(self, text: str, max_retries: int = 3) -> List[float]:
        """获取单个文本的embedding，带重试机制"""
        if text in self._cache:
            return self._cache[text]

        # 截断过长文本
        if len(text) > self.max_length * 2:
            text = text[:self.max_length * 2]

        headers = {"Content-Type": "application/json"}
        data = {
            "return_sparse": False,
            "return_colbert_vecs": False,
            "return_dense": True,
            "max_length": self.max_length,
            "batch_size": 1,
            "sentences": [text]
        }

        for attempt in range(max_retries):
            try:
                resp = requests.post(self.url, json=data, headers=headers, timeout=60)
                resp.raise_for_status()
                embedding = resp.json()['dense_vecs'][0]
                self._cache[text] = embedding
                self._request_count += 1
                return embedding
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    print(f"  Embedding超时，重试 {attempt + 2}/{max_retries}")
                    time.sleep(2)
                else:
                    print(f"  Embedding超时，已达最大重试次数")
                    return [0.0] * 1024
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"  Embedding失败: {e}，重试 {attempt + 2}/{max_retries}")
                    time.sleep(1)
                else:
                    print(f"  Embedding失败: {e}")
                    return [0.0] * 1024

        return [0.0] * 1024

    def get_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """批量获取embedding"""
        results = []
        for text in texts:
            results.append(self.get_embedding(text))
        return results


class TableRelationExtractor:
    """从remark中提取表关联关系"""
    # 常见表名模式
    TABLE_PATTERNS = [
        r'[A-Z]+_[A-Za-z]+',  # 如 LC_StockArchives, QT_DailyQuote
        r'SecuMain',
        r'CT_SystemConst',
    ]

    def extract(self, remark: str) -> List[str]:
        """从remark中提取关联的表名"""
        if not remark:
            return []

        relations = []

        # 模式1: "与XXX表关联"、"与(XXX)表"
        patterns = [
            r'与[（(]?([A-Z]+_[A-Za-z]+)[）)]?表',
            r'与[（(]?([A-Z]+[A-Za-z]*)[）)]?表',
            r'关联[表项]*[（(]?([A-Z]+_[A-Za-z]+)[）)]?',
            r'([A-Z]+_[A-Za-z]+)表中的',
            r'([A-Z]+_[A-Za-z]+)表',
        ]

        for pattern in patterns:
            matches = re.findall(pattern, remark)
            relations.extend(matches)

        # 去重并过滤无效值
        relations = list(set(relations))
        relations = [r for r in relations if len(r) > 3 and not r.startswith('注')]

        return relations


class IndexBuilder:
    """索引构建器"""
    def __init__(self, config: Config):
        self.config = config
        # ES配置 - 优先环境变量
        self.es_host = config.get("elasticsearch", "host", default="http://localhost:9200", env_var="ES_HOST")
        self.es_index = config.get("elasticsearch", "index", default="db_meta", env_var="ES_INDEX")
        self.es_username = config.get("elasticsearch", "username", default="", env_var="ES_USERNAME")
        self.es_password = config.get("elasticsearch", "password", default="", env_var="ES_PASSWORD")
        self.request_timeout = config.get("elasticsearch", "request_timeout", default=20)
        self.retry_on_timeout = config.get("elasticsearch", "retry_on_timeout", default=True)
        self.max_retries = config.get("elasticsearch", "max_retries", default=3)
        # 索引构建配置
        self.json_dir = config.get("index", "json_dir", default="output/")
        self.batch_size = config.get("index", "batch_size", default=100)

        self.embedding_client = EmbeddingClient(config)
        self.relation_extractor = TableRelationExtractor()
        self.es = None

    def connect_es(self):
        """连接ES"""
        if self.es_username and self.es_password:
            self.es = Elasticsearch(
                self.es_host,
                basic_auth=(self.es_username, self.es_password),
                request_timeout=self.request_timeout,
                retry_on_timeout=self.retry_on_timeout,
                max_retries=self.max_retries
            )
        else:
            self.es = Elasticsearch(self.es_host)
        # 测试连接
        try:
            self.es.info()
            print(f"成功连接ES: {self.es_host}")
        except Exception as e:
            raise ConnectionError(f"无法连接ES: {self.es_host}, 错误: {e}")

    def create_index(self):
        """创建索引（如果不存在）"""
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
                        "index_options": {
                            "type": "hnsw",
                            "m": 48,
                            "ef_construction": 500
                        }
                    }
                }
            }
        }

        self.es.indices.create(index=self.es_index, body=mapping)
        print(f"创建索引: {self.es_index}")

    def build_table_doc(self, data: dict) -> dict:
        """构建表文档"""
        # 构建搜索文本
        search_text = f"{data['tableChiName']} {data['tableName']} {data.get('description', '')} {data.get('path', '')}"

        # 提取关联关系
        relations = []
        for col in data.get("columns", []):
            remark = col.get("remark") or ""
            relations.extend(self.relation_extractor.extract(remark))
        relations = list(set(relations))

        # 获取embedding
        embedding = self.embedding_client.get_embedding(search_text)

        return {
            "type": "table",
            "table_id": data["id"],
            "table_name": data["tableName"],
            "table_chi_name": data["tableChiName"],
            "path": data.get("path", ""),
            "description": data.get("description", ""),
            "relations": relations,
            "search_text": search_text,
            "vectors": embedding
        }

    def build_column_doc(self, data: dict, col: dict) -> dict:
        """构建字段文档"""
        remark = col.get("remark") or ""
        search_text = f"{col['columnChiName']} {col['columnName']} {remark}"

        # 获取embedding
        embedding = self.embedding_client.get_embedding(search_text)

        return {
            "type": "column",
            "table_id": data["id"],
            "table_name": data["tableName"],
            "column_name": col["columnName"],
            "column_chi_name": col["columnChiName"],
            "column_type": col.get("columnType", ""),
            "remark": remark,
            "search_text": search_text,
            "vectors": embedding
        }

    def load_json_files(self) -> List[dict]:
        """加载所有JSON文件"""
        json_files = glob.glob(os.path.join(self.json_dir, "*.json"))
        print(f"找到 {len(json_files)} 个JSON文件")

        all_data = []
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_data.append(data)
            except Exception as e:
                print(f"加载文件失败 {json_file}: {e}")

        return all_data

    def build(self):
        """构建索引"""
        import time
        print("=" * 50)
        print("开始构建索引")
        print("=" * 50)

        # 连接ES
        self.connect_es()

        # 创建索引
        self.create_index()

        # 加载数据
        all_data = self.load_json_files()
        total_tables = len(all_data)
        print(f"共 {total_tables} 张表需要处理")

        # 获取已存在的文档
        existing_count = self.es.count(index=self.es_index)['count']
        print(f"索引中已有 {existing_count} 条文档")

        # 构建文档
        actions = []
        processed = 0
        skipped = 0
        start_time = time.time()

        for data in all_data:
            processed += 1
            table_name = data.get('tableName', 'unknown')

            # 显示进度
            if processed % 10 == 0:
                elapsed = time.time() - start_time
                speed = processed / elapsed if elapsed > 0 else 0
                eta = (total_tables - processed) / speed if speed > 0 else 0
                print(f"进度: {processed}/{total_tables} ({processed*100//total_tables}%) | 速度: {speed:.1f}张/秒 | 预计剩余: {eta:.0f}秒 | 当前: {table_name}")

            try:
                # 检查表文档是否已存在
                table_doc_id = f"table_{data['id']}"
                if self.es.exists(index=self.es_index, id=table_doc_id):
                    skipped += 1
                    continue

                # 表文档
                table_doc = self.build_table_doc(data)
                actions.append({
                    "_index": self.es_index,
                    "_id": table_doc_id,
                    "_source": table_doc
                })

                # 字段文档
                for col in data.get("columns", []):
                    col_doc = self.build_column_doc(data, col)
                    actions.append({
                        "_index": self.es_index,
                        "_id": f"column_{data['id']}_{col['columnOrderId']}",
                        "_source": col_doc
                    })

                # 批量写入
                if len(actions) >= self.batch_size:
                    helpers.bulk(self.es, actions)
                    actions = []

            except Exception as e:
                print(f"处理表 {table_name} 失败: {e}")

        # 写入剩余数据
        if actions:
            helpers.bulk(self.es, actions)

        # 统计
        count = self.es.count(index=self.es_index)
        print("=" * 50)
        print(f"索引构建完成!")
        print(f"共写入 {count['count']} 条记录")
        print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="构建数据库元数据索引")
    parser.add_argument("--config", "-c", help="配置文件路径")
    args = parser.parse_args()

    config = Config(args.config)
    builder = IndexBuilder(config)
    builder.build()


if __name__ == "__main__":
    main()
