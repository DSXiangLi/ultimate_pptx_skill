#!/usr/bin/env python3
"""
表检索脚本 - 根据用户问题检索相关表和字段
用法: python search_tables.py "用户问题" [--config config.yaml] [--top-k 20]

优化版本:
1. 数据域识别 - 根据问题识别数据类型(指数/基金/股票/债券等)
2. Path过滤 - 优先在对应数据域的表中搜索
3. 多维度搜索 - 拆分问题为多个搜索词
"""

import os
import sys
import json
import re
import argparse
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
from collections import defaultdict

import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent.parent))
try:
    from elasticsearch import Elasticsearch
except ImportError:
    print("请安装 elasticsearch: pip install elasticsearch")
    sys.exit(1)


# ============ 数据域识别配置 ============
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
            # 基础
            "基金", "ETF", "LOF", "QDII", "公募", "私募", "货币基金", "债券基金", "股票基金",
            "混合基金", "指数基金", "FOF", "净值", "申购", "赎回",
            # 基金公司/管理人相关
            "基金公司", "基金管理公司", "管理人", "基金管理人", "投资顾问",
            "旗下基金", "管理规模", "规模排名", "基金数量", "托管人",
            # 基金类型
            "REITs", "商品基金", "理财基金", "养老基金",
            # 基金指标
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

# 业务场景 -> 最优表映射（核心优化：直接推荐最合适的表）
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
            "embedding": {"url": "", "max_length": 512},
            "search": {"default_top_k": 20, "max_tables": 8, "max_columns_per_table": 8}
        }

    def _parse_env_value(self, value):
        if not isinstance(value, str):
            return value
        pattern = r'\$\{([^}:]+)(?::-([^}]*))?\}'
        def replace_env(match):
            var_name = match.group(1)
            default_val = match.group(2) if match.group(2) is not None else ""
            return os.environ.get(var_name, default_val)
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


class EmbeddingClient:
    """Embedding接口客户端 - 支持主备切换"""
    def __init__(self, config: Config):
        self.url = config.get("embedding", "url")
        self.fallback_url = config.get("embedding", "fallback_url")
        self.max_length = config.get("embedding", "max_length", default=512)
        self.timeout = config.get("embedding", "timeout", default=30)
        self.max_retries = config.get("embedding", "max_retries", default=2)
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

    def get_embedding(self, text: str) -> List[float]:
        """获取embedding，支持主备切换"""
        if not self.url:
            return None

        # 如果主接口之前失败过，直接用备用接口
        if self._primary_failed and self.fallback_url:
            try:
                return self._call_embedding(self.fallback_url, text)
            except Exception as e:
                print(f"备用Embedding接口也失败: {e}")
                return None

        # 尝试主接口
        for attempt in range(self.max_retries):
            try:
                result = self._call_embedding(self.url, text)
                return result
            except Exception as e:
                if attempt < self.max_retries - 1:
                    continue
                print(f"主Embedding接口失败: {e}")
                self._primary_failed = True

                # 尝试备用接口
                if self.fallback_url:
                    print(f"尝试备用接口: {self.fallback_url}")
                    try:
                        return self._call_embedding(self.fallback_url, text)
                    except Exception as e2:
                        print(f"备用Embedding接口也失败: {e2}")

        return None


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
                    # 更长的关键词权重更高
                    score += len(keyword) * 0.1

            if matched_keywords:
                scores[domain] = score

        # 归一化并排序
        if scores:
            max_score = max(scores.values())
            results = [(k, v/max_score) for k, v in scores.items()]
            return sorted(results, key=lambda x: x[1], reverse=True)
        return []

    @staticmethod
    def get_search_terms(question: str, domain: str = None) -> List[str]:
        """根据问题和数据域生成多个搜索词"""
        terms = [question]  # 原始问题

        # 添加指标相关搜索词
        for indicator, hints in INDICATOR_MAPPING.items():
            if indicator in question:
                terms.extend(hints)

        # 添加数据域相关搜索词
        if domain and domain in DATA_DOMAINS:
            terms.extend(DATA_DOMAINS[domain].get("search_hints", []))

        return list(set(terms))


