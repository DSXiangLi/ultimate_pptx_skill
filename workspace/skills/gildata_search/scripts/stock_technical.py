#!/usr/bin/env python3
"""
股票技术指标查询
用法:
    python stock_technical.py 600519               # 默认行情+涨跌幅+换手率
    python stock_technical.py 600519 --ma           # 均线数据(MA5/10/20/60)
    python stock_technical.py 600519 --volume    # 成交量数据
    python stock_technical.py 600519 --turnover   # 换手率详细
    python stock_technical.py 600519 --range      # 振幅区间
    python stock_technical.py 600519 --suspend    # 停牌信息
    python stock_technical.py 600519 --all         # 全部数据
    python stock_technical.py 00700               # 港股

功能:
  1. 行情表现(日/周/月/季/年/近1年)
  2. MA均线(MA5/10/20/60)
  3. 成交量(日/周/月/季/年)
  4. 换手率(日/周/月/季/年)
  5. 振幅区间
  6. 停牌信息
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
import sys
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


# ============ A股技术指标查询 ============
class AShareTechnicalQuery:
    """A股技术指标查询"""

    # 行情数据列
    QUOTE_COLUMNS = [
        "TradingDay", "IfSuspend",
        "PrevClosePrice", "OpenPrice", "HighPrice", "LowPrice", "ClosePrice",
        "ChangePCT", "RangePCT",  # 日涨跌幅、振幅
        "TurnoverVolume", "TurnoverValue", "TurnoverRate",  # 成交量、成交额、换手率
    ]

    # MA均线列
    MA_COLUMNS = [
        "TradingDay",
        "AvgPriceRW", "AvgPriceRM", "AvgPriceRMSix", "AvgPriceRY", "AvgPriceYTD",  # 均价
    ]

    COLUMN_MAPPING = {
        "TradingDay": "交易日期",
        "IfSuspend": "是否停牌",
        "PrevClosePrice": "昨收盘", "OpenPrice": "今开盘",
        "HighPrice": "最高价", "LowPrice": "最低价", "ClosePrice": "收盘价",
        "ChangePCT": "涨跌幅%", "RangePCT": "振幅%",
        "TurnoverVolume": "成交量(万股)", "TurnoverValue": "成交额(万元)",
        "TurnoverRate": "换手率%",
        "AvgPriceRW": "MA5", "AvgPriceRM": "MA10",
        "AvgPriceRMSix": "MA20", "AvgPriceRY": "MA60",
        "AvgPriceYTD": "MA120(年线)",
        "HighPriceRW": "周最高", "LowPriceRW": "周最低",
        "TurnoverRateRW": "周换手率%",
        "ChangePCTRW": "周涨跌幅%", "RangePCTRW": "周振幅%",
        "SecuCode": "股票代码", "SecuAbbr": "股票简称"
    }

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_quote(self, codes: List[str], days: int = 30) -> pd.DataFrame:
        """获取行情数据"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT sm.SecuCode, sm.ChiNameAbbr as SecuAbbr,
                   qt.TradingDay, qt.IfSuspend,
                   qt.PrevClosePrice, qt.OpenPrice, qt.HighPrice, qt.LowPrice, qt.ClosePrice,
                   qt.ChangePCT, qt.RangePCT,
                   qt.TurnoverVolume, qt.TurnoverValue/1e4 as TurnoverValue,
                   qt.TurnoverRate
            FROM SecuMain sm
            JOIN QT_StockPerformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND qt.TradingDay >= '{start_date}'
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)
        return df

    def get_ma_data(self, codes: List[str], days: int = 60) -> pd.DataFrame:
        """获取MA均线数据

        注: QT_StockPerformance表的均线字段:
        - AvgPriceRW: 周均价
        - AvgPriceRM: 月均价
        - AvgPriceRY: 十二个月均价
        - AvgPriceYTD: 今年以来均价
        """
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT sm.SecuCode, sm.ChiNameAbbr as SecuAbbr,
                   qt.TradingDay,
                   qt.AvgPriceRW as 周均价,
                   qt.AvgPriceRM as 月均价,
                   qt.AvgPriceRY as 年均价,
                   qt.AvgPriceYTD as 今年以来均价,
                   qt.ClosePrice
            FROM SecuMain sm
            JOIN QT_StockPerformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND qt.TradingDay >= '{start_date}'
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns={"SecuCode": "股票代码", "SecuAbbr": "股票简称", "TradingDay": "交易日期", "ClosePrice": "收盘价"})
        return df

    def get_volume_data(self, codes: List[str], period: str = "D") -> pd.DataFrame:
        """获取成交量数据

        period: D=日, W=周, M=月, Q=季, Y=年, YTD=近1年
        """
        codes_str = format_codes(codes)
        period_map = {
            "D": ("TurnoverVolume", "TurnoverValue"),
            "W": ("TurnoverVolumeRW", "TurnoverValueRW"),
            "M": ("TurnoverVolumeRM", "TurnoverValueRM"),
            "Q": ("TurnoverVolumeRMThree", "TurnoverValueRMThree"),
            "Y": ("TurnoverVolumeRY", "TurnoverValueRY"),
            "YTD": ("TurnoverVolumeYTD", "TurnoverValueYTD"),
        }
        vol_col, val_col = period_map.get(period.upper(), ("TurnoverVolume", "TurnoverValue"))

        turnover_col = "TurnoverRate" if period.upper() == "D" else f"TurnoverRate{period.upper()}"

        sql = f"""
            SELECT sm.SecuCode, sm.ChiNameAbbr as SecuAbbr,
                   qt.TradingDay,
                   qt.{vol_col} as 成交量_股,
                   qt.{val_col}/1e4 as 成交额_万元,
                   qt.{turnover_col} as 换手率,
                   qt.ClosePrice
            FROM SecuMain sm
            JOIN QT_StockPerformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns={"SecuCode": "股票代码", "SecuAbbr": "股票简称", "TradingDay": "交易日期", "ClosePrice": "收盘价"})
        return df

    def get_turnover_data(self, codes: List[str], period: str = "D") -> pd.DataFrame:
        """获取换手率数据"""
        codes_str = format_codes(codes)
        period_map = {
            "D": "TurnoverRate",
            "W": "TurnoverRateRW",
            "M": "TurnoverRateRM",
            "Q": "TurnoverRateRMThree",
            "Y": "TurnoverRateRY",
            "YTD": "TurnoverRateYTD",
        }
        rate_col = period_map.get(period.upper(), "TurnoverRate")

        sql = f"""
            SELECT sm.SecuCode, sm.ChiNameAbbr as SecuAbbr,
                   qt.TradingDay,
                   qt.{rate_col} as 换手率,
                   qt.TurnoverVolume as 成交量_股,
                   qt.TurnoverValue/1e4 as 成交额_万元,
                   qt.ClosePrice
            FROM SecuMain sm
            JOIN QT_StockPerformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns={"SecuCode": "股票代码", "SecuAbbr": "股票简称", "TradingDay": "交易日期", "ClosePrice": "收盘价"})
        return df

    def get_range_data(self, codes: List[str], period: str = "D") -> pd.DataFrame:
        """获取振幅区间数据"""
        codes_str = format_codes(codes)
        period_map = {
            "D": ("HighPrice", "LowPrice", "RangePCT"),
            "W": ("HighPriceRW", "LowPriceRW", "RangePCTRW"),
            "M": ("HighPriceRM", "LowPriceRM", "RangePCTRM"),
            "Q": ("HighPriceRMThree", "LowPriceRMThree", "RangePCTRMThree"),
            "Y": ("HighPriceRY", "LowPriceRY", "RangePCTRY"),
            "YTD": ("HighPriceYTD", "LowPriceYTD", "RangePCTYTD"),
        }
        high_col, low_col, range_col = period_map.get(period.upper(),
            ("HighPrice", "LowPrice", "RangePCT"))

        sql = f"""
            SELECT sm.SecuCode, sm.ChiNameAbbr as SecuAbbr,
                   qt.TradingDay,
                   qt.{high_col} as 最高价,
                   qt.{low_col} as 最低价,
                   qt.{range_col} as 振幅,
                   qt.ClosePrice
            FROM SecuMain sm
            JOIN QT_StockPerformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns={"SecuCode": "股票代码", "SecuAbbr": "股票简称", "TradingDay": "交易日期", "ClosePrice": "收盘价"})
        return df

    def get_suspend_info(self, codes: List[str], days: int = 365) -> pd.DataFrame:
        """获取停牌信息"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        sql = f"""
            SELECT sm.SecuCode as 股票代码,
                   sm.ChiNameAbbr as 股票简称,
                   qt.TradingDay as 交易日期,
                   qt.IfSuspend as 是否停牌,
                   qt.PrevClosePrice as 昨收盘,
                   qt.ClosePrice as 收盘价
            FROM SecuMain sm
            JOIN QT_StockPerformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND qt.TradingDay >= '{start_date}'
            AND qt.IfSuspend = 1
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df


