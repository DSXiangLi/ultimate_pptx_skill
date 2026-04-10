#!/usr/bin/env python3
"""
股票同行业对比分析（含行业平均对比）
用法:
    # 同行业对比
    python stock_peer_analysis.py 600519               # 茅台同行业对比
    python stock_peer_analysis.py 600519 --top 5        # 只看前5名
    python stock_peer_analysis.py 600519 --trend      # 财务趋势

    # 行业平均对比
    python stock_peer_analysis.py 600519 --avg           # 与行业平均对比
    python stock_peer_analysis.py 600519 --rank         # 行业ROE排名

    # 港股
    python stock_peer_analysis.py 00700               # 港股腾讯

数据表:
  - LC_ExgIndustry (A股行业分类)
  - HK_ExgIndustry + CT_IndustryType (港股行业分类)
  - LC_DIndicesForValuation (A股估值)
  - LC_MainIndexNew (A股财务指标)
  - QT_HKDailyQuoteIndex (港股估值)
  - HK_Derivative (港股财务指标)
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
from typing import List, Optional, Dict, Tuple

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

# ============ A股同行业分析 ============
class ASharePeerAnalysis:
    """A股同行业对比分析"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_industry(self, code: str) -> Tuple[str, str, str]:
        """获取股票所属申万行业（一二三级）"""
        sql = f"""
            SELECT FirstIndustryName, SecondIndustryName, ThirdIndustryName
            FROM LC_ExgIndustry
            JOIN SecuMain ON LC_ExgIndustry.CompanyCode = SecuMain.CompanyCode
            WHERE SecuCode = '{code}' AND Standard = 38 AND IfPerformed = 1
            LIMIT 1
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return None, None, None
        return df.iloc[0]["FirstIndustryName"], df.iloc[0]["SecondIndustryName"], df.iloc[0]["ThirdIndustryName"]

    def get_peer_companies(self, code: str, top_n: int = 5) -> List[str]:
        """获取同行业市值前N的公司"""
        first_ind, second_ind, third_ind = self.get_industry(code)
        if not third_ind:
            return [code]

        sql = f"""
            SELECT sm.SecuCode, sm.ChiNameAbbr, perf.TotalMV
            FROM LC_ExgIndustry exg
            JOIN SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            LEFT JOIN QT_StockPerformance perf ON sm.InnerCode = perf.InnerCode
            WHERE exg.ThirdIndustryName = '{third_ind}'
            AND exg.Standard = 38 AND exg.IfPerformed = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND sm.SecuCategory = 1
            AND sm.ListedSector = 1
            AND LENGTH(sm.SecuCode) = 6
            AND sm.SecuCode NOT LIKE 'X%%'
            AND sm.SecuCode REGEXP '^[0-9]+$'
            AND perf.TradingDay = (SELECT MAX(TradingDay) FROM QT_StockPerformance)
            ORDER BY perf.TotalMV DESC
            LIMIT {top_n}
        """
        df = pd.read_sql(sql, self.conn)
        codes = df["SecuCode"].tolist()
        if code not in codes:
            codes.append(code)
        return codes

    def get_peer_comparison(self, codes: List[str]) -> pd.DataFrame:
        """获取同行业公司对比数据"""
        codes_str = format_codes(codes)
        sql_date = "SELECT MAX(TradingDay) FROM QT_StockPerformance"
        latest_date = pd.read_sql(sql_date, self.conn).iloc[0, 0]
        latest_date_str = latest_date.strftime("%Y-%m-%d") if hasattr(latest_date, 'strftime') else str(latest_date)

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                val.TotalMV/1e8 as 总市值_亿元,
                val.PELYR as PE,
                val.PE as PE_TTM,
                val.PB as PB,
                val.PS as PS,
                val.DividendRatioLYR as 股息率_pct,
                idx.ROEAvg as ROE_pct,
                idx.GrossIncomeRatio as 毛利率_pct,
                idx.NetProfitRatio as 净利率_pct,
                idx.DebtAssetsRatio as 资产负债率_pct,
                idx.OperatingRevenueGrowRate as 营收增速_pct,
                idx.NetProfitGrowRate as 净利润增速_pct
            FROM SecuMain sm
            LEFT JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = '{latest_date_str}'
            LEFT JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
                AND idx.EndDate = (
                    SELECT MAX(EndDate) FROM LC_MainIndexNew
                    WHERE CompanyCode = sm.CompanyCode
                )
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            ORDER BY val.TotalMV DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_financial_trend(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        """获取财务趋势数据"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                YEAR(idx.EndDate) as 年份,
                idx.ROEAvg as ROE_pct,
                idx.GrossIncomeRatio as 毛利率_pct,
                idx.NetProfitRatio as 净利率_pct,
                idx.BasicEPS as EPS,
                idx.OperatingRevenueGrowRate as 营收增速_pct,
                idx.NetProfitGrowRate as 净利润增速_pct
            FROM SecuMain sm
            JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND YEAR(idx.EndDate) >= {start_year}
            AND idx.EndDate LIKE '%%-12-%%'
            ORDER BY sm.SecuCode, idx.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_industry_avg(self, third_industry: str) -> pd.DataFrame:
        """获取行业平均财务指标"""
        sql = f"""
            SELECT
                '{third_industry}' as 行业,
                COUNT(*) as 公司数,
                AVG(idx.ROEAvg) as 行业ROE,
                AVG(idx.NetProfitRatio) as 行业净利率,
                AVG(idx.GrossIncomeRatio) as 行业毛利率,
                AVG(idx.DebtAssetsRatio) as 行业资产负债率,
                AVG(val.PE) as 行业PE_TTM,
                AVG(val.PB) as 行业PB
            FROM LC_ExgIndustry exg
            JOIN SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
            LEFT JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM LC_DIndicesForValuation)
            WHERE exg.ThirdIndustryName = '{third_industry}'
            AND exg.Standard = 38 AND exg.IfPerformed = 1
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND idx.EndDate = (
                SELECT MAX(EndDate) FROM LC_MainIndexNew
                WHERE CompanyCode = sm.CompanyCode
            )
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_stock_metrics(self, code: str) -> pd.DataFrame:
        """获取个股财务指标"""
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                idx.ROEAvg as ROE,
                idx.NetProfitRatio as 净利率,
                idx.GrossIncomeRatio as 毛利率,
                idx.DebtAssetsRatio as 资产负债率,
                val.PE as PE_TTM,
                val.PB as PB
            FROM SecuMain sm
            JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
            LEFT JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM LC_DIndicesForValuation)
            WHERE sm.SecuCode = '{code}'
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND idx.EndDate = (
                SELECT MAX(EndDate) FROM LC_MainIndexNew
                WHERE CompanyCode = sm.CompanyCode
            )
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_industry_ranking(self, code: str, top_n: int = 20) -> pd.DataFrame:
        """获取行业内ROE排名"""
        third_ind = self.get_industry(code)[2]
        if not third_ind:
            return pd.DataFrame()

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                idx.ROEAvg as ROE,
                idx.NetProfitRatio as 净利率,
                val.TotalMV/1e8 as 总市值,
                val.PE as PE_TTM
            FROM LC_ExgIndustry exg
            JOIN SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
            LEFT JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM LC_DIndicesForValuation)
            WHERE exg.ThirdIndustryName = '{third_ind}'
            AND exg.Standard = 38 AND exg.IfPerformed = 1
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            AND idx.EndDate = (
                SELECT MAX(EndDate) FROM LC_MainIndexNew
                WHERE CompanyCode = sm.CompanyCode
            )
            ORDER BY idx.ROEAvg DESC
            LIMIT {top_n}
        """
        df = pd.read_sql(sql, self.conn)
        df['ROE排名'] = range(1, len(df) + 1)
        df['是否目标'] = df['股票代码'].apply(lambda x: '★' if x == code else '')
        return df

