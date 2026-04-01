#!/usr/bin/env python3
"""
业绩预告/快报查询
用法:
    python stock_earnings_forecast.py 600519               # 蟥询茅台业绩预告
    python stock_earnings_forecast.py 600519 --type forecast  # 业绩预告
    python stock_earnings_forecast.py 600519 --type express    # 业绩快报
    python stock_earnings_forecast.py 00700                # 港股

功能:
  1. 查询业绩预告数据
  2. 查询业绩快报数据
  3. 韥询历史业绩预告准确率
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

from datetime import datetime
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

# ============ A股业绩预告 ============
class AShareEarningsForecast:
    """A股业绩预告/快报查询"""

    # 业绩预告类型映射
    FORECAST_TYPE_MAP = {
        1: "预亏", 2: "不确定", 3: "预盈", 4: "预增",
        5: "预平", 6: "经营计划", 7: "减亏", 8: "续亏"
    }

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_forecast(self, codes: List[str]) -> pd.DataFrame:
        """获取业绩预告"""
        codes_str = format_codes(codes)

        # 使用 dz_performanceforecast 表
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                fc.InfoPublDate as 发布日期,
                fc.EndDate as 报告期,
                fc.ForcastType as 预告类型,
                fc.ResultStatement as 预告说明,
                fc.EProfitFloor/1e8 as 预告净利润下限_亿元,
                fc.EProfitCeiling/1e8 as 预告净利润上限_亿元,
                fc.LastProfit/1e8 as 上年同期净利润_亿元,
                fc.EGrowthRateFloor as 预计增幅下限,
                fc.EGrowthRateCeiling as 预计增幅上限
            FROM SecuMain sm
            JOIN dz_performanceforecast fc ON sm.CompanyCode = fc.CompanyCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND fc.ForcastType IN (1, 3, 4, 5, 7, 8)
            ORDER BY sm.SecuCode, fc.InfoPublDate DESC
        """
        df = pd.read_sql(sql, self.conn)

        # 映射预告类型
        df['预告类型'] = df['预告类型'].apply(
            lambda x: self.FORECAST_TYPE_MAP.get(x, f"未知({x})") if pd.notna(x) else "未知"
        )

        return df

    def get_express(self, codes: List[str]) -> pd.DataFrame:
        """获取业绩快报 - 暂不支持"""
        return pd.DataFrame({"提示": ["业绩快报功能暂不支持，请使用业绩预告功能"]})

    def get_forecast_accuracy(self, code: str, years: int = 3) -> pd.DataFrame:
        """获取历史业绩预告准确率"""
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                YEAR(fc.EndDate) as 年度,
                fc.ForcastType as 预告类型,
                fc.EProfitFloor/1e8 as 预告下限_亿元,
                fc.EProfitCeiling/1e8 as 预告上限_亿元,
                inc.NPParentCompanyOwners/1e8 as 实际净利润_亿元,
                CASE
                    WHEN inc.NPParentCompanyOwners BETWEEN fc.EProfitFloor AND fc.EProfitCeiling
                    THEN '准确'
                    WHEN inc.NPParentCompanyOwners IS NULL OR fc.EProfitFloor IS NULL
                    THEN '无法判断'
                    ELSE '偏差'
                END as 预告准确性
            FROM SecuMain sm
            JOIN dz_performanceforecast fc ON sm.CompanyCode = fc.CompanyCode
            JOIN LC_IncomeStatementAll inc ON sm.CompanyCode = inc.CompanyCode
                AND YEAR(inc.EndDate) = YEAR(fc.EndDate)
                AND inc.IfMerged = 1
            WHERE sm.SecuCode = '{code}'
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND YEAR(fc.EndDate) >= {start_year}
            ORDER BY fc.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)

        if not df.empty:
            # 映射预告类型
            df['预告类型'] = df['预告类型'].apply(
                lambda x: self.FORECAST_TYPE_MAP.get(x, f"未知({x})") if pd.notna(x) else "未知"
            )

        return df

# ============ 港股业绩预告 ============
class HKShareEarningsForecast:
    """港股业绩预告/快报查询"""

    # 业绩预告类型映射
    FORECAST_TYPE_MAP = {
        1: "预亏", 2: "不确定", 3: "预盈", 4: "预增",
        5: "预平", 6: "经营计划", 7: "减亏"
    }

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_forecast(self, codes: List[str]) -> pd.DataFrame:
        """获取业绩预告 - 港股暂不支持"""
        return pd.DataFrame({"提示": ["港股业绩预告功能暂不支持，请使用A股查询"]})

    def get_express(self, codes: List[str]) -> pd.DataFrame:
        """获取业绩快报 - 暂不支持"""
        return pd.DataFrame({"提示": ["港股业绩快报功能暂不支持"]})