class TableSearcher:
    """表检索器"""

    def __init__(self, config: Config):
        self.config = config
        self.es_host = config.get("elasticsearch", "host", default="http://localhost:9200", env_var="ES_HOST")
        self.es_index = config.get("elasticsearch", "index", default="db_meta", env_var="ES_INDEX")
        self.es_username = config.get("elasticsearch", "username", default="", env_var="ES_USERNAME")
        self.es_password = config.get("elasticsearch", "password", default="", env_var="ES_PASSWORD")
        self.request_timeout = config.get("elasticsearch", "request_timeout", default=20)
        self.default_top_k = config.get("search", "default_top_k", default=20)
        self.max_tables = config.get("search", "max_tables", default=8)
        self.max_columns = config.get("search", "max_columns_per_table", default=8)

        self.embedding_client = EmbeddingClient(config)
        self.es = None

    def connect(self):
        if self.es_username and self.es_password:
            self.es = Elasticsearch(
                self.es_host,
                basic_auth=(self.es_username, self.es_password),
                request_timeout=self.request_timeout,
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
            # 完全匹配场景关键词
            if scenario in question:
                matched_tables.extend(tables)
                continue
            # 分词匹配：场景关键词的每个词都在问题中出现
            scenario_words = scenario.split()
            if len(scenario_words) >= 2 and all(w in question for w in scenario_words):
                matched_tables.extend(tables)

        # 去重保序
        return list(dict.fromkeys(matched_tables))

    def search_with_domain_filter(self, question: str, domain: str = None, top_k: int = None) -> List[dict]:
        """带数据域过滤的搜索"""
        if top_k is None:
            top_k = self.default_top_k

        query_vec = self.embedding_client.get_embedding(question)
        if not query_vec:
            query_vec = [0.0] * 1024

        # 构建查询
        must_clauses = []
        should_clauses = []

        # 如果识别出数据域，添加 path 过滤
        if domain and domain in DATA_DOMAINS:
            path_patterns = DATA_DOMAINS[domain].get("path_patterns", [])
            if path_patterns:
                path_should = []
                for pattern in path_patterns:
                    path_should.append({"match": {"path": pattern}})
                # path 匹配作为 boost 而不是硬过滤
                should_clauses.append({
                    "bool": {
                        "should": path_should,
                        "boost": 2.0
                    }
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
            # 英文表名/字段名搜索
            {"match": {"table_name": {"query": question, "boost": 2.0}}},
        ])

        # 向量检索
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

        query = {
            "_source": ["type", "table_id", "table_name", "table_chi_name", "path",
                       "description", "relations", "column_name", "column_chi_name",
                       "column_type", "remark", "search_text"],
            "query": {
                "bool": {
                    "must": must_clauses if must_clauses else [{"match_all": {}}],
                    "should": should_clauses,
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

    def multi_term_search(self, question: str, domain: str = None) -> List[dict]:
        """多搜索词组合搜索"""
        all_hits = {}
        search_terms = DomainRecognizer.get_search_terms(question, domain)

        for term in search_terms[:5]:  # 最多5个搜索词
            hits = self.search_with_domain_filter(term, domain, top_k=30)
            for hit in hits:
                doc_id = hit["_id"]
                if doc_id not in all_hits or hit["_score"] > all_hits[doc_id]["_score"]:
                    all_hits[doc_id] = hit

        # 按分数排序
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
                        "relations": []
                    }
                tables[table_id]["columns"].append({
                    "info": src,
                    "score": score
                })
                if score > tables[table_id]["table_score"]:
                    tables[table_id]["table_score"] = score

        sorted_tables = sorted(tables.values(), key=lambda x: x["table_score"], reverse=True)

        for t in sorted_tables:
            t["columns"] = sorted(t["columns"], key=lambda x: x["score"], reverse=True)[:self.max_columns]

        return sorted_tables[:self.max_tables]

    def format_output(self, grouped: List[dict], question: str, domain: str = None, scenario_tables: List[str] = None) -> str:
        """生成结构化文本描述"""
        lines = []
        lines.append(f"# 用户问题")
        lines.append(f"{question}")

        if domain:
            lines.append(f"\n识别数据域: **{domain}**")

        # 场景匹配提示
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

            lines.append(f"## {i}. {table_name}（{table_chi_name}）")
            lines.append(f"- 路径: {table.get('path', 'N/A')}")
            lines.append(f"- 描述: {table.get('description', 'N/A')}")

            relations = table.get("relations", [])
            if relations:
                lines.append(f"- 关联表: {', '.join(relations)}")

            columns = item.get("columns", [])
            if columns:
                lines.append("- 相关字段:")
                for col in columns[:self.max_columns]:
                    c = col.get("info", {})
                    col_name = c.get("column_name", "")
                    col_chi_name = c.get("column_chi_name", "")
                    col_type = c.get("column_type", "")
                    remark = c.get("remark", "")

                    if remark and len(remark) > 60:
                        remark = remark[:60] + "..."

                    remark_str = f" # {remark}" if remark else ""
                    lines.append(f"  - {col_name} ({col_chi_name}): {col_type}{remark_str}")

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

        return "\n".join(lines)

    def search_tables(self, question: str, top_k: int = None) -> str:
        """主函数: 检索并返回结构化文本"""
        if not self.es:
            self.connect()

        # 1. 识别数据域
        domains = DomainRecognizer.recognize(question)
        primary_domain = domains[0][0] if domains else None

        if domains:
            print(f"[识别数据域] {domains}")

        # 2. 场景匹配，优先推荐最优表
        scenario_tables = self._match_scenario(question)
        if scenario_tables:
            print(f"[场景匹配] 推荐表: {scenario_tables}")

        # 3. 多搜索词搜索
        hits = self.multi_term_search(question, primary_domain)

        # 4. 聚合结果
        grouped = self.group_results(hits)

        # 5. 将场景匹配的表提升到结果前列
        if scenario_tables:
            grouped = self._promote_scenario_tables(grouped, scenario_tables)

        return self.format_output(grouped, question, primary_domain, scenario_tables)

    def _promote_scenario_tables(self, grouped: List[dict], scenario_tables: List[str]) -> List[dict]:
        """将场景匹配的表提升到结果前列，如果不在结果中则从ES查询补充"""
        # 已在结果中的场景表
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

        # 按场景表顺序重新排列
        promoted = []
        for table_name in scenario_tables:
            if table_name in in_result:
                promoted.append(in_result[table_name])
            else:
                # 尝试从ES查询该表的详细信息
                table_info = self._fetch_table_by_name(table_name)
                if table_info:
                    promoted.append(table_info)

        # 加上其他结果
        promoted.extend(others)

        return promoted[:self.max_tables]

    def _fetch_table_by_name(self, table_name: str) -> Optional[dict]:
        """根据表名从ES获取表信息"""
        try:
            query = {
                "_source": ["type", "table_id", "table_name", "table_chi_name", "path",
                           "description", "relations"],
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
                    "table_score": 100  # 场景推荐的表给予高分
                }
        except Exception as e:
            pass
        return None


def main():
    parser = argparse.ArgumentParser(description="检索相关数据库表")
    parser.add_argument("question", help="用户的自然语言问题")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--top-k", "-k", type=int, help="返回结果数量")
    parser.add_argument("--json", "-j", action="store_true", help="以JSON格式输出")
    args = parser.parse_args()

    config = Config(args.config)
    searcher = TableSearcher(config)

    result = searcher.search_tables(args.question, args.top_k)

    if args.json:
        output = {"question": args.question, "result": result}
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(result)


if __name__ == "__main__":
    main()
