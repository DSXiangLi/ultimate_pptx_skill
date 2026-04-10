#!/usr/bin/env python3
"""
指数数据快捷查询
用法:
    python index_query.py 000300                # 沪深300行情
    python index_query.py 000300 --pe           # 估值历史
    python index_query.py 000300 --components   # 成分股
    python index_query.py --list                # 主要指数列表
    python index_query.py --top 20              # 涨幅排名
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


class IndexQuery:
    """指数数据查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_quote(self, codes: List[str]) -> pd.DataFrame:
        """指数行情"""
        codes_str = "(" + ", ".join(f"'{c}'" for c in codes) + ")"
        sql = f"""
            SELECT sm.SecuCode as 代码, sm.ChiNameAbbr as 简称,
                   q.TradingDay as 日期, q.ClosePrice as 收盘价,
                   q.TurnoverValue/1e8 as 成交额_亿, q.TurnoverVolume/1e8 as 成交量_亿
            FROM SecuMain sm
            JOIN QT_CSIIndexQuote q ON sm.InnerCode = q.IndexCode
            WHERE sm.SecuCode IN {codes_str}
            AND q.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode, q.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.drop_duplicates(subset=['代码'], keep='first') if not df.empty else df

        # 获取估值数据
        sql2 = f"""
            SELECT sm.SecuCode as 代码,
                   v.PE as PE_TTM, v.PB, v.PS, v.DividendRatio as 股息率
            FROM SecuMain sm
            JOIN LC_DIndicesForValuation v ON sm.InnerCode = v.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND v.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode, v.TradingDay DESC
        """
        df2 = pd.read_sql(sql2, self.conn)
        if not df2.empty:
            df2 = df2.drop_duplicates(subset=['代码'], keep='first')
            df = df.merge(df2, on='代码', how='left')

        return df

    def get_pe_history(self, codes: List[str], months: int = 12) -> pd.DataFrame:
        """估值历史 - 使用 QT_CSIIndexQuote 表"""
        codes_str = "(" + ", ".join(f"'{c}'" for c in codes) + ")"
        sql = f"""
            SELECT sm.SecuCode as 代码, sm.ChiNameAbbr as 简称,
                   q.TradingDay as 日期,
                   q.IndexPERatio1 as PE_TTM,
                   q.IndexDYRatio1 as 股息率
            FROM SecuMain sm
            JOIN QT_CSIIndexQuote q ON sm.InnerCode = q.IndexCode
            WHERE sm.SecuCode IN {codes_str}
            AND q.TradingDay >= DATE_SUB(CURDATE(), INTERVAL {months} MONTH)
            ORDER BY sm.SecuCode, q.TradingDay DESC
        """
        return pd.read_sql(sql, self.conn)

    def get_components(self, code: str, top_n: int = 50) -> pd.DataFrame:
        """指数成分股"""
        sql = f"""
            SELECT sm.SecuCode as 指数代码, sm.ChiNameAbbr as 指数简称,
                   stk.SecuCode as 股票代码, stk.ChiNameAbbr as 股票简称,
                   c.Weight as 权重
            FROM SecuMain sm
            JOIN LC_IndexComponentsWeight c ON sm.InnerCode = c.IndexCode
            JOIN SecuMain stk ON c.InnerCode = stk.InnerCode
            WHERE sm.SecuCode = '{code}'
            AND c.EndDate = (SELECT MAX(EndDate) FROM LC_IndexComponentsWeight WHERE IndexCode = sm.InnerCode)
            ORDER BY c.Weight DESC
            LIMIT {top_n}
        """
        return pd.read_sql(sql, self.conn)

    def list_main_indices(self) -> pd.DataFrame:
        """主要指数列表"""
        sql = """
            SELECT sm.SecuCode as 代码, sm.ChiNameAbbr as 简称,
                   q.ClosePrice as 收盘价
            FROM SecuMain sm
            JOIN QT_CSIIndexQuote q ON sm.InnerCode = q.IndexCode
            WHERE sm.SecuCode IN ('000001', '000016', '000300', '000905', '000852',
                                  '399001', '399005', '399006', '399673', '399303')
            AND q.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode
        """
        df = pd.read_sql(sql, self.conn)
        df = df.drop_duplicates(subset=['代码'], keep='first') if not df.empty else df

        # 获取估值数据
        sql2 = """
            SELECT sm.SecuCode as 代码,
                   v.PE as PE_TTM, v.PB, v.DividendRatio as 股息率
            FROM SecuMain sm
            JOIN LC_DIndicesForValuation v ON sm.InnerCode = v.InnerCode
            WHERE sm.SecuCode IN ('000001', '000016', '000300', '000905', '000852',
                                  '399001', '399005', '399006', '399673', '399303')
            AND v.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            ORDER BY sm.SecuCode
        """
        df2 = pd.read_sql(sql2, self.conn)
        if not df2.empty:
            df2 = df2.drop_duplicates(subset=['代码'], keep='first')
            df = df.merge(df2, on='代码', how='left')

        return df

    def get_top_gainers(self, top_n: int = 20) -> pd.DataFrame:
        """涨幅排名"""
        sql = f"""
            SELECT sm.SecuCode as 代码, sm.ChiNameAbbr as 简称,
                   q.ClosePrice as 收盘价, q.ChangePCT as 涨跌幅,
                   q.TurnoverValue/1e8 as 成交额_亿
            FROM SecuMain sm
            JOIN QT_CSIIndexQuote q ON sm.InnerCode = q.IndexCode
            WHERE q.TradingDay >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
            AND sm.SecuCategory = 4
            ORDER BY q.ChangePCT DESC
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
                if '率' in str(col) or '股息' in str(col):
                    values.append(f"{val:.2f}%")
                elif 'PE' in str(col) or 'PB' in str(col):
                    values.append(f"{val:.2f}")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")
    if total > max_rows:
        print(f"\n*共{total}条，显示前{max_rows}条*")