# ============ 港股技术指标查询 ============
class HKShareTechnicalQuery:
    """港股技术指标查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_quote(self, codes: List[str], days: int = 30) -> pd.DataFrame:
        """获取港股行情数据"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")

        # 港股使用CS_HKStockPerformance表
        sql = f"""
            SELECT sm.SecuCode, sm.ChiName as SecuAbbr,
                   qt.TradingDay,
                   qt.PrevClosePrice,
                   qt.OpenPrice,
                   qt.HighPrice,
                   qt.LowPrice,
                   qt.ClosePrice,
                   qt.ChangePCT as 涨跌幅,
                   qt.RangePCT as 振幅,
                   qt.TurnoverVolume/1e4 as 成交量_万股,
                   qt.TurnoverValue/1e4 as 成交额_万港币,
                   qt.TurnoverRate as 换手率
            FROM HK_SecuMain sm
            JOIN cs_hkstockperformance qt ON sm.InnerCode = qt.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuMarket = 72
            AND qt.TradingDay >= '{start_date}'
            ORDER BY sm.SecuCode, qt.TradingDay DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns={
            "SecuCode": "股票代码", "SecuAbbr": "股票简称",
            "TradingDay": "交易日期", "PrevClosePrice": "昨收盘",
            "OpenPrice": "今开盘", "HighPrice": "最高价", "LowPrice": "最低价",
            "ClosePrice": "收盘价"
        })
        return df


# ============ 输出格式化 ============
def print_dataframe(df: pd.DataFrame, title: str = None, max_rows: int = 10):
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

    # 表头
    print("| " + " | ".join(str(c) for c in df_show.columns) + " |")
    print("|" + "|".join(["---"] * len(df_show.columns)) + "|")

    # 数据行
    for _, row in df_show.iterrows():
        values = []
        for col in df_show.columns:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif hasattr(val, 'strftime'):
                values.append(val.strftime('%m-%d'))
            elif isinstance(val, float):
                col_lower = col.lower()
                if '幅' in col or '率' in col or '%' in col:
                    values.append(f"{val:.2f}%")
                elif '量' in col or '额' in col:
                    values.append(f"{val:,.0f}")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共 {total} 条，显示前 {max_rows} 条*")


def print_ma_analysis(df: pd.DataFrame):
    """打印MA均线分析"""
    if df.empty:
        print("无MA均线数据")
        return

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.float_format', lambda x: f'{x:.2f}' if pd.notna(x) else '-')

    # 计算均线趋势
    for code in df['股票代码'].unique():
        stock_df = df[df['股票代码'] == code].copy()
        if len(stock_df) < 2:
            continue

        latest = stock_df.iloc[0]
        prev = stock_df.iloc[1] if len(stock_df) > 1 else None

        print(f"\n{latest['股票简称']} ({code}) MA分析:")
        print(f"  收盘价: {latest['收盘价']:.2f}")
        print(f"  MA5: {latest['MA5']:.2f}" if pd.notna(latest['MA5']) else "  MA5: -")
        print(f"  MA10: {latest['MA10']:.2f}" if pd.notna(latest['MA10']) else "  MA10: -")
        print(f"  MA20: {latest['MA20']:.2f}" if pd.notna(latest['MA20']) else "  MA20: -")
        print(f"  MA60: {latest['MA60']:.2f}" if pd.notna(latest['MA60']) else "  MA60: -")

        # 判断趋势
        close = latest['收盘价']
        ma5 = latest['MA5']
        ma10 = latest['MA10']
        ma20 = latest['MA20']

        if pd.notna(ma5) and pd.notna(ma10) and pd.notna(ma20):
            if close > ma5 > ma10 > ma20:
                print("  趋势: 多头排列(短>中>长)")
            elif close < ma5 < ma10 < ma20:
                print("  趋势: 空头排列(短<中<长)")
            else:
                print("  趋势: 均线纠缠")


# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票技术指标查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 行情数据
  %(prog)s 600519                    # 默认30日行情
  %(prog)s 600519 --days 60          # 60日行情

  # MA均线
  %(prog)s 600519 --ma              # MA均线数据
  %(prog)s 600519 --ma --analysis    # MA均线分析

  # 成交量
  %(prog)s 600519 --volume           # 日成交量
  %(prog)s 600519 --volume -p W      # 周成交量
  %(prog)s 600519 --volume -p M      # 月成交量

  # 换手率
  %(prog)s 600519 --turnover         # 日换手率
  %(prog)s 600519 --turnover -p W    # 周换手率

  # 振幅区间
  %(prog)s 600519 --range            # 日振幅
  %(prog)s 600519 --range -p W       # 周振幅

  # 停牌信息
  %(prog)s 600519 --suspend         # 停牌信息

  # 港股
  %(prog)s 00700                    # 港股腾讯
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--ma", action="store_true", help="显示MA均线数据")
    parser.add_argument("--analysis", action="store_true", help="MA均线分析")
    parser.add_argument("--volume", action="store_true", help="显示成交量数据")
    parser.add_argument("--turnover", action="store_true", help="显示换手率数据")
    parser.add_argument("--range", action="store_true", help="显示振幅区间")
    parser.add_argument("--amplitude", action="store_true", help="显示振幅区间(同--range)")
    parser.add_argument("--suspend", action="store_true", help="显示停牌信息")
    parser.add_argument("-d", "--days", type=int, default=30, help="查询天数，默认30")
    parser.add_argument("-p", "--period", choices=["D", "W", "M", "Q", "Y", "YTD"],
                        default="D", help="时间周期: D=日, W=周, M=月, Q=季, Y=年, YTD=近1年")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--output", "-o", help="输出到Excel文件")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        is_hk = all(is_hk_stock(c) for c in codes)

        if is_hk:
            query = HKShareTechnicalQuery(conn)
            print(f"查询港股技术指标: {codes}")
        else:
            query = AShareTechnicalQuery(conn)
            print(f"查询A股技术指标: {codes}")

        results = {}

        # MA均线
        if args.ma:
            df = query.get_ma_data(codes, args.days)
            print_dataframe(df, f"MA均线数据(近{args.days}日)")
            results["MA均线"] = df

            if args.analysis and not is_hk:
                print_ma_analysis(df)

        # 成交量
        elif args.volume:
            df = query.get_volume_data(codes, args.period)
            period_name = {"D": "日", "W": "周", "M": "月", "Q": "季", "Y": "年", "YTD": "近1年"}
            print_dataframe(df, f"成交量数据({period_name.get(args.period, '日')})")
            results["成交量"] = df

        # 换手率
        elif args.turnover:
            df = query.get_turnover_data(codes, args.period)
            period_name = {"D": "日", "W": "周", "M": "月", "Q": "季", "Y": "年", "YTD": "近1年"}
            print_dataframe(df, f"换手率数据({period_name.get(args.period, '日')})")
            results["换手率"] = df

        # 振幅区间
        elif args.range or args.amplitude:
            df = query.get_range_data(codes, args.period)
            period_name = {"D": "日", "W": "周", "M": "月", "Q": "季", "Y": "年", "YTD": "近1年"}
            print_dataframe(df, f"振幅区间({period_name.get(args.period, '日')})")
            results["振幅区间"] = df

        # 停牌信息
        elif args.suspend:
            df = query.get_suspend_info(codes, args.days)
            print_dataframe(df, f"停牌信息(近{args.days}日)")
            results["停牌信息"] = df

        # 默认显示行情数据
        else:
            df = query.get_quote(codes, args.days)
            print_dataframe(df, f"行情数据(近{args.days}日)")
            results["行情数据"] = df

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