# ============ 港股同行业分析 ============
class HKSharePeerAnalysis:
    """港股同行业对比分析"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_industry(self, code: str) -> Tuple[str, str, str]:
        """获取股票所属申万行业"""
        sql = f"""
            SELECT ct.FirstIndustryName, ct.SecondIndustryName, ct.ThirdIndustryName
            FROM HK_ExgIndustry exg
            JOIN HK_SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            JOIN CT_IndustryType ct ON exg.IndustryNum = ct.IndustryNum AND ct.Standard = 38
            WHERE sm.SecuCode = '{code}' AND exg.Standard = 38 AND exg.IfExecuted = 1
            LIMIT 1
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return None, None, None
        return df.iloc[0]["FirstIndustryName"], df.iloc[0]["SecondIndustryName"], df.iloc[0]["ThirdIndustryName"]

    def get_peer_companies(self, code: str, top_n: int = 5) -> List[str]:
        """获取同行业市值前N的公司"""
        first_ind, second_ind, third_ind = self.get_industry(code)
        if not third_ind:
            return [code]

        sql = f"""
            SELECT sm.SecuCode, sm.ChiName, idx.HKStkMV
            FROM HK_ExgIndustry exg
            JOIN HK_SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            JOIN CT_IndustryType ct ON exg.IndustryNum = ct.IndustryNum AND ct.Standard = 38
            LEFT JOIN QT_HKDailyQuoteIndex idx ON sm.InnerCode = idx.InnerCode
            WHERE ct.ThirdIndustryName = '{third_ind}'
            AND exg.Standard = 38 AND exg.IfExecuted = 1
            AND sm.SecuMarket = 72
            AND sm.SecuCategory IN (3, 51, 53, 78)
            AND sm.ListedState <> 9
            AND LENGTH(sm.SecuCode) = 5
            AND idx.TradingDay = (SELECT MAX(TradingDay) FROM QT_HKDailyQuoteIndex)
            ORDER BY idx.HKStkMV DESC
            LIMIT {top_n}
        """
        df = pd.read_sql(sql, self.conn)
        codes = df["SecuCode"].tolist()
        if code not in codes:
            codes.append(code)
        return codes

    def get_peer_comparison(self, codes: List[str]) -> pd.DataFrame:
        """获取同行业公司对比数据"""
        codes_str = format_codes(codes)
        sql_date = "SELECT MAX(TradingDay) FROM QT_HKDailyQuoteIndex"
        latest_date = pd.read_sql(sql_date, self.conn).iloc[0, 0]
        latest_date_str = latest_date.strftime("%Y-%m-%d") if hasattr(latest_date, 'strftime') else str(latest_date)

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                val.HKStkMV/1e8 as 市值_亿港币,
                val.FPE as PE,
                val.PETTM as PE_TTM,
                val.PB as PB,
                val.PS as PS,
                val.DividendRatioRW as 股息率_pct,
                idx.ROE as ROE_pct,
                idx.GrossIncomeRatio as 毛利率_pct
            FROM HK_SecuMain sm
            LEFT JOIN QT_HKDailyQuoteIndex val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = '{latest_date_str}'
            LEFT JOIN HK_Derivative idx ON sm.CompanyCode = idx.CompanyCode
                AND idx.EndDate = (
                    SELECT MAX(EndDate) FROM HK_Derivative
                    WHERE CompanyCode = sm.CompanyCode
                )
            WHERE sm.SecuCode IN {codes_str}
            ORDER BY val.HKStkMV DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_industry_avg(self, third_industry: str) -> pd.DataFrame:
        """获取港股行业平均"""
        sql = f"""
            SELECT
                '{third_industry}' as 行业,
                COUNT(*) as 公司数,
                AVG(der.ROE) as 行业ROE,
                AVG(der.NetProfitRatio) as 行业净利率,
                AVG(der.GrossIncomeRatio) as 行业毛利率,
                AVG(val.PETTM) as 行业PE_TTM,
                AVG(val.PB) as 行业PB
            FROM HK_ExgIndustry exg
            JOIN HK_SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            JOIN CT_IndustryType ct ON exg.IndustryNum = ct.IndustryNum AND ct.Standard = 38
            LEFT JOIN HK_Derivative der ON sm.CompanyCode = der.CompanyCode
                AND der.EndDate = (SELECT MAX(EndDate) FROM HK_Derivative WHERE CompanyCode = sm.CompanyCode)
            LEFT JOIN QT_HKDailyQuoteIndex val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM QT_HKDailyQuoteIndex)
            WHERE ct.ThirdIndustryName = '{third_industry}'
            AND exg.Standard = 38 AND exg.IfExecuted = 1
            AND sm.SecuMarket = 72
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_stock_metrics(self, code: str) -> pd.DataFrame:
        """获取港股个股指标"""
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                der.ROE as ROE,
                der.NetProfitRatio as 净利率,
                der.GrossIncomeRatio as 毛利率,
                val.PETTM as PE_TTM,
                val.PB as PB
            FROM HK_SecuMain sm
            LEFT JOIN HK_Derivative der ON sm.CompanyCode = der.CompanyCode
                AND der.EndDate = (SELECT MAX(EndDate) FROM HK_Derivative WHERE CompanyCode = sm.CompanyCode)
            LEFT JOIN QT_HKDailyQuoteIndex val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM QT_HKDailyQuoteIndex)
            WHERE sm.SecuCode = '{code}'
            AND sm.SecuMarket = 72
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_industry_ranking(self, code: str, top_n: int = 20) -> pd.DataFrame:
        """获取港股行业ROE排名"""
        third_ind = self.get_industry(code)[2]
        if not third_ind:
            return pd.DataFrame()

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                der.ROE as ROE,
                val.HKStkMV/1e8 as 总市值_亿港币,
                val.PETTM as PE_TTM
            FROM HK_ExgIndustry exg
            JOIN HK_SecuMain sm ON exg.CompanyCode = sm.CompanyCode
            JOIN CT_IndustryType ct ON exg.IndustryNum = ct.IndustryNum AND ct.Standard = 38
            LEFT JOIN HK_Derivative der ON sm.CompanyCode = der.CompanyCode
                AND der.EndDate = (SELECT MAX(EndDate) FROM HK_Derivative WHERE CompanyCode = sm.CompanyCode)
            LEFT JOIN QT_HKDailyQuoteIndex val ON sm.InnerCode = val.InnerCode
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM QT_HKDailyQuoteIndex)
            WHERE ct.ThirdIndustryName = '{third_ind}'
            AND exg.Standard = 38 AND exg.IfExecuted = 1
            AND sm.SecuMarket = 72
            ORDER BY der.ROE DESC
            LIMIT {top_n}
        """
        df = pd.read_sql(sql, self.conn)
        df['ROE排名'] = range(1, len(df) + 1)
        df['是否目标'] = df['股票代码'].apply(lambda x: '★' if x == code else '')
        return df

