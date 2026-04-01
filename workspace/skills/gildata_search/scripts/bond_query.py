#!/usr/bin/env python3
"""
债券数据快捷查询
用法:
    python bond_query.py 010107              # 国债行情
    python bond_query.py 010107 --yield  # 收益率
    python bond_query.py --list             # 主要债券列表
    python bond_query.py --treasury      # 国债列表
    python bond_query.py --corporate     # 企业债列表
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

class BondQuery:
    """债券数据查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_quote(self, codes: List[str]) -> pd.DataFrame:
        """债券行情 - 综合银行间和交易所"""
        codes_str = "(" + ", ".join(f"'{c}'" for c in codes) + ")"

        # 先查银行间债券
        sql_interbank = f"""
            SELECT sm.SecuCode as 代码, sm.SecuAbbr as 名称,
                   q.TradingDay as 日期, q.CloseNetPrice as 净价,
                   q.YTM_CL as 到期收益率, q.ModifiedDuration_CL as 修正久期,
                   q.TurnoverVolume as 成交量_张
            FROM bond_code sm
            LEFT JOIN bond_interbankquote q ON sm.InnerCode = q.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND q.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode, q.TradingDay DESC
        """
        df1 = pd.read_sql(sql_interbank, self.conn)

        # 再查交易所债券
        sql_exchange = f"""
            SELECT sm.SecuCode as 代码, sm.SecuAbbr as 名称,
                   q.TradingDay as 日期, q.CloseNetPrice as 净价,
                   q.YTM_CL as 到期收益率, q.ModifiedDuration_CL as 修正久期,
                   q.TurnoverVolume as 成交量_张
            FROM bond_code sm
            LEFT JOIN bond_exchangequotefi q ON sm.InnerCode = q.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND q.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode, q.TradingDay DESC
        """
        df2 = pd.read_sql(sql_exchange, self.conn)

        # 合并结果
        if not df1.empty:
            df1 = df1.drop_duplicates(subset=['代码'], keep='first')
        if not df2.empty:
            df2 = df2.drop_duplicates(subset=['代码'], keep='first')

        # 优先使用银行间数据
        if not df1.empty:
            return df1
        return df2

    def get_yield_curve(self, bond_type: str = "国债") -> pd.DataFrame:
        """收益率曲线 - 暂不可用"""
        return pd.DataFrame({"提示": ["收益率曲线功能暂不可用，请使用债券行情查询"]})

    def list_treasury_bonds(self, top_n: int = 20) -> pd.DataFrame:
        """国债列表"""
        sql = f"""
            SELECT SecuCode as 代码, SecuAbbr as 名称,
                   Issuer as 发行人, InterestEndDate as 到期日
            FROM bond_code
            WHERE BondTypeLevel1 = 1000
            AND ListedState = 1
            ORDER BY ListedDate DESC
            LIMIT {top_n}
        """
        return pd.read_sql(sql, self.conn)

    def list_corporate_bonds(self, top_n: int = 20) -> pd.DataFrame:
        """企业债列表"""
        sql = f"""
            SELECT SecuCode as 代码, SecuAbbr as 名称,
                   Issuer as 发行人, InterestEndDate as 到期日
            FROM bond_code
            WHERE BondTypeLevel1 = 1300
            AND ListedState = 1
            ORDER BY ListedDate DESC
            LIMIT {top_n}
        """
        return pd.read_sql(sql, self.conn)

    def list_main_bonds(self, top_n: int = 30) -> pd.DataFrame:
        """主要债券列表"""
        sql = f"""
            SELECT SecuCode as 代码, SecuAbbr as 名称,
                   BondTypeLevel1Desc as 债券类型, Issuer as 发行人,
                   InterestEndDate as 到期日
            FROM bond_code
            WHERE ListedState = 1
            ORDER BY ListedDate DESC
            LIMIT {top_n}
        """
        return pd.read_sql(sql, self.conn)

def print_table(df: pd.DataFrame, title: str = None, max_rows: int = 20):
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
                if '率' in str(col) or '收益' in str(col):
                    values.append(f"{val:.2f}%")
                else:
                    values.append(f"{val:.4f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")
    if total > max_rows:
        print(f"\n*共{total}条，显示前{max_rows}条*")

def main():
    parser = argparse.ArgumentParser(description="债券数据查询")
    parser.add_argument("codes", nargs="?", help="债券代码")
    parser.add_argument("--ytm", action="store_true", help="收益率曲线")
    parser.add_argument("--list", action="store_true", help="主要债券列表")
    parser.add_argument("--treasury", action="store_true", help="国债列表")
    parser.add_argument("--corporate", action="store_true", help="企业债列表")
    parser.add_argument("--top", type=int, default=20, help="显示前N条")
    parser.add_argument("--output", "-o", help="导出Excel")
    args = parser.parse_args()

    config = load_config()
    conn = get_connection(config)
    query = BondQuery(conn)

    try:
        results = {}

        if args.list:
            df = query.list_main_bonds(args.top)
            print(f"\n{'='*20} 主要债券 {'='*20}")
            print_table(df, "主要债券", max_rows=args.top)
            results["主要债券"] = df
        elif args.treasury:
            df = query.list_treasury_bonds(args.top)
            print(f"\n{'='*20} 国债列表 {'='*20}")
            print_table(df, "国债列表", max_rows=args.top)
            results["国债列表"] = df
        elif args.corporate:
            df = query.list_corporate_bonds(args.top)
            print(f"\n{'='*20} 企业债列表 {'='*20}")
            print_table(df, "企业债列表", max_rows=args.top)
            results["企业债列表"] = df
        elif args.ytm and args.codes:
            bond_type = "国债"  # 默认国债
            if "企业" in args.codes or "03" in args.codes:
                bond_type = "企业债"
            elif "金融" in args.codes or "02" in args.codes:
                bond_type = "金融债"
            df = query.get_yield_curve(bond_type)
            print(f"\n{'='*20} {bond_type}收益率曲线 {'='*20}")
            print_table(df, f"{bond_type}收益率曲线", max_rows=30)
            results[f"{bond_type}收益率曲线"] = df
        elif args.codes:
            codes = [c.strip() for c in args.codes.split(",")]
            print(f"查询: {codes}")
            df = query.get_quote(codes)
            print(f"\n{'='*20} 债券行情 {'='*20}")
            print_table(df, "行情")
            results["行情"] = df
        else:
            # 默认显示主要债券
            df = query.list_main_bonds(args.top)
            print(f"\n{'='*20} 主要债券 {'='*20}")
            print_table(df, "主要债券", max_rows=args.top)
            results["主要债券"] = df

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
