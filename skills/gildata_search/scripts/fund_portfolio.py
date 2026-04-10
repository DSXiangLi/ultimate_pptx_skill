#!/usr/bin/env python3
"""
公募基金持仓查询
用法:
    python fund_portfolio.py 008263               # 股票持仓
    python fund_portfolio.py 008263 --top 20      # 前20大持仓
    python fund_portfolio.py 008263 --allocation  # 资产配置
    python fund_portfolio.py 008263 --industry    # 行业配置
    python fund_portfolio.py 008263 --history     # 持仓历史

功能:
  1. 股票持仓明细
  2. 资产配置比例
  3. 行业配置
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

class FundPortfolioQuery:
    """公募基金持仓查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_stock_holdings(self, codes: List[str], top_n: int = 10) -> pd.DataFrame:
        """股票持仓"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                p.ReportDate as 报告期,
                p.SerialNumber as 序号,
                stk.SecuCode as 股票,
                stk.ChiNameAbbr as 名称,
                p.MarketValue/1e8 as 市值_亿,
                p.RatioInNV*100 as 占比
            FROM SecuMain sm
            JOIN mf_stockportfoliodetail p ON sm.InnerCode = p.InnerCode
            JOIN SecuMain stk ON p.StockInnerCode = stk.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND p.ReportDate = (
                SELECT MAX(ReportDate) FROM mf_stockportfoliodetail WHERE InnerCode = sm.InnerCode
            )
            AND p.SerialNumber <= {top_n}
            ORDER BY sm.SecuCode, p.RatioInNV DESC
        """
        return pd.read_sql(sql, self.conn)

    def get_asset_allocation(self, codes: List[str]) -> pd.DataFrame:
        """资产配置"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                a.ReportDate as 报告期,
                a.NV/1e8 as 净值_亿,
                a.RINOfStock*100 as 股票,
                a.RINOfBond*100 as 债券,
                a.RINOfMonetary*100 as 现金,
                a.RINOfHKConnect*100 as 港股
            FROM SecuMain sm
            JOIN mf_assetallocationnew a ON sm.InnerCode = a.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            ORDER BY sm.SecuCode, a.ReportDate DESC
            LIMIT 20
        """
        return pd.read_sql(sql, self.conn)

    def get_industry_allocation(self, codes: List[str]) -> pd.DataFrame:
        """行业配置 - 使用mf_fundindustryalloy表"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                i.ReportDate as 报告期,
                i.IndustryName as 行业,
                i.RatioInNV*100 as 占比,
                i.MarketValue/1e8 as 市值_亿
            FROM SecuMain sm
            JOIN mf_fundindustryalloy i ON sm.InnerCode = i.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND i.ReportDate = (
                SELECT MAX(ReportDate) FROM mf_fundindustryalloy WHERE InnerCode = sm.InnerCode
            )
            ORDER BY sm.SecuCode, i.RatioInNV DESC
        """
        return pd.read_sql(sql, self.conn)

    def get_holding_history(self, codes: List[str], stock_code: str = None) -> pd.DataFrame:
        """持仓历史"""
        codes_str = format_codes(codes)
        stock_filter = f"AND stk.SecuCode = '{stock_code}'" if stock_code else ""
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                p.ReportDate as 报告期,
                stk.SecuCode as 股票,
                stk.ChiNameAbbr as 名称,
                p.SharesHolding/10000 as 持仓_万,
                p.RatioInNV*100 as 占比
            FROM SecuMain sm
            JOIN mf_stockportfoliodetail p ON sm.InnerCode = p.InnerCode
            JOIN SecuMain stk ON p.StockInnerCode = stk.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            {stock_filter}
            ORDER BY sm.SecuCode, p.ReportDate DESC, p.RatioInNV DESC
            LIMIT 100
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
                if '比' in str(col):
                    values.append(f"{val:.2f}%")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共{total}条*")

def main():
    parser = argparse.ArgumentParser(
        description="公募基金持仓查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 008263                  # 股票持仓
  %(prog)s 008263 --top 20         # 前20大
  %(prog)s 008263 --allocation     # 资产配置
  %(prog)s 008263 --industry       # 行业配置
  %(prog)s 008263 --history        # 持仓历史
  %(prog)s 008263 --stock 600519   # 某股票历史
        """
    )
    parser.add_argument("codes", help="基金代码")
    parser.add_argument("--top", type=int, default=10, help="前N大持仓")
    parser.add_argument("--allocation", "-a", action="store_true", help="资产配置")
    parser.add_argument("--industry", "-i", action="store_true", help="行业配置")
    parser.add_argument("--history", action="store_true", help="持仓历史")
    parser.add_argument("--stock", help="指定股票")
    parser.add_argument("--output", "-o", help="导出Excel")
    args = parser.parse_args()

    config = load_config()
    conn = get_connection(config)
    query = FundPortfolioQuery(conn)

    try:
        codes = [c.strip() for c in args.codes.split(",")]
        print(f"查询: {codes}")
        results = {}

        # 默认显示持仓
        if not args.allocation and not args.industry and not args.history:
            df = query.get_stock_holdings(codes, args.top)
            print(f"\n{'='*20} 股票持仓(前{args.top}) {'='*20}")
            print_table(df, f"股票持仓前{args.top}")
            results["持仓"] = df

        if args.allocation:
            df = query.get_asset_allocation(codes)
            print(f"\n{'='*20} 资产配置 {'='*20}")
            print_table(df, "资产配置")
            results["配置"] = df

        if args.industry:
            df = query.get_industry_allocation(codes)
            print(f"\n{'='*20} 行业配置 {'='*20}")
            print_table(df, "行业配置")
            results["行业"] = df

        if args.history:
            df = query.get_holding_history(codes, args.stock)
            print(f"\n{'='*20} 持仓历史 {'='*20}")
            print_table(df, "持仓历史", max_rows=20)
            results["历史"] = df

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