# ============ 输出格式化 ============
def print_dataframe(df: pd.DataFrame, title: str = None, highlight_code: str = None):
    """打印DataFrame，高亮目标股票"""
    if title:
        print(f"\n{'='*20} {title} {'='*20}")
    if df.empty:
        print("无数据")
        return

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.float_format', lambda x: f'{x:,.2f}' if pd.notna(x) else '-')

    output = df.to_string(index=False)

    if highlight_code:
        lines = output.split('\n')
        for i, line in enumerate(lines):
                if highlight_code in line:
                    lines[i] = f">>> {line}  <<<"
        output = '\n'.join(lines)

    print(output)

def print_industry_info(first: str, second: str, third: str):
    """打印行业信息"""
    print(f"\n所属行业:")
    print(f"  一级: {first}")
    print(f"  二级: {second}")
    print(f"  三级: {third}")

def print_comparison(stock_df: pd.DataFrame, industry_df: pd.DataFrame):
    """打印个股vs行业平均对比"""
    if stock_df.empty or industry_df.empty:
        print("无数据")
        return

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    metrics = ['ROE', '净利率', '毛利率', 'PE_TTM', 'PB']
    metrics = [m for m in metrics if m in stock_df.columns and f'行业{m}' in industry_df.columns]

    rows = []
    for m in metrics:
        stock_val = stock_df.iloc[0].get(m, np.nan)
        industry_val = industry_df.iloc[0].get(f'行业{m}', np.nan)
        diff = stock_val - industry_val if pd.notna(stock_val) and pd.notna(industry_val) else np.nan

        rows.append({
            '指标': m,
            '个股': f'{stock_val:.2f}' if pd.notna(stock_val) else '-',
            '行业平均': f'{industry_val:.2f}' if pd.notna(industry_val) else '-',
            '差异': f'{diff:+.2f}' if pd.notna(diff) else '-',
            '评价': '优于行业' if diff > 0 else ('弱于行业' if diff < 0 else '-')
        })

    result_df = pd.DataFrame(rows)
    # 输出Markdown格式表格
    print("| " + " | ".join(result_df.columns) + " |")
    print("|" + "|".join(["---"] * len(result_df.columns)) + "|")
    for _, row in result_df.iterrows():
        print("| " + " | ".join(str(v) for v in row) + " |")