# ============ 输出格式化 ============
def print_forecast(df: pd.DataFrame):
    """打印业绩预告"""
    if df.empty:
        print("无业绩预告数据")
        return

    if '提示' in df.columns:
        print(df['提示'].iloc[0])
        return

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.float_format', lambda x: f'{x:,.2f}' if pd.notna(x) else '-')

    # 选择显示列
    display_cols = ['股票简称', '报告期', '预告类型', '预告说明', '预告净利润下限_亿元', '预告净利润上限_亿元', '上年同期净利润_亿元', '发布日期']
    display_cols = [c for c in display_cols if c in df.columns]

    display_df = df[display_cols].copy()

    # 格式化日期
    for col in ['发布日期', '报告期']:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(
                lambda x: x.strftime('%Y-%m-%d') if hasattr(x, 'strftime') else str(x)
            )

    print(display_df.to_string(index=False))

def print_express(df: pd.DataFrame):
    """打印业绩快报"""
    if df.empty:
        print("无业绩快报数据")
        return

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.float_format', lambda x: f'{x:,.2f}' if pd.notna(x) else '-')

    # 选择显示列
    display_cols = ['股票简称', '报告类型', '净利润', '净利润增速', '营业收入', '营业收入增速', '每股收益', '报告期']
    display_cols = [c for c in display_cols if c in df.columns]

    display_df = df[display_cols].copy()

    # 格式化日期
    if '报告期' in display_df.columns:
        display_df['报告期'] = display_df['报告期'].apply(
            lambda x: x.strftime('%Y-%m-%d') if hasattr(x, 'strftime') else str(x)
        )

    print(display_df.to_string(index=False))

def print_accuracy(df: pd.DataFrame):
    """打印预告准确率"""
    if df.empty:
        print("无预告准确率数据")
        return

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    # 讱算准确率统计
    if '预告准确性' in df.columns:
        accuracy_stats = df['预告准确性'].value_counts()
        print("\n预告准确率统计:")
        for acc, count in accuracy_stats.items():
            print(f"  {acc}: {count}次")

    # 显示详细数据
    display_cols = ['股票简称', '年度', '预告类型', '预告方向', '预告下限', '预告上限', '实际净利润', '预告准确性']
    display_cols = [c for c in display_cols if c in df.columns]

    display_df = df[display_cols].copy()
    print("\n预告详细数据:")
    print(display_df.to_string(index=False))

# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="业绩预告/快报查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 600519                    # 查询茅台业绩预告
  %(prog)s 600519 --type forecast   # 只看业绩预告
  %(prog)s 600519 --type express    # 只看业绩快报
  %(prog)s 600519 --accuracy        # 查询预告准确率
  %(prog)s 600519,000858            # 多股查询
  %(prog)s 00700                     # 港股
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--type", "-t", choices=["forecast", "express"], default=None,
                        help="查询类型: forecast(业绩预告), express(业绩快报)")
    parser.add_argument("--accuracy", "-a", action="store_true", help="查询预告准确率")
    parser.add_argument("--config", help="配置文件路径")
    parser.add_argument("--output", "-o", help="输出到Excel文件")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        is_hk = all(is_hk_stock(c) for c in codes)

        if is_hk:
            query = HKShareEarningsForecast(conn)
            print(f"查询港股业绩数据: {codes}")
        else:
            query = AShareEarningsForecast(conn)
            print(f"查询A股业绩数据: {codes}")

        results = {}

        # 根据参数决定查询类型
        if args.accuracy and not is_hk:
            # 查询预告准确率（仅A股）
            for code in codes:
                df = query.get_forecast_accuracy(code, years=3)
                if not df.empty:
                    print(f"\n{'='*20} {code} 预告准确率 {'='*20}")
                    print_accuracy(df)
                    results[f"{code}_预告准确率"] = df
        elif args.type == "forecast" or args.type is None:
            # 查询业绩预告
            df = query.get_forecast(codes)
            print(f"\n{'='*20} 业绩预告 {'='*20}")
            print_forecast(df)
            results["业绩预告"] = df
        elif args.type == "express":
            # 查询业绩快报
            df = query.get_express(codes)
            print(f"\n{'='*20} 业绩快报 {'='*20}")
            print_express(df)
            results["业绩快报"] = df

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
