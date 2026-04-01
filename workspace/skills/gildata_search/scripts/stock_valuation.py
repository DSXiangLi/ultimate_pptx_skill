#!/usr/bin/env python3
"""
股票估值数据综合查询（含分红历史）
用法:
    # 最新估值
    python stock_valuation.py 600519                        # 查询茅台估值
    python stock_valuation.py 600519,000858                 # 多股对比

    # 历史估值
    python stock_valuation.py 600519 --history              # 历史估值
    python stock_valuation.py 600519 --history -m 24        # 24个月历史

    # 估值分位数
    python stock_valuation.py 600519 --percentile           # 估值分位数
    python stock_valuation.py 600519 --percentile -m 24     # 24个月分位数

    # 分红历史
    python stock_valuation.py 600519 --dividend             # 分红历史
    python stock_valuation.py 600519 --dividend --stats     # 分红统计

    # 港股
    python stock_valuation.py 00700                         # 港股腾讯

数据表:
  - LC_DIndicesForValuation (A股估值指标)
  - QT_HKDailyQuoteIndex (港股估值指标)
  - dz_dividend (A股分红)
  - hk_dividend (港股分红)
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

from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional, Dict

import numpy as np
import pandas as pd
import pymysql
import yaml

# ============ 配置加载 ============
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

def is_hk_stock(code: str) -> bool:
    return len(code) == 5

def format_codes(codes: List[str]) -> str:
    return "(" + ", ".join(f"'{c}'" for c in codes) + ")"

# ============ A股估值查询 ============
class AShareValuationQuery:
    """A股估值数据查询"""

    VALUATION_COLUMNS = [
        "TradingDay", "TotalMV", "NegotiableMV",
        "PELYR", "PE", "PB", "PS", "PSTTM",
        "EnterpriseValueN", "EVToEBITDA", "DividendRatioLYR"
    ]

    COLUMN_MAPPING = {
        "TradingDay": "交易日期",
        "TotalMV": "总市值(亿)", "NegotiableMV": "流通市值(亿)",
        "PELYR": "PE(静)", "PE": "PE(TTM)",
        "PB": "PB(MRQ)",
        "PS": "PS(静)", "PSTTM": "PS(TTM)",
        "EnterpriseValueN": "企业价值(亿)", "EVToEBITDA": "EV/EBITDA",
        "DividendRatioLYR": "股息率(%)",
        "SecuCode": "股票代码", "SecuAbbr": "股票简称"
    }

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_latest_valuation(self, codes: List[str]) -> pd.DataFrame:
        """获取最新估值数据"""
        codes_str = format_codes(codes)
        cols = ", ".join(self.VALUATION_COLUMNS)

        sql = f"""
            SELECT SecuMain.SecuCode, SecuMain.ChiNameAbbr as SecuAbbr, {cols}
            FROM LC_DIndicesForValuation
            JOIN SecuMain ON LC_DIndicesForValuation.InnerCode = SecuMain.InnerCode
            WHERE SecuMain.SecuCode IN {codes_str}
            AND SecuMain.SecuCategory = 1 AND SecuMain.SecuMarket IN (18, 83, 90)
            AND TradingDay = (SELECT MAX(TradingDay) FROM LC_DIndicesForValuation)
            ORDER BY TotalMV DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)

        for col in ["总市值(亿)", "流通市值(亿)", "企业价值(亿)"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce') / 1e8

        return df

    def get_history_valuation(self, codes: List[str], months: int = 12) -> pd.DataFrame:
        """获取历史估值数据"""
        codes_str = format_codes(codes)
        cols = "TradingDay, TotalMV, PELYR, PB, PS, DividendRatioLYR"
        start_date = (datetime.now() - timedelta(days=months * 31)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT SecuMain.SecuCode, SecuMain.ChiNameAbbr as SecuAbbr, {cols}
            FROM LC_DIndicesForValuation
            JOIN SecuMain ON LC_DIndicesForValuation.InnerCode = SecuMain.InnerCode
            WHERE SecuMain.SecuCode IN {codes_str}
            AND SecuMain.SecuCategory = 1 AND SecuMain.SecuMarket IN (18, 83, 90)
            AND TradingDay >= '{start_date}'
            ORDER BY SecuMain.SecuCode, TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)
        df["总市值(亿)"] = pd.to_numeric(df["总市值(亿)"], errors='coerce') / 1e8
        return df

    def get_percentile(self, codes: List[str], months: int = 12) -> pd.DataFrame:
        """计算估值分位数"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=months * 31)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT SecuMain.SecuCode, SecuMain.ChiNameAbbr as SecuAbbr,
                   TradingDay, PELYR, PB, PS
            FROM LC_DIndicesForValuation
            JOIN SecuMain ON LC_DIndicesForValuation.InnerCode = SecuMain.InnerCode
            WHERE SecuMain.SecuCode IN {codes_str}
            AND SecuMain.SecuCategory = 1 AND SecuMain.SecuMarket IN (18, 83, 90)
            AND TradingDay >= '{start_date}'
            ORDER BY SecuMain.SecuCode, TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)

        results = []
        for code in codes:
            stock_df = df[df["SecuCode"] == code].copy()
            if stock_df.empty:
                continue

            latest = stock_df.iloc[0]
            row = {
                "股票代码": code,
                "股票简称": latest["SecuAbbr"],
                "最新日期": latest["TradingDay"].strftime("%Y-%m-%d"),
            }

            for col, name in [("PELYR", "PE"), ("PB", "PB"), ("PS", "PS")]:
                values = pd.to_numeric(stock_df[col], errors='coerce').dropna()
                if not values.empty:
                    latest_val = float(latest[col]) if pd.notna(latest[col]) else np.nan
                    percentile = (values <= latest_val).sum() / len(values) * 100 if not np.isnan(latest_val) else np.nan
                    row[f"当前{name}"] = round(latest_val, 2)
                    row[f"{name}分位(%)"] = round(percentile, 1)
                    row[f"{name}最低"] = round(values.min(), 2)
                    row[f"{name}最高"] = round(values.max(), 2)
                else:
                    row[f"当前{name}"] = "-"
                    row[f"{name}分位(%)"] = "-"

            results.append(row)

        return pd.DataFrame(results)

    def get_dividend_history(self, codes: List[str], years: int = 10) -> pd.DataFrame:
        """获取分红历史"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                dv.EndDate as 分红年度,
                dv.ExDiviDate as 除权除息日,
                YEAR(dv.EndDate) as 年度,
                dv.CashDiviRMB/10 as 每股股利_税前,
                dv.ActualCashDiviRMB/10 as 每股股利_税后,
                dv.TotalCashDiviComRMB/1e8 as 分红总额_亿元,
                dv.BonusShareRatio as 送股比例_10送X,
                dv.TranAddShareRaio as 转增比例_10转X,
                dv.EventProcedureDesc as 事件进程
            FROM SecuMain sm
            JOIN dz_dividend dv ON sm.InnerCode = dv.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1 AND sm.SecuMarket IN (18, 83, 90)
            AND YEAR(dv.EndDate) >= {start_year}
            AND dv.IfDividend = 1
            AND dv.CashDiviRMB > 0
            ORDER BY sm.SecuCode, dv.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_dividend_stats(self, codes: List[str], years: int = 10) -> pd.DataFrame:
        """获取分红统计"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                COUNT(DISTINCT YEAR(dv.EndDate)) as 分红年数,
                COUNT(*) as 分红次数,
                SUM(dv.CashDiviRMB/10) as 累计每股股利,
                AVG(dv.CashDiviRMB/10) as 平均每股股利,
                MAX(dv.CashDiviRMB/10) as 最高每股股利,
                MIN(dv.CashDiviRMB/10) as 最低每股股利
            FROM SecuMain sm
            JOIN dz_dividend dv ON sm.InnerCode = dv.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1 AND sm.SecuMarket IN (18, 83, 90)
            AND YEAR(dv.EndDate) >= {start_year}
            AND dv.IfDividend = 1
            AND dv.CashDiviRMB > 0
            GROUP BY sm.SecuCode, sm.ChiNameAbbr
        """
        df = pd.read_sql(sql, self.conn)
        return df

# ============ 港股估值查询 ============
class HKShareValuationQuery:
    """港股估值数据查询"""

    COLUMN_MAPPING = {
        "TradingDay": "交易日期", "ClosePrice": "收盘价",
        "HKStkMV": "市值(亿港币)", "PERatio": "PE", "PETTM": "PE(TTM)",
        "PB": "PB", "PS": "PS", "DividendRatioRW": "股息率(%)",
        "SecuCode": "股票代码", "ChiName": "股票简称"
    }

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_latest_valuation(self, codes: List[str]) -> pd.DataFrame:
        """获取最新估值数据"""
        codes_str = format_codes(codes)

        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName,
                   TradingDay, ClosePrice, HKStkMV, PERatio, PETTM, PB, PS, DividendRatioRW
            FROM QT_HKDailyQuoteIndex
            JOIN HK_SecuMain ON QT_HKDailyQuoteIndex.InnerCode = HK_SecuMain.InnerCode
            WHERE SecuCode IN {codes_str}
            AND TradingDay = (SELECT MAX(TradingDay) FROM QT_HKDailyQuoteIndex)
            ORDER BY HKStkMV DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)
        df["市值(亿港币)"] = pd.to_numeric(df["市值(亿港币)"], errors='coerce') / 1e8
        return df

    def get_history_valuation(self, codes: List[str], months: int = 12) -> pd.DataFrame:
        """获取历史估值数据"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=months * 31)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName,
                   TradingDay, ClosePrice, HKStkMV, PERatio, PB, PS, DividendRatioRW
            FROM QT_HKDailyQuoteIndex
            JOIN HK_SecuMain ON QT_HKDailyQuoteIndex.InnerCode = HK_SecuMain.InnerCode
            WHERE SecuCode IN {codes_str}
            AND TradingDay >= '{start_date}'
            ORDER BY SecuCode, TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)
        df["市值(亿港币)"] = pd.to_numeric(df["市值(亿港币)"], errors='coerce') / 1e8
        return df

    def get_percentile(self, codes: List[str], months: int = 12) -> pd.DataFrame:
        """计算估值分位数"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=months * 31)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName,
                   TradingDay, PERatio, PB, PS
            FROM QT_HKDailyQuoteIndex
            JOIN HK_SecuMain ON QT_HKDailyQuoteIndex.InnerCode = HK_SecuMain.InnerCode
            WHERE SecuCode IN {codes_str}
            AND TradingDay >= '{start_date}'
            ORDER BY SecuCode, TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)

        results = []
        for code in codes:
            stock_df = df[df["SecuCode"] == code].copy()
            if stock_df.empty:
                continue

            latest = stock_df.iloc[0]
            row = {
                "股票代码": code,
                "股票简称": latest["ChiName"],
                "最新日期": latest["TradingDay"].strftime("%Y-%m-%d"),
            }

            for col, name in [("PERatio", "PE"), ("PB", "PB"), ("PS", "PS")]:
                values = pd.to_numeric(stock_df[col], errors='coerce').dropna()
                if not values.empty:
                    latest_val = float(latest[col]) if pd.notna(latest[col]) else np.nan
                    percentile = (values <= latest_val).sum() / len(values) * 100 if not np.isnan(latest_val) else np.nan
                    row[f"当前{name}"] = round(latest_val, 2)
                    row[f"{name}分位(%)"] = round(percentile, 1)
                    row[f"{name}最低"] = round(values.min(), 2)
                    row[f"{name}最高"] = round(values.max(), 2)
                else:
                    row[f"当前{name}"] = "-"
                    row[f"{name}分位(%)"] = "-"

            results.append(row)

        return pd.DataFrame(results)

    def get_dividend_history(self, codes: List[str], years: int = 10) -> pd.DataFrame:
        """获取分红历史"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                dv.ExDate as 除权除息日,
                YEAR(dv.ExDate) as 年度,
                dv.CashDividendPS as 每股股利,
                dv.DividendPeriod as 股息期间
            FROM HK_SecuMain sm
            JOIN hk_dividend dv ON sm.InnerCode = dv.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuMarket = 72
            AND dv.ExDate IS NOT NULL
            AND YEAR(dv.ExDate) >= {start_year}
            AND dv.IfDividend = 1
            AND dv.CashDividendPS > 0
            ORDER BY sm.SecuCode, dv.ExDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_dividend_stats(self, codes: List[str], years: int = 10) -> pd.DataFrame:
        """获取分红统计"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                COUNT(DISTINCT YEAR(dv.ExDate)) as 分红年数,
                COUNT(*) as 分红次数,
                SUM(dv.CashDividendPS) as 累计每股股利,
                AVG(dv.CashDividendPS) as 平均每股股利,
                MAX(dv.CashDividendPS) as 最高每股股利,
                MIN(dv.CashDividendPS) as 最低每股股利
            FROM HK_SecuMain sm
            JOIN hk_dividend dv ON sm.InnerCode = dv.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuMarket = 72
            AND dv.ExDate IS NOT NULL
            AND YEAR(dv.ExDate) >= {start_year}
            AND dv.IfDividend = 1
            AND dv.CashDividendPS > 0
            GROUP BY sm.SecuCode, sm.ChiName
        """
        df = pd.read_sql(sql, self.conn)
        return df

# ============ 输出格式化 ============
def print_dataframe(df: pd.DataFrame, title: str = None, max_rows: int = 8):
    """打印Markdown格式表格"""
    if title:
        print(f"\n### {title}\n")
    if df.empty:
        print("*无数据*")
        return

    # 限制行数
    total = len(df)
    if total > max_rows:
        df_show = df.head(max_rows)
    else:
        df_show = df

    # 选择关键列（简化输出）
    key_cols_map = {
        '最新估值': ['股票简称', '总市值(亿)', 'PE(TTM)', 'PB(MRQ)', '股息率(%)'],
        '历史估值': ['交易日期', 'PE(TTM)', 'PB(MRQ)', '股息率(%)'],
        '分红历史': ['股票简称', '除权除息日', '年度', '每股股利_税前'],
        '分红统计': ['股票简称', '分红年数', '平均每股股利'],
    }

    # 查找匹配的列
    cols = [c for c in df_show.columns if c in ['股票代码', '股票简称', '交易日期', '除权除息日', '年度']]
    cols += [c for c in df_show.columns if any(k in c for k in ['市值', 'PE', 'PB', 'PS', '股息率', '每股', '分红'])]

    if not cols:
        cols = list(df_show.columns)

    df_display = df_show[cols].copy()

    # 格式化日期列
    for col in ['交易日期', '除权除息日']:
        if col in df_display.columns:
            df_display[col] = df_display[col].apply(
                lambda x: x.strftime('%m-%d') if hasattr(x, 'strftime') else str(x)
            )

    # 表头
    print("| " + " | ".join(str(c) for c in df_display.columns) + " |")
    print("|" + "|".join(["---"] * len(df_display.columns)) + "|")

    # 数据行
    for _, row in df_display.iterrows():
        values = []
        for col in df_display.columns:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif isinstance(val, float):
                # 智能精度
                col_lower = col.lower()
                if '率' in col or '%' in col or '息' in col:
                    values.append(f"{val:.2f}%")
                elif '市值' in col or '亿' in col:
                    values.append(f"{val:.0f}")
                elif 'pe' in col_lower:
                    values.append(f"{val:.1f}")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    # 行数提示
    if total > max_rows:
        print(f"\n*共 {total} 条，显示前 {max_rows} 条*")

def print_dividend_history(df: pd.DataFrame):
    """打印分红历史"""
    if df.empty:
        print("无分红记录")
        return
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.float_format', lambda x: f'{x:.4f}' if pd.notna(x) else '-')

    if '除权除息日' in df.columns:
        df['除权除息日'] = df['除权除息日'].apply(
            lambda x: x.strftime('%Y-%m-%d') if hasattr(x, 'strftime') else str(x)
        )

    cols = ['股票简称', '分红年度', '除权除息日', '年度', '每股股利_税前', '每股股利_税后',
            '分红总额_亿元', '送股比例_10送X', '转增比例_10转X']
    cols = [c for c in cols if c in df.columns]
    print(df[cols].to_string(index=False))

# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票估值数据综合查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 最新估值
  %(prog)s 600519                        # 查询茅台估值
  %(prog)s 600519,000858                 # 多股对比

  # 历史估值
  %(prog)s 600519 --history              # 历史估值
  %(prog)s 600519 --history -m 24        # 24个月历史

  # 估值分位数
  %(prog)s 600519 --percentile           # 估值分位数
  %(prog)s 600519 --percentile -m 24     # 24个月分位数

  # 分红历史
  %(prog)s 600519 --dividend             # 分红历史
  %(prog)s 600519 --dividend --stats     # 分红统计

  # 港股
  %(prog)s 00700                         # 港股腾讯
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--history", action="store_true", help="显示历史估值")
    parser.add_argument("--percentile", action="store_true", help="计算估值分位数")
    parser.add_argument("--dividend", action="store_true", help="查询分红历史")
    parser.add_argument("--stats", action="store_true", help="分红统计（配合--dividend）")
    parser.add_argument("-m", "--months", type=int, default=12, help="历史数据月数，默认12")
    parser.add_argument("-y", "--years", type=int, default=10, help="分红查询年数，默认10")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--output", "-o", help="输出到Excel文件")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        is_hk = all(is_hk_stock(c) for c in codes)

        if is_hk:
            query = HKShareValuationQuery(conn)
            print(f"查询港股估值: {codes}")
        else:
            query = AShareValuationQuery(conn)
            print(f"查询A股估值: {codes}")

        results = {}

        # 分红查询
        if args.dividend:
            if args.stats:
                df = query.get_dividend_stats(codes, args.years)
                print_dataframe(df, f"分红统计（近{args.years}年）")
                results["分红统计"] = df
            else:
                df = query.get_dividend_history(codes, args.years)
                print_dataframe(df, f"分红历史（近{args.years}年）")
                results["分红历史"] = df

        # 估值查询
        elif args.history:
            df = query.get_history_valuation(codes, args.months)
            print_dataframe(df, f"历史估值（近{args.months}个月）")
            results["历史估值"] = df

        elif args.percentile:
            df = query.get_percentile(codes, args.months)
            print_dataframe(df, f"估值分位数（近{args.months}个月）")
            results["估值分位数"] = df

        else:
            # 默认显示最新估值
            df = query.get_latest_valuation(codes)
            print_dataframe(df, "最新估值")
            results["最新估值"] = df

        # 导出
        if args.output:
            with pd.ExcelWriter(args.output, engine='openpyxl') as writer:
                for sheet_name, df in results.items():
                    if not df.empty:
                        df.to_excel(writer, sheet_name=sheet_name[:31], index=False)
            print(f"\n数据已导出到: {args.output}")

    finally:
        conn.close()

if __name__ == "__main__":
    main()
