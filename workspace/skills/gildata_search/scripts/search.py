#!/usr/bin/env python3
"""
表检索脚本 - 完整保留原有功能，新增数据可用性支持
用法: 
  python search.py "用户问题" [--available] [--top-k 20]
  python search.py --table "表名"  # 查询表详情
"""


import os
import sys

# 在导入其他库之前，先设置环境变量并预加载 conda 库
# 解决库版本兼容性问题
conda_lib = "/opt/conda/lib"
if os.path.exists(conda_lib):
    # 设置环境变量
    os.environ["LD_LIBRARY_PATH"] = conda_lib + ":" + os.environ.get("LD_LIBRARY_PATH", "")
    # 使用 ctypes 预加载关键共享库
    try:
        import ctypes
        # 预加载 libstdc++
        ctypes.CDLL(os.path.join(conda_lib, "libstdc++.so.6"), mode=ctypes.RTLD_GLOBAL)
    except Exception:
        pass  # 如果失败，继续执行

import os
import sys
import json
import re
import time
import argparse
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Optional, Tuple

import requests
import yaml
from elasticsearch import Elasticsearch

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
    """配置管理 - 支持从任意目录执行"""
    def __init__(self, config_path: str = None):
        self.config_path = config_path or self._find_config()
        self._load_config()

    def _find_config(self) -> str:
        """按优先级查找配置文件"""
        # 获取脚本所在目录的绝对路径
        script_dir = Path(__file__).parent.absolute()
        project_root = script_dir.parent
        
        possible_paths = [
            # 1. 命令行指定的路径
            Path(self.config_path) if hasattr(self, 'config_path') and self.config_path else None,
            # 2. 脚本所在项目的 config 目录
            project_root / "config" / "config.yaml",
            # 3. 当前工作目录
            Path.cwd() / "config" / "config.yaml",
            Path.cwd() / "config.yaml",
            # 4. 上级目录（从 scripts 目录执行时）
            Path.cwd().parent / "config" / "config.yaml",
            # 5. 项目根目录（根据特征文件判断）
            self._find_project_root() / "config" / "config.yaml",
        ]
        
        for p in possible_paths:
            if p and p.exists():
                print(f"[Config] 加载配置: {p}")
                return str(p)
        
        print("[Config] 警告: 未找到配置文件，使用默认配置")
        return None

    def _find_project_root(self) -> Path:
        """通过查找特征文件定位项目根目录"""
        current = Path.cwd()
        # 向上查找包含 config 目录或特定文件的目录
        for _ in range(5):  # 最多向上5层
            if (current / "config").exists() or (current / "gildata_search").exists():
                return current
            if current.parent == current:  # 到达根目录
                break
            current = current.parent
        return Path.cwd()

    def _load_config(self):
        if self.config_path and Path(self.config_path).exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self._config = yaml.safe_load(f)
            except Exception as e:
                print(f"[Config] 加载配置文件失败: {e}")
                self._config = self._default_config()
        else:
            self._config = self._default_config()

    def _default_config(self) -> dict:
        return {
            "elasticsearch": {
                "host": os.environ.get("GIL_ES_HOST"),
                "index": os.environ.get("GIL_ES_INDEX", "gil_index_v2_fast"),
                "username": os.environ.get("GIL_ES_USERNAME", ""),
                "password": os.environ.get("GIL_ES_PASSWORD", "")
            },
            "embedding": {"url": os.environ.get("GIL_EMBEDDING_URL", ""), "max_length": 8192},
            "search": {"default_top_k": 20, "max_tables": 8, "max_columns_per_table": 8}
        }

    def get(self, *keys, default=None, env_var: str = None):
        # 优先从环境变量获取
        if env_var and env_var in os.environ:
            return os.environ[env_var]
        
        # 从配置文件获取
        value = self._config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return parse_env(value) if isinstance(value, str) else value