def print_ranking(df: pd.DataFrame, code: str):
    """打印排名 - Markdown表格格式"""
    if df.empty:
        print("无排名数据")
        return

    target_rank = df[df['股票代码'] == code]['ROE排名'].values
    if len(target_rank) > 0:
        total = len(df)
        print(f"\n目标股票 {code} 在行业内ROE排名第 {int(target_rank[0])}/{total}")

    cols = ['ROE排名', '股票代码', '股票简称', 'ROE', '净利率', '是否目标']
    cols = [c for c in cols if c in df.columns]
    df_show = df[cols].copy()

    # 输出Markdown表格
    print("\n| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")
    for _, row in df_show.iterrows():
        values = []
        for col in cols:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif isinstance(val, float):
                values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票同行业对比分析（含行业平均对比）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 同行业对比
  %(prog)s 600519                    # 茅台同行业对比
  %(prog)s 600519 --top 5            # 只看前5名
  %(prog)s 600519 --trend            # 显示财务趋势

  # 行业平均对比
  %(prog)s 600519 --avg             # 与行业平均对比
  %(prog)s 600519 --rank            # 行业ROE排名

  # 港股
  %(prog)s 00700                    # 港股腾讯同行业对比
        """
    )
    parser.add_argument("code", help="股票代码")
    parser.add_argument("--top", "-n", type=int, default=5, help="同行业公司数量，默认5")
    parser.add_argument("--trend", action="store_true", help="显示财务趋势")
    parser.add_argument("--avg", action="store_true", help="与行业平均对比")
    parser.add_argument("--rank", action="store_true", help="行业ROE排名")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--output", "-o", help="输出到Excel文件")

    args = parser.parse_args()
    code = args.code.strip()

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        is_hk = is_hk_stock(code)

        if is_hk:
            analysis = HKSharePeerAnalysis(conn)
            print(f"分析港股: {code}")
        else:
            analysis = ASharePeerAnalysis(conn)
            print(f"分析A股: {code}")

        # 获取行业信息
        first, second, third = analysis.get_industry(code)
        if first:
            print_industry_info(first, second, third)

        results = {}

        # 行业排名
        if args.rank:
            rank_df = analysis.get_industry_ranking(code, args.top if args.top > 10 else 20)
            print(f"\n{'='*20} 行业ROE排名 {'='*20}")
            print_ranking(rank_df, code)
            results["行业排名"] = rank_df

        # 行业平均对比
        if args.avg:
            stock_df = analysis.get_stock_metrics(code)
            if third:
                industry_df = analysis.get_industry_avg(third)
                print(f"\n{'='*20} 个股 vs 行业平均 {'='*20}")
                print_comparison(stock_df, industry_df)
                results["个股指标"] = stock_df
                results["行业平均"] = industry_df

        # 同行业对比（默认，当没有指定rank和avg时）
        if not args.rank and not args.avg:
            peer_codes = analysis.get_peer_companies(code, args.top)
            print(f"\n同行业公司({len(peer_codes)}家): {', '.join(peer_codes)}")

            comparison_df = analysis.get_peer_comparison(peer_codes)
            print_dataframe(comparison_df, "同行业对比", highlight_code=code)
            results["同行业对比"] = comparison_df

            if args.trend and hasattr(analysis, 'get_financial_trend'):
                trend_df = analysis.get_financial_trend(peer_codes, years=3)
                print_dataframe(trend_df, "财务趋势(近3年)")
                results["财务趋势"] = trend_df

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
