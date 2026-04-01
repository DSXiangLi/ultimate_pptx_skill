#!/usr/bin/env python3
"""
公募基金信息查询（业绩+评级）
用法:
    python fund_info.py 008263                    # 基金业绩
    python fund_info.py 008263 --rating           # 基金评级
    python fund_info.py 008263 --history          # 净值历史
    python fund_info.py --type 灵活配置 --top 20   # 按类型筛选排名

功能:
  1. 净值和各期收益率
  2. 基金星级评级
  3. 按类型筛选排名
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

import argparse
import re
from pathlib import Path
from typing import List

import pandas as pd
import pymysql
import yaml

def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def parse_env(value: str) -> str:
    """解析 ${VAR} 和 ${VAR:-default} 格式"""
    if not isinstance(value, str):
        return value
    pattern = r'\$\{([^}:]+)(?::-([^}]*))?\}'
    match = re.search(pattern, value)
    if match:
        var_name = match.group(1)
        default = match.group(2) if match.group(2) is not None else ''
        return os.environ.get(var_name, default)
    return value

def get_connection(config: dict) -> pymysql.Connection:
    mysql = config["mysql"]
    # 修复：port 可能是字符串，需要转换为整数
    port = mysql.get("port", 3306)
    if isinstance(port, str):
        port = int(port) if port.isdigit() else 3306
    return pymysql.connect(
        host=parse_env(mysql["host"]),
        port=port,
        user=parse_env(mysql["user"]),
        password=parse_env(mysql["password"]),
        database=parse_env(mysql["database"]),
        charset=mysql.get("charset", "utf8mb4"),
    )

def format_codes(codes: List[str]) -> str:
    return "(" + ", ".join(f"'{c}'" for c in codes) + ")"

class FundInfoQuery:
    """公募基金信息查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_performance(self, codes: List[str]) -> pd.DataFrame:
        """获取业绩表现"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                p.TradingDay as 日期,
                p.UnitNV as 净值,
                p.RRInSingleMonth as 近1月,
                p.RRInThreeMonth as 近3月,
                p.RRInSixMonth as 近6月,
                p.RRSinceThisYear as 今年以来,
                p.RRInSingleYear as 近1年,
                p.AnnualizedRRInThreeYear as 近3年年化
            FROM SecuMain sm
            JOIN mf_netvalueperformance p ON sm.InnerCode = p.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND p.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode, p.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        if not df.empty:
            df = df.drop_duplicates(subset=['代码'], keep='first')
        return df

    def get_netvalue_history(self, codes: List[str], months: int = 6) -> pd.DataFrame:
        """获取净值历史"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                p.TradingDay as 日期,
                p.UnitNV as 净值,
                p.NVDailyGrowthRate as 日涨跌
            FROM SecuMain sm
            JOIN mf_netvalueperformance p ON sm.InnerCode = p.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND p.TradingDay >= DATE_SUB(CURDATE(), INTERVAL {months} MONTH)
            ORDER BY sm.SecuCode, p.TradingDay DESC
        """
        return pd.read_sql(sql, self.conn)

    def get_rating(self, codes: List[str]) -> pd.DataFrame:
        """获取基金评级"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                r.FundTypeName as 类型,
                r.StarRank as 三年星,
                r.StarRank5Y as 五年星
            FROM SecuMain sm
            JOIN mf_txsecfundrating r ON sm.InnerCode = r.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            ORDER BY sm.SecuCode, r.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        if not df.empty:
            df = df.drop_duplicates(subset=['代码'], keep='first')
        return df

    def get_top_by_type(self, fund_type: str, top_n: int = 20) -> pd.DataFrame:
        """按类型获取排名靠前的基金"""
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                r.FundTypeName as 类型,
                r.StarRank as 三年星
            FROM SecuMain sm
            JOIN mf_txsecfundrating r ON sm.InnerCode = r.InnerCode
            WHERE r.EndDate = (SELECT MAX(EndDate) FROM mf_txsecfundrating)
            AND r.FundTypeName LIKE '%{fund_type}%'
            AND r.StarRank IS NOT NULL
            ORDER BY r.StarRank DESC
            LIMIT {top_n}
        """
        return pd.read_sql(sql, self.conn)

def print_table(df: pd.DataFrame, title: str = None, max_rows: int = 10):
    """打印表格"""
    if title:
        print(f"\n### {title}\n")
    if df.empty:
        print("*无数据*")
        return

    total = len(df)
    df_show = df.head(max_rows) if total > max_rows else df

    print("| " + " | ".join(str(c) for c in df_show.columns) + " |")
    print("|" + "|".join(["---"] * len(df_show.columns)) + "|")

    for _, row in df_show.iterrows():
        values = []
        for col in df_show.columns:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif hasattr(val, 'strftime'):
                values.append(val.strftime('%Y-%m-%d'))
            elif isinstance(val, float):
                if '率' in str(col) or '年' in str(col) or '近' in str(col) or '来' in str(col) or '涨' in str(col):
                    values.append(f"{val:.2f}%")
                else:
                    values.append(f"{val:.4f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共{total}条*")

def main():
    parser = argparse.ArgumentParser(
        description="公募基金信息查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 008263                  # 业绩表现
  %(prog)s 008263 --rating         # 评级
  %(prog)s 008263 --history        # 净值历史
  %(prog)s --type 灵活配置 --top 20 # 类型排名
        """
    )
    parser.add_argument("codes", nargs="?", help="基金代码")
    parser.add_argument("--rating", "-r", action="store_true", help="显示评级")
    parser.add_argument("--history", action="store_true", help="净值历史")
    parser.add_argument("--type", "-t", help="按类型筛选")
    parser.add_argument("--top", type=int, default=20, help="显示前N名")
    parser.add_argument("--months", type=int, default=6, help="历史月数")
    parser.add_argument("--output", "-o", help="导出Excel")
    args = parser.parse_args()

    config = load_config()
    conn = get_connection(config)
    query = FundInfoQuery(conn)

    try:
        results = {}

        if args.type:
            df = query.get_top_by_type(args.type, args.top)
            print(f"\n{'='*20} {args.type}前{args.top} {'='*20}")
            print_table(df, f"{args.type}前{args.top}")
            results["排名"] = df

        elif args.codes:
            codes = [c.strip() for c in args.codes.split(",")]
            print(f"查询: {codes}")

            if args.history:
                df = query.get_netvalue_history(codes, args.months)
                print(f"\n{'='*20} 净值历史(近{args.months}月) {'='*20}")
                print_table(df, "净值历史", max_rows=15)
                results["净值历史"] = df
            elif args.rating:
                df = query.get_rating(codes)
                print(f"\n{'='*20} 基金评级 {'='*20}")
                print_table(df, "评级")
                results["评级"] = df
            else:
                df = query.get_performance(codes)
                print(f"\n{'='*20} 业绩表现 {'='*20}")
                print_table(df, "业绩表现")
                results["业绩"] = df

        else:
            print("请指定基金代码或使用 --type 筛选")
            return

        if args.output:
            with pd.ExcelWriter(args.output, engine='openpyxl') as writer:
                for name, df in results.items():
                    if not df.empty:
                        df.to_excel(writer, sheet_name=name[:31], index=False)
            print(f"\n已导出: {args.output}")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