def main():
    parser = argparse.ArgumentParser(description="指数数据查询")
    parser.add_argument("codes", nargs="?", help="指数代码")
    parser.add_argument("--pe", action="store_true", help="估值历史")
    parser.add_argument("--components", action="store_true", help="成分股")
    parser.add_argument("--list", action="store_true", help="主要指数列表")
    parser.add_argument("--top", type=int, default=20, help="显示前N条")
    parser.add_argument("--months", type=int, default=12, help="历史月数")
    parser.add_argument("--output", "-o", help="导出Excel")
    args = parser.parse_args()

    config = load_config()
    conn = get_connection(config)
    query = IndexQuery(conn)

    try:
        results = {}

        if args.list:
            df = query.list_main_indices()
            print(f"\n{'='*20} 主要指数 {'='*20}")
            print_table(df, "主要指数")
            results["指数列表"] = df
        elif args.top and not args.codes:
            df = query.get_top_gainers(args.top)
            print(f"\n{'='*20} 指数涨幅前{args.top} {'='*20}")
            print_table(df, f"涨幅前{args.top}")
            results["涨幅排名"] = df
        elif args.codes:
            codes = [c.strip() for c in args.codes.split(",")]
            print(f"查询: {codes}")

            if args.components:
                for code in codes:
                    df = query.get_components(code, args.top)
                    print(f"\n{'='*20} {code} 成分股(前{args.top}) {'='*20}")
                    print_table(df, f"成分股前{args.top}")
                    results[f"成分股_{code}"] = df
            elif args.pe:
                df = query.get_pe_history(codes, args.months)
                print(f"\n{'='*20} 估值历史(近{args.months}月) {'='*20}")
                print_table(df, "估值历史", max_rows=30)
                results["估值历史"] = df
            else:
                df = query.get_quote(codes)
                print(f"\n{'='*20} 指数行情 {'='*20}")
                print_table(df, "行情")
                results["行情"] = df
        else:
            # 默认显示主要指数
            df = query.list_main_indices()
            print(f"\n{'='*20} 主要指数 {'='*20}")
            print_table(df, "主要指数")
            results["指数列表"] = df

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