class EmbeddingClient:
    """Embedding接口客户端"""
    def __init__(self, config: Config):
        self.url = config.get("embedding", "url")
        self.max_length = config.get("embedding", "max_length", default=512)
        self.timeout = config.get("embedding", "timeout", default=30)
        self.max_retries = config.get("embedding", "max_retries", default=2)

    def _call_embedding(self, url: str, text: str) -> List[float]:
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
        resp = requests.post(url, json=data, headers=headers, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()['dense_vecs'][0]

    def get_embedding(self, text: str) -> List[float]:
        """获取embedding"""
        if not self.url:
            return None

        # 尝试主接口
        for attempt in range(self.max_retries):
            try:
                result = self._call_embedding(self.url, text)
                return result
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(0.5)
                    continue

        return None


# ============ 完整的数据域识别配置 ============
DATA_DOMAINS = {
    "指数": {
        "keywords": ["指数", "沪深300", "上证", "深证", "中证", "科创", "创业板", "双创", "50", "500", "1000",
                     "CSI 300", "STAR50", "index", "纳指", "道指", "恒生"],
        "path_patterns": ["指数数据库", "指数"],
        "priority_tables": ["QT_IndexQuote", "QT_CSIIndexQuote", "Index_RiskAnalysis", "Index_ReturnAnalysis",
                           "SecuMain", "Index_E"],
        "search_hints": ["指数行情", "指数收益", "指数风险", "指数波动率"]
    },
    "基金": {
        "keywords": [
            "基金", "ETF", "LOF", "QDII", "公募", "私募", "货币基金", "债券基金", "股票基金",
            "混合基金", "指数基金", "FOF", "净值", "申购", "赎回",
            "基金公司", "基金管理公司", "管理人", "基金管理人", "投资顾问",
            "旗下基金", "管理规模", "规模排名", "基金数量", "托管人",
            "REITs", "商品基金", "理财基金", "养老基金",
            "份额", "资产净值", "复权净值", "累计净值",
        ],
        "path_patterns": ["基金", "公募基金"],
        "priority_tables": ["MF_", "SecuMain"],
        "search_hints": [
            "基金净值", "基金业绩", "基金持仓", "基金收益",
            "基金管理人规模", "基金公司排名", "管理人规模排名",
            "基金规模统计", "旗下基金数量", "基金份额变动",
        ]
    },
    "股票": {
        "keywords": ["股票", "A股", "港股", "美股", "上市", "股价", "收盘价", "成交量", "茅台", "平安",
                     "行情", "日线", "K线"],
        "path_patterns": ["上市公司", "股票", "国内上市公司"],
        "priority_tables": ["QT_DailyQuote", "SecuMain", "LC_", "QT_"],
        "search_hints": ["股票行情", "日行情", "收盘价", "成交量"]
    },
    "债券": {
        "keywords": ["债券", "国债", "企业债", "公司债", "可转债", "利率债", "信用债", "久期", "收益率曲线"],
        "path_patterns": ["债券"],
        "priority_tables": ["Bond_", "SecuMain"],
        "search_hints": ["债券基本信息", "债券行情", "债券收益率"]
    },
    "期货": {
        "keywords": ["期货", "商品", "股指期货", "国债期货", "主力合约", "持仓量", "保证金"],
        "path_patterns": ["期货"],
        "priority_tables": ["Fut_", "QT_"],
        "search_hints": ["期货行情", "期货合约"]
    }
}

# 通用指标关键词 -> 搜索建议
INDICATOR_MAPPING = {
    # 风险收益指标
    "夏普比率": ["夏普比率", "收益指标", "风险指标", "波动率", "SharpRatio"],
    "波动率": ["波动率", "标准差", "风险指标", "RiskAnalysis"],
    "收益率": ["收益率", "年化收益", "Return", "Performance"],
    "回撤": ["最大回撤", "回撤", "Drawdown"],
    # 估值指标
    "市盈率": ["市盈率", "PE", "估值指标", "Valuation"],
    "市净率": ["市净率", "PB", "估值指标", "Valuation"],
    "估值": ["估值", "PE", "PB", "PS", "估值指标", "Valuation", "DIndicesForValuation"],
    # 规模/排名相关
    "规模": ["规模", "管理规模", "资产规模", "净值规模", "Scale", "NV", "NVII"],
    "排名": ["排名", "排行", "Rank", "排序", "名次"],
    "基金数量": ["基金数量", "旗下基金", "基金数", "FundN", "TotalFundN"],
    "份额": ["份额", "基金份额", "TotalShares", "份额变动"],
    # 财务指标
    "股息率": ["股息率", "分红率", "DividendRatio", "DYRatio"],
    "ROE": ["ROE", "净资产收益率", "股东权益回报率"],
    "市值": ["市值", "总市值", "流通市值", "TotalMV"],
}

# 业务场景 -> 最优表映射
SCENARIO_MAPPING = {
    # 基金公司/管理人相关
    "基金公司规模排名": ["MF_AdvisorScaleRank", "MF_InvestAdvisorOutline"],
    "基金公司管理规模": ["MF_AdvisorScaleRank", "MF_ScaleAnalysis"],
    "基金管理人排名": ["MF_AdvisorScaleRank", "MF_InvestAdvisorOutline"],
    "基金管理人规模": ["MF_AdvisorScaleRank", "MF_ScaleAnalysis"],
    "旗下基金数量": ["MF_AdvisorScaleRank", "MF_FundArchives"],
    "基金公司排名": ["MF_AdvisorScaleRank", "MF_InvestAdvisorOutline"],

    # 基金产品相关
    "基金净值": ["MF_NetValue", "MF_FundArchives"],
    "基金业绩": ["MF_FundPerformance", "MF_KeyIndex"],
    "基金持仓": ["MF_PortfolioStock", "MF_PortfolioBond"],
    "基金规模": ["MF_ScaleAnalysis", "MF_FundArchives"],
    "基金份额": ["MF_ScaleAnalysis", "MF_FundArchives"],
    "基金收益": ["MF_FundPerformance", "MF_NetValue"],

    # 指数相关
    "指数行情": ["QT_IndexQuote", "QT_CSIIndexQuote"],
    "指数估值": ["QT_CSIIndexQuote", "Index_E"],
    "指数PE": ["QT_CSIIndexQuote"],
    "指数成分股": ["LC_IndexComponentsWeight", "LC_IndexComponents"],
    "指数权重": ["LC_IndexComponentsWeight"],
    "指数风险": ["Index_RiskAnalysis"],
    "指数收益": ["Index_ReturnAnalysis"],
    "指数波动率": ["Index_RiskAnalysis"],

    # 股票相关
    "股票行情": ["QT_StockPerformance", "LC_DIndicesForValuation"],
    "股票估值": ["LC_DIndicesForValuation"],
    "股票PE": ["LC_DIndicesForValuation"],
    "股票筛选": ["LC_DIndicesForValuation", "LC_MainIndexNew", "SecuMain"],
    "财务指标": ["LC_MainIndexNew", "LC_FinancialIndicator"],
    "ROE": ["LC_MainIndexNew"],
    "股息率": ["LC_DIndicesForValuation"],
}


class DomainRecognizer:
    """数据域识别器"""

    @staticmethod
    def recognize(question: str) -> List[Tuple[str, float]]:
        """识别问题所属的数据域，返回 (域名, 置信度) 列表"""
        scores = {}
        question_lower = question.lower()

        for domain, config in DATA_DOMAINS.items():
            score = 0.0
            matched_keywords = []

            for keyword in config["keywords"]:
                if keyword.lower() in question_lower:
                    matched_keywords.append(keyword)
                    score += len(keyword) * 0.1

            if matched_keywords:
                scores[domain] = score

        if scores:
            max_score = max(scores.values())
            results = [(k, v/max_score) for k, v in scores.items()]
            return sorted(results, key=lambda x: x[1], reverse=True)
        return []

    @staticmethod
    def get_search_terms(question: str, domain: str = None) -> List[str]:
        """根据问题和数据域生成多个搜索词"""
        terms = [question]

        # 添加指标相关搜索词
        for indicator, hints in INDICATOR_MAPPING.items():
            if indicator in question:
                terms.extend(hints)

        # 添加数据域相关搜索词
        if domain and domain in DATA_DOMAINS:
            terms.extend(DATA_DOMAINS[domain].get("search_hints", []))

        return list(set(terms))


class TableSearcher:
    """表检索器 - 完整功能版"""

    def __init__(self, config: Config):
        self.config = config
        self.es_host = config.get("elasticsearch", "host")
        self.es_index = config.get("elasticsearch", "index", default="gil_index_v2")
        self.es_username = config.get("elasticsearch", "username", default="")
        self.es_password = config.get("elasticsearch", "password", default="")
        self.es = None
        self.embedding_client = EmbeddingClient(config)
        self.default_top_k = config.get("search", "default_top_k", default=20)
        self.max_tables = config.get("search", "max_tables", default=8)
        self.max_columns = config.get("search", "max_columns_per_table", default=8)

    def connect(self):
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
        try:
            self.es.info()
        except Exception as e:
            raise ConnectionError(f"无法连接ES: {self.es_host}, 错误: {e}")

    def _match_scenario(self, question: str) -> List[str]:
        """匹配业务场景，返回推荐表名列表"""
        matched_tables = []
        question_lower = question.lower()

        for scenario, tables in SCENARIO_MAPPING.items():
            if scenario in question:
                matched_tables.extend(tables)
                continue
            scenario_words = scenario.split()
            if len(scenario_words) >= 2 and all(w in question for w in scenario_words):
                matched_tables.extend(tables)

        return list(dict.fromkeys(matched_tables))

    def search_with_domain_filter(self, question: str, domain: str = None, 
                                   top_k: int = None, only_available: bool = False) -> List[dict]:
        """带数据域过滤的搜索"""
        if top_k is None:
            top_k = self.default_top_k

        # 获取查询的embedding向量
        query_vec = self.embedding_client.get_embedding(question)

        # 构建查询
        must_clauses = []
        should_clauses = []

        # 如果识别出数据域，添加 path 过滤
        if domain and domain in DATA_DOMAINS:
            path_patterns = DATA_DOMAINS[domain].get("path_patterns", [])
            if path_patterns:
                path_should = [{"match": {"path": pattern}} for pattern in path_patterns]
                should_clauses.append({
                    "bool": {"should": path_should, "boost": 2.0}
                })

        # 关键词检索
        should_clauses.extend([
            {"match_phrase": {"table_chi_name": {"query": question, "boost": 3.0}}},
            {"match_phrase": {"column_chi_name": {"query": question, "boost": 2.0}}},
            {"multi_match": {
                "type": "most_fields",
                "query": question,
                "fields": ["table_chi_name^3", "column_chi_name^2", "description^1.5", "remark^1.5", "search_text"],
                "boost": 1.5
            }},
            {"match": {"table_name": {"query": question, "boost": 2.0}}},
        ])

        # 向量检索（原有功能，仅当embedding可用时启用）
        if query_vec:
            should_clauses.append({
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'vectors') + 1.0",
                        "params": {"query_vector": query_vec}
                    },
                    "boost": 1.0
                }
            })

        # 过滤条件
        filter_clauses = []
        if only_available:
            filter_clauses.append({"term": {"data_status.available": True}})

        query = {
            "_source": ["type", "table_id", "table_name", "table_chi_name", "path",
                       "description", "column_name", "column_chi_name", 
                       "column_type", "remark", "search_text", "data_status"],
            "query": {
                "bool": {
                    "must": must_clauses if must_clauses else [{"match_all": {}}],
                    "should": should_clauses,
                    "filter": filter_clauses,
                    "minimum_should_match": 1
                }
            },
            "size": top_k
        }

        try:
            result = self.es.search(index=self.es_index, body=query)
            return result["hits"]["hits"]
        except Exception as e:
            print(f"检索失败: {e}")
            return []

    def multi_term_search(self, question: str, domain: str = None, 
                          only_available: bool = False) -> List[dict]:
        """多搜索词组合搜索"""
        all_hits = {}
        search_terms = DomainRecognizer.get_search_terms(question, domain)

        for term in search_terms[:5]:
            hits = self.search_with_domain_filter(term, domain, top_k=30, 
                                                   only_available=only_available)
            for hit in hits:
                doc_id = hit["_id"]
                if doc_id not in all_hits or hit["_score"] > all_hits[doc_id]["_score"]:
                    all_hits[doc_id] = hit

        return sorted(all_hits.values(), key=lambda x: x["_score"], reverse=True)

    def group_results(self, hits: List[dict]) -> List[dict]:
        """按table_id聚合结果"""
        tables = defaultdict(lambda: {"table": None, "columns": [], "table_score": 0})

        for hit in hits:
            src = hit["_source"]
            score = hit["_score"]
            table_id = src.get("table_id")

            if table_id is None:
                continue

            if src.get("type") == "table":
                tables[table_id]["table"] = src
                tables[table_id]["table_score"] = score
            else:
                if tables[table_id]["table"] is None:
                    tables[table_id]["table"] = {
                        "type": "table",
                        "table_id": table_id,
                        "table_name": src.get("table_name", "unknown"),
                        "table_chi_name": src.get("table_chi_name") or src.get("table_name", ""),
                        "path": src.get("path", ""),
                        "description": "",
                        "data_status": src.get("data_status", {})
                    }
                tables[table_id]["columns"].append({"info": src, "score": score})
                if score > tables[table_id]["table_score"]:
                    tables[table_id]["table_score"] = score

        sorted_tables = sorted(tables.values(), key=lambda x: x["table_score"], reverse=True)

        for t in sorted_tables:
            t["columns"] = sorted(t["columns"], key=lambda x: x["score"], reverse=True)[:self.max_columns]

        return sorted_tables[:self.max_tables]

    def _fetch_table_by_name(self, table_name: str) -> Optional[dict]:
        """根据表名从ES获取表信息"""
        try:
            query = {
                "_source": ["type", "table_id", "table_name", "table_chi_name", "path",
                           "description", "data_status"],
                "query": {
                    "bool": {
                        "must": [
                            {"term": {"type": "table"}},
                            {"term": {"table_name": table_name}}
                        ]
                    }
                },
                "size": 1
            }
            result = self.es.search(index=self.es_index, body=query)
            hits = result.get("hits", {}).get("hits", [])
            if hits:
                return {
                    "table": hits[0]["_source"],
                    "columns": [],
                    "table_score": 100
                }
        except Exception as e:
            pass
        return None

    def _promote_scenario_tables(self, grouped: List[dict], scenario_tables: List[str]) -> List[dict]:
        """将场景匹配的表提升到结果前列，如果不在结果中则从ES查询补充"""
        in_result = {}
        others = []

        for item in grouped:
            table = item.get("table")
            if not table:
                others.append(item)
                continue
            table_name = table.get("table_name", "")
            if table_name in scenario_tables:
                in_result[table_name] = item
            else:
                others.append(item)

        promoted = []
        for table_name in scenario_tables:
            if table_name in in_result:
                promoted.append(in_result[table_name])
            else:
                table_info = self._fetch_table_by_name(table_name)
                if table_info:
                    promoted.append(table_info)

        promoted.extend(others)
        return promoted[:self.max_tables]

    def search_tables(self, question: str, only_available: bool = False) -> str:
        """主函数: 检索并返回结构化文本"""
        if not self.es:
            self.connect()

        # 1. 识别数据域
        domains = DomainRecognizer.recognize(question)
        primary_domain = domains[0][0] if domains else None

        if domains:
            print(f"[识别数据域] {domains}")

        # 2. 场景匹配
        scenario_tables = self._match_scenario(question)
        if scenario_tables:
            print(f"[场景匹配] 推荐表: {scenario_tables}")

        # 3. 多搜索词搜索
        hits = self.multi_term_search(question, primary_domain, only_available)

        # 4. 聚合结果
        grouped = self.group_results(hits)

        # 5. 将场景匹配的表提升到结果前列
        if scenario_tables:
            grouped = self._promote_scenario_tables(grouped, scenario_tables)

        return self.format_output(grouped, question, primary_domain, scenario_tables)

    def format_output(self, grouped: List[dict], question: str, 
                      domain: str = None, scenario_tables: List[str] = None) -> str:
        """生成结构化文本描述"""
        lines = []
        lines.append(f"# 用户问题")
        lines.append(f"{question}")

        if domain:
            lines.append(f"\n识别数据域: **{domain}**")

        if scenario_tables:
            lines.append(f"\n🎯 **场景匹配推荐表**: {', '.join(scenario_tables)}")

        lines.append(f"\n# 相关表信息")
        lines.append("")

        if not grouped:
            lines.append("未找到相关表，请尝试更换查询词。")
            return "\n".join(lines)

        for i, item in enumerate(grouped, 1):
            table = item.get("table")
            if not table:
                continue

            table_name = table.get("table_name", "unknown")
            table_chi_name = table.get("table_chi_name", "")
            
            # 数据可用性标记
            ds = table.get("data_status", {})
            status_icon = "✅" if ds.get("available") else "❌"

            lines.append(f"## {i}. {status_icon} {table_name}（{table_chi_name}）")
            lines.append(f"- 路径: {table.get('path', 'N/A')}")
            lines.append(f"- 描述: {table.get('description', 'N/A')[:200]}...")
            
            # 数据可用性详情
            if ds.get("available"):
                lines.append(f"- 数据状态: 可用（{ds.get('row_count', 0)} 行）")
            else:
                lines.append(f"- 数据状态: {ds.get('error', '不可用')}")

            columns = item.get("columns", [])
            if columns:
                lines.append("- 相关字段:")
                for col in columns[:self.max_columns]:
                    c = col.get("info", {})
                    col_name = c.get("column_name", "")
                    col_chi_name = c.get("column_chi_name", "")
                    remark = c.get("remark", "")

                    if remark and len(remark) > 60:
                        remark = remark[:60] + "..."

                    remark_str = f" # {remark}" if remark else ""
                    lines.append(f"  - {col_name}（{col_chi_name}）{remark_str}")

            lines.append("")

        # 添加查询建议
        lines.append("# 查询建议")
        if len(grouped) > 1:
            lines.append("- 涉及多张表时，请注意通过关联字段(如InnerCode, CompanyCode)进行JOIN")
            lines.append("- SecuMain通常是证券主表，可用于获取股票代码和名称")

        # 添加数据域特定建议
        if domain == "指数":
            lines.append("- 指数行情: QT_IndexQuote (交易所指数), QT_CSIIndexQuote (中证指数)")
            lines.append("- 指数风险指标: Index_RiskAnalysis (波动率、最大回撤等)")
            lines.append("- 指数收益指标: Index_ReturnAnalysis (夏普比率、信息比率等)")
        elif domain == "基金":
            lines.append("- 基金净值: MF_NetValue")
            lines.append("- 基金业绩: MF_FundPerformance")
            lines.append("- 基金持仓: MF_PortfolioStock")

        return "\n".join(lines)

    # ============ 新增：表详情查询功能 ============
    
    def get_table_detail(self, table_name: str) -> Optional[dict]:
        """
        通过表名获取完整详情（表+所有字段）
        支持：英文名、中文名
        """
        if not self.es:
            self.connect()

        # 1. 查询表文档（支持英文/中文名）
        table_query = {
            "query": {
                "bool": {
                    "must": [{"term": {"type": "table"}}],
                    "should": [
                        {"term": {"table_name": table_name}},
                        {"match": {"table_chi_name": table_name}}
                    ],
                    "minimum_should_match": 1
                }
            },
            "size": 1
        }
        
        table_result = self.es.search(index=self.es_index, body=table_query)
        if not table_result["hits"]["hits"]:
            return None
        
        table_doc = table_result["hits"]["hits"][0]["_source"]
        table_id = table_doc["table_id"]
        
        # 2. 查询所有字段文档
        col_query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"type": "column"}},
                        {"term": {"table_id": table_id}}
                    ]
                }
            },
            "size": 1000
        }
        
        col_result = self.es.search(index=self.es_index, body=col_query)
        columns = [hit["_source"] for hit in col_result["hits"]["hits"]]
        
        return {"table": table_doc, "columns": columns}

    def format_table_detail(self, detail: dict) -> str:
        """格式化表详情为文本"""
        if not detail:
            return "表不存在"
        
        table = detail["table"]
        columns = detail["columns"]
        
        lines = []
        lines.append(f"# {table['table_name']} ({table['table_chi_name']})")
        lines.append(f"路径: {table.get('path', 'N/A')}")
        lines.append(f"描述: {table.get('description', 'N/A')}")
        
        # 数据可用性
        ds = table.get("data_status", {})
        lines.append(f"\n数据可用性: {'✅ 可用' if ds.get('available') else '❌ 不可用'}")
        if ds.get("available"):
            lines.append(f"数据行数: {ds.get('row_count', 0)}")
        else:
            lines.append(f"错误信息: {ds.get('error', '未知')}")
        
        lines.append(f"\n# 字段列表 ({len(columns)} 个)")
        for i, col in enumerate(columns, 1):
            lines.append(f"\n## {i}. {col['column_name']}")
            lines.append(f"  中文名: {col['column_chi_name']}")
            lines.append(f"  类型: {col['column_type']}")
            if col.get("remark"):
                remark = col['remark']
                if len(remark) > 100:
                    remark = remark[:100] + "..."
                lines.append(f"  说明: {remark}")
        
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="表检索工具")
    parser.add_argument("question", nargs="?", help="用户的自然语言问题")
    parser.add_argument("--table", help="查询指定表的完整信息")
    parser.add_argument("--config", default="../config/config.yaml", help="配置文件路径")
    parser.add_argument("--top-k", "-k", type=int, help="返回结果数量")
    parser.add_argument("--available", action="store_true", help="只显示有数据的表")
    parser.add_argument("--json", "-j", action="store_true", help="以JSON格式输出")
    args = parser.parse_args()

    if not args.question and not args.table:
        parser.print_help()
        return

    config = Config(args.config)
    searcher = TableSearcher(config)

    if args.table:
        # 查询表详情
        detail = searcher.get_table_detail(args.table)
        if args.json:
            print(json.dumps(detail, ensure_ascii=False, indent=2))
        else:
            print(searcher.format_table_detail(detail))
    else:
        # 搜索 - 使用完整的 search_tables 方法来获得一致的体验
        output = searcher.search_tables(args.question, only_available=args.available)
        
        if args.json:
            # 解析输出为JSON格式（简化版）
            lines = output.split('\n')
            serializable = {
                "query": args.question,
                "tables": []
            }
            
            current_table = None
            for line in lines:
                line = line.strip()
                if line.startswith('## ') and '（' in line:
                    # 提取表名: ## 1. ✅ MF_NetValue（公募基金净值）
                    parts = line.replace('## ', '').split('（')[0]
                    for i in range(1, 10):
                        parts = parts.replace(f'{i}. ', '').replace('✅ ', '').replace('❌ ', '')
                    table_name = parts.strip()
                    current_table = {"name": table_name, "description": ""}
                    serializable["tables"].append(current_table)
                elif line.startswith('- 描述:') and current_table:
                    current_table["description"] = line.replace('- 描述:', '').strip()[:200]
            
            print(json.dumps(serializable, ensure_ascii=False, indent=2))
        else:
            print(output)


if __name__ == "__main__":
    main()
