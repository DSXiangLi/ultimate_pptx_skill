#!/usr/bin/env python3
"""
公募基金经理/公司查询
用法:
    python fund_manager.py 008263               # 基金经理
    python fund_manager.py 008263 --history     # 历任经理
    python fund_manager.py --name 张坤          # 搜索经理
    python fund_manager.py --name 张坤 --funds  # 经理管理的基金
    python fund_manager.py --company 天弘       # 搜索公司
    python fund_manager.py --top 20             # 公司规模排名

功能:
  1. 基金经理信息
  2. 基金公司规模排名
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

class FundManagerQuery:
    """基金经理/公司查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_fund_managers(self, codes: List[str], history: bool = False) -> pd.DataFrame:
        """获取基金经理"""
        codes_str = format_codes(codes)
        incumbent_filter = "" if history else "AND m.Incumbent = 1"

        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                m.Name as 经理,
                CASE m.Incumbent WHEN 1 THEN '在任' ELSE '离任' END as 状态,
                m.AccessionDate as 到任,
                m.ManagementTime as 天数,
                m.Performance*100 as 收益率
            FROM SecuMain sm
            JOIN mf_fundmanagernew m ON sm.InnerCode = m.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            {incumbent_filter}
            ORDER BY sm.SecuCode, m.Incumbent DESC, m.AccessionDate DESC
        """
        return pd.read_sql(sql, self.conn)

    def search_manager(self, name: str) -> pd.DataFrame:
        """搜索经理"""
        sql = f"""
            SELECT DISTINCT
                m.Name as 经理,
                COUNT(DISTINCT m.InnerCode) as 管理数,
                SUM(CASE WHEN m.Incumbent = 1 THEN 1 ELSE 0 END) as 在管
            FROM mf_fundmanagernew m
            WHERE m.Name LIKE '%{name}%'
            GROUP BY m.Name
        """
        return pd.read_sql(sql, self.conn)

    def get_manager_funds(self, name: str) -> pd.DataFrame:
        """经理管理的基金"""
        sql = f"""
            SELECT
                sm.SecuCode as 代码,
                sm.ChiNameAbbr as 简称,
                m.Name as 经理,
                CASE m.Incumbent WHEN 1 THEN '在任' ELSE '离任' END as 状态,
                m.ManagementTime as 天数,
                m.Performance*100 as 收益率
            FROM SecuMain sm
            JOIN mf_fundmanagernew m ON sm.InnerCode = m.InnerCode
            WHERE m.Name LIKE '%{name}%'
            ORDER BY m.Incumbent DESC, m.AccessionDate DESC
        """
        return pd.read_sql(sql, self.conn)

    def search_company(self, name: str) -> pd.DataFrame:
        """搜索公司"""
        sql = f"""
            SELECT
                i.ChiName as 公司,
                r.TotalFundNV as 总规模_亿,
                r.FundNVRank as 排名,
                r.TotalFundN as 基金数,
                r.EquityFundNV as 股票_亿,
                r.BondFundNV as 债券_亿
            FROM mf_advisorscalerank r
            JOIN lc_instiarchive i ON r.InvestAdvisorCode = i.CompanyCode
            WHERE r.EndDate = (SELECT MAX(EndDate) FROM mf_advisorscalerank)
            AND i.ChiName LIKE '%{name}%'
        """
        return pd.read_sql(sql, self.conn)

    def get_top_companies(self, fund_type: str = "总规模", top_n: int = 20) -> pd.DataFrame:
        """公司规模排名"""
        type_map = {
            "总规模": ("TotalFundNV", "FundNVRank"),
            "股票": ("EquityFundNV", "EquityNVRank"),
            "混合": ("HybridFundNV", "HybridNVRank"),
            "债券": ("BondFundNV", "BondNVRank"),
            "货币": ("MonetaryFundNV", "MonetaryNVRank"),
        }
        field, rank_field = type_map.get(fund_type, ("TotalFundNV", "FundNVRank"))

        sql = f"""
            SELECT
                i.ChiName as 公司,
                r.{field} as 规模_亿,
                r.{rank_field} as 排名,
                r.TotalFundN as 基金数
            FROM mf_advisorscalerank r
            JOIN lc_instiarchive i ON r.InvestAdvisorCode = i.CompanyCode
            WHERE r.EndDate = (SELECT MAX(EndDate) FROM mf_advisorscalerank)
            AND r.{field} IS NOT NULL
            ORDER BY r.{field} DESC
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
                if '率' in str(col):
                    values.append(f"{val:.2f}%")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(int(val)) if isinstance(val, (int, float)) and not isinstance(val, bool) else str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共{total}条*")

def main():
    parser = argparse.ArgumentParser(
        description="基金经理/公司查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 008263                  # 基金经理
  %(prog)s 008263 --history        # 历任经理
  %(prog)s --name 张坤             # 搜索经理
  %(prog)s --name 张坤 --funds     # 经理的基金
  %(prog)s --company 天弘          # 搜索公司
  %(prog)s --top 20                # 公司排名
  %(prog)s --type 股票 --top 10    # 股票规模排名
        """
    )
    parser.add_argument("codes", nargs="?", help="基金代码")
    parser.add_argument("--name", "-n", help="经理姓名")
    parser.add_argument("--funds", action="store_true", help="经理管理的基金")
    parser.add_argument("--history", action="store_true", help="历任经理")
    parser.add_argument("--company", "-c", help="公司名称")
    parser.add_argument("--top", type=int, default=20, help="显示前N名")
    parser.add_argument("--type", "-t", default="总规模", help="类型: 总规模/股票/混合/债券/货币")
    parser.add_argument("--output", "-o", help="导出Excel")
    args = parser.parse_args()

    config = load_config()
    conn = get_connection(config)
    query = FundManagerQuery(conn)

    try:
        results = {}

        if args.name:
            if args.funds:
                df = query.get_manager_funds(args.name)
                print(f"\n{'='*20} {args.name}管理的基金 {'='*20}")
                print_table(df, f"{args.name}管理基金")
            else:
                df = query.search_manager(args.name)
                print(f"\n{'='*20} 搜索: {args.name} {'='*20}")
                print_table(df, "搜索结果")
            results["经理"] = df

        elif args.company:
            df = query.search_company(args.company)
            print(f"\n{'='*20} 搜索: {args.company} {'='*20}")
            print_table(df, "搜索结果")
            results["公司"] = df

        elif not args.codes:
            df = query.get_top_companies(args.type, args.top)
            print(f"\n{'='*20} {args.type}前{args.top} {'='*20}")
            print_table(df, f"{args.type}前{args.top}")
            results["排名"] = df

        else:
            codes = [c.strip() for c in args.codes.split(",")]
            print(f"查询: {codes}")
            df = query.get_fund_managers(codes, args.history)
            title = "历任经理" if args.history else "现任经理"
            print(f"\n{'='*20} {title} {'='*20}")
            print_table(df, title)
            results["经理"] = df

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
