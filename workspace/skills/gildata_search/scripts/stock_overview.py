#!/usr/bin/env python3
"""
股票综合概览查询 - 一站式获取财务+估值数据
用法:
    python stock_overview.py 600519                    # 贵州茅台综合概览
    python stock_overview.py 600519,000858             # 多股对比
    python stock_overview.py 600519 --years 5          # 指定历史年数

数据来源:
  - LC_DIndicesForValuation (估值指标: PE/PB/PS/EV/EBITDA/市值)
  - LC_MainIndexNew (财务指标: ROE/毛利率/增速等)
  - LC_IncomeStatementAll (利润表: 营收/净利润)
  - LC_CashFlowStatementAll (现金流)

输出字段:
  - 估值: 市值(亿)、PE(TTM)、PB(MRQ)、PS(TTM)、EV/EBITDA
  - 财务(当期): 营业收入、归母净利润、经营现金流、EPS、ROE
  - 成长: 营收同比、净利润同比、现金流同比
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
from decimal import Decimal
from pathlib import Path
from typing import List, Dict, Any, Optional

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
    return len(code) == 5 and code.isdigit()

def format_codes(codes: List[str]) -> str:
    return "(" + ", ".join(f"'{c}'" for c in codes) + ")"

def safe_float(val) -> Optional[float]:
    """安全转换为float，处理Decimal和str类型"""
    if val is None or pd.isna(val):
        return None
    try:
        return float(Decimal(str(val)))
    except:
        return None

# ============ A股综合查询 ============
class AShareOverviewQuery:
    """A股综合概览查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_overview(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        """获取综合概览数据"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=years * 365)).strftime("%Y-%m-%d")

        # 综合查询：估值 + 财务指标 + 利润表 + 现金流
        sql = f"""
        SELECT
            sm.SecuCode as 股票代码,
            sm.ChiNameAbbr as 股票简称,
            DATE_FORMAT(idx.EndDate, '%Y-%m-%d') as 报告期,

            -- 估值指标 (取报告期对应的交易日估值)
            val.TotalMV / 1e8 as 市值_亿,
            val.PE as PE_TTM,
            val.PB as PB_MRQ,
            val.PSTTM as PS_TTM,
            val.EVToEBITDA as EV_EBITDA,

            -- 财务指标
            idx.BasicEPS as EPS,
            idx.ROE as ROE,
            idx.GrossIncomeRatio as 销售毛利率,
            idx.NetProfitRatio as 销售净利率,
            idx.OperatingRevenueGrowRate as 营收同比,
            idx.NetProfitGrowRate as 净利润同比,
            idx.NetProfitCashCover as 净利润现金含量,

            -- 利润表
            inc.TotalOperatingRevenue / 1e8 as 营业收入_亿,
            inc.NPParentCompanyOwners / 1e8 as 归母净利润_亿,

            -- 现金流
            cf.NetOperateCashFlow / 1e8 as 经营现金流_亿

        FROM SecuMain sm
        JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
        LEFT JOIN LC_IncomeStatementAll inc ON sm.CompanyCode = inc.CompanyCode
            AND idx.EndDate = inc.EndDate AND inc.IfMerged = 1 AND inc.IfComplete = 1
        LEFT JOIN LC_CashFlowStatementAll cf ON sm.CompanyCode = cf.CompanyCode
            AND idx.EndDate = cf.EndDate AND cf.IfMerged = 1 AND cf.IfComplete = 1
        LEFT JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
            AND val.TradingDay = (
                SELECT MAX(TradingDay) FROM LC_DIndicesForValuation
                WHERE InnerCode = sm.InnerCode AND TradingDay <= idx.EndDate
            )
        WHERE sm.SecuCode IN {codes_str}
        AND sm.SecuCategory = 1
        AND sm.SecuMarket IN (18, 83, 90, 81)
        AND idx.EndDate >= '{start_date}'
        ORDER BY sm.SecuCode, idx.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)

        # 去重（同一报告期可能有多条记录）
        df = df.drop_duplicates(subset=['股票代码', '报告期'], keep='first')

        # 数据类型转换 (LC_MainIndexNew的百分比字段已经是百分比形式，如15.71表示15.71%)
        pct_cols = ['ROE', '销售毛利率', '销售净利率', '营收同比', '净利润同比', '净利润现金含量']
        for col in pct_cols:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: safe_float(x) if safe_float(x) else None)

        return df

    def get_latest_valuation(self, codes: List[str]) -> pd.DataFrame:
        """获取最新估值数据"""
        codes_str = format_codes(codes)

        sql = f"""
        SELECT
            sm.SecuCode as 股票代码,
            sm.ChiNameAbbr as 股票简称,
            DATE_FORMAT(val.TradingDay, '%Y-%m-%d') as 估值日期,
            val.TotalMV / 1e8 as 总市值_亿,
            val.NegotiableMV / 1e8 as 流通市值_亿,
            val.PE as PE_TTM,
            val.PELYR as PE_LYR,
            val.PB as PB_MRQ,
            val.PBLF as PB_LF,
            val.PSTTM as PS_TTM,
            val.PS as PS_LYR,
            val.EVToEBITDA as EV_EBITDA,
            val.EnterpriseValueN / 1e8 as 企业价值_亿,
            val.DividendRatio as 股息率_TTM,
            val.PEG as PEG
        FROM SecuMain sm
        JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
        WHERE sm.SecuCode IN {codes_str}
        AND sm.SecuCategory = 1
        AND sm.SecuMarket IN (18, 83, 90, 81)
        AND val.TradingDay = (
            SELECT MAX(TradingDay) FROM LC_DIndicesForValuation
        )
        ORDER BY sm.SecuCode
        """
        df = pd.read_sql(sql, self.conn)

        # 股息率已经是百分比形式（如3.54表示3.54%），不需要乘以100
        if '股息率_TTM' in df.columns:
            df['股息率_TTM'] = df['股息率_TTM'].apply(lambda x: safe_float(x) if safe_float(x) else None)

        return df

    def get_multi_period_data(self, code: str, periods: int = 8) -> pd.DataFrame:
        """获取多期财务数据（用于趋势分析）"""
        sql = f"""
        SELECT
            sm.SecuCode as 股票代码,
            sm.ChiNameAbbr as 股票简称,
            DATE_FORMAT(idx.EndDate, '%Y-%m-%d') as 报告期,
            YEAR(idx.EndDate) as 年份,
            QUARTER(idx.EndDate) as 季度,

            idx.TotalOperatingRevenuePS as 每股营收,
            idx.BasicEPS as EPS,
            idx.NetAssetPS as 每股净资产,
            idx.OperCashFlowPS as 每股经营现金流,

            idx.ROE as ROE,
            idx.ROA as ROA,
            idx.GrossIncomeRatio as 毛利率,
            idx.NetProfitRatio as 净利率,

            idx.OperatingRevenueGrowRate as 营收同比,
            idx.NetProfitGrowRate as 净利润同比,
            idx.TotalAssetGrowRate as 总资产同比,

            idx.CurrentRatio as 流动比率,
            idx.QuickRatio as 速动比率,
            idx.DebtAssetsRatio as 资产负债率,
            idx.NetProfitCashCover as 现金含量

        FROM SecuMain sm
        JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
        WHERE sm.SecuCode = '{code}'
        AND sm.SecuCategory = 1
        AND sm.SecuMarket IN (18, 83, 90, 81)
        ORDER BY idx.EndDate DESC
        LIMIT {periods}
        """
        df = pd.read_sql(sql, self.conn)

        # LC_MainIndexNew中的百分比字段已经是百分比形式(如25.14表示25.14%)，无需转换
        return df

    def get_consensus_forecast(self, codes: List[str], years: List[int] = None) -> pd.DataFrame:
        """获取分析师一致预期数据"""
        codes_str = format_codes(codes)
        current_year = datetime.now().year
        if years is None:
            years = [current_year, current_year + 1, current_year + 2]
        year_filter = ", ".join(str(y) for y in years)

        sql = f"""
        SELECT
            sm.SecuCode as 股票代码,
            sm.ChiNameAbbr as 股票简称,
            fc.ForecastYear as 预测年度,
            COUNT(*) as 分析师数量,
            AVG(fc.EPS) as EPS一致预期,
            AVG(fc.PNetProfit) / 1e4 as 归母净利润一致预期_亿,
            AVG(fc.OpIncome) / 1e4 as 营业收入一致预期_亿,
            AVG(fc.ROE) as ROE一致预期,
            MIN(fc.EPS) as EPS最低,
            MAX(fc.EPS) as EPS最高
        FROM SecuMain sm
        JOIN c_rr_profitforecast fc ON sm.InnerCode = fc.InnerCode
        WHERE sm.SecuCode IN {codes_str}
        AND sm.SecuCategory = 1
        AND fc.ForecastYear IN ({year_filter})
        AND fc.EPS IS NOT NULL
        GROUP BY sm.SecuCode, fc.ForecastYear
        ORDER BY sm.SecuCode, fc.ForecastYear
        """
        df = pd.read_sql(sql, self.conn)

        # 数据类型转换
        for col in ['EPS一致预期', 'EPS最低', 'EPS最高']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: safe_float(x) if safe_float(x) else None)
        for col in ['归母净利润一致预期_亿', '营业收入一致预期_亿']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: safe_float(x) if safe_float(x) else None)
        for col in ['ROE一致预期']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: safe_float(x) if safe_float(x) else None)

        return df

    def get_valuation_percentile(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        """计算估值指标历史分位数"""
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=years * 365)).strftime("%Y-%m-%d")

        # 获取当前估值和历史数据
        sql = f"""
        WITH current_val AS (
            SELECT
                sm.SecuCode,
                sm.ChiNameAbbr,
                val.PE,
                val.PB,
                val.PSTTM
                FROM SecuMain sm
                JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
                WHERE sm.SecuCode IN {codes_str}
                AND sm.SecuCategory = 1
                AND val.TradingDay = (SELECT MAX(TradingDay) FROM LC_DIndicesForValuation)
        ),
        hist_stats AS (
            SELECT
                sm.SecuCode,
                COUNT(*) as 样本数,
                MIN(val.PE) as PE_最小,
                MAX(val.PE) as PE_最大,
                AVG(val.PE) as PE_均值,
                MIN(val.PB) as PB_最小,
                MAX(val.PB) as PB_最大,
                AVG(val.PB) as PB_均值,
                MIN(val.PSTTM) as PS_最小,
                MAX(val.PSTTM) as PS_最大,
                AVG(val.PSTTM) as PS_均值
            FROM SecuMain sm
            JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND val.TradingDay >= '{start_date}'
            AND val.PE IS NOT NULL
            GROUP BY sm.SecuCode
        ),
        percentile_calc AS (
            SELECT
                sm.SecuCode,
                SUM(CASE WHEN val.PE <= cv.PE THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as PE分位数,
                SUM(CASE WHEN val.PB <= cv.PB THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as PB分位数,
                SUM(CASE WHEN val.PSTTM <= cv.PSTTM THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as PS分位数
            FROM SecuMain sm
            JOIN LC_DIndicesForValuation val ON sm.InnerCode = val.InnerCode
            JOIN current_val cv ON sm.SecuCode = cv.SecuCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND val.TradingDay >= '{start_date}'
            AND val.PE IS NOT NULL
            GROUP BY sm.SecuCode
        )
        SELECT
            cv.SecuCode as 股票代码,
            cv.ChiNameAbbr as 股票简称,
            hs.样本数,
            pc.PE分位数,
            pc.PB分位数,
            pc.PS分位数,
            cv.PE as 当前PE,
            hs.PE_最小,
            hs.PE_均值,
            hs.PE_最大,
            cv.PB as 当前PB,
            hs.PB_最小,
            hs.PB_均值,
            hs.PB_最大,
            cv.PSTTM as 当前PS,
            hs.PS_最小,
            hs.PS_均值,
            hs.PS_最大
        FROM current_val cv
        JOIN hist_stats hs ON cv.SecuCode = hs.SecuCode
        JOIN percentile_calc pc ON cv.SecuCode = pc.SecuCode
        """
        df = pd.read_sql(sql, self.conn)
        return df

# ============ 港股综合查询 ============
class HKShareOverviewQuery:
    """港股综合概览查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_overview(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        codes_str = format_codes(codes)
        start_date = (datetime.now() - timedelta(days=years * 365)).strftime("%Y-%m-%d")

        sql = f"""
        SELECT
            sm.SecuCode as 股票代码,
            sm.ChiName as 股票简称,
            DATE_FORMAT(der.EndDate, '%Y-%m-%d') as 报告期,

            der.EPS as EPS,
            der.ROE as ROE,
            der.GrossIncomeRatio as 毛利率,
            der.NetProfitRatio as 净利率,
            der.CurrentRatio as 流动比率,
            der.QuickRatio as 速动比率,
            der.DebtAssetsRatio as 资产负债率,

            inc.TotOpeRev / 1e8 as 营业收入_亿,
            inc.NPPCompOwners / 1e8 as 归母净利润_亿,
            cf.NetOpeCFlow / 1e8 as 经营现金流_亿

        FROM HK_SecuMain sm
        LEFT JOIN HK_Derivative der ON sm.CompanyCode = der.CompanyCode
        LEFT JOIN HK_IncomeStatementCN inc ON sm.CompanyCode = inc.CompanyCode AND der.EndDate = inc.EndDate
        LEFT JOIN HK_CashFlowStatementCN cf ON sm.CompanyCode = cf.CompanyCode AND der.EndDate = cf.EndDate
        WHERE sm.SecuCode IN {codes_str}
        AND der.EndDate >= '{start_date}'
        ORDER BY sm.SecuCode, der.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)

        pct_cols = ['ROE', '毛利率', '净利率', '资产负债率']
        for col in pct_cols:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: safe_float(x) * 100 if safe_float(x) else None)

        return df

# ============ 输出格式化 ============
def print_overview(df: pd.DataFrame, title: str = "综合概览"):
    """打印综合概览表格"""
    if df.empty:
        print("*无数据*")
        return

    print(f"\n### {title}\n")

    # 显示列
    cols = ['股票简称', '报告期', '市值_亿', 'PE_TTM', 'PB_MRQ', 'PS_TTM', 'EV_EBITDA',
            '营业收入_亿', '归母净利润_亿', '营收同比', '净利润同比', 'EPS', 'ROE', '经营现金流_亿']
    cols = [c for c in cols if c in df.columns]

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df.head(10).iterrows():
        values = []
        for col in cols:
            val = row.get(col)
            if pd.isna(val) or val is None:
                values.append("-")
            elif col in ['营收同比', '净利润同比', 'ROE']:
                values.append(f"{val:.1f}%")
            elif col in ['PE_TTM', 'PB_MRQ', 'PS_TTM', 'EV_EBITDA']:
                values.append(f"{val:.2f}")
            elif col in ['市值_亿', '营业收入_亿', '归母净利润_亿', '经营现金流_亿', 'EPS']:
                values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

def print_valuation(df: pd.DataFrame):
    """打印估值数据"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 最新估值指标\n")

    cols = ['股票简称', '估值日期', '总市值_亿', 'PE_TTM', 'PE_LYR', 'PB_MRQ', 'PS_TTM', 'EV_EBITDA', '股息率_TTM', 'PEG']
    cols = [c for c in cols if c in df.columns]

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df.iterrows():
        values = []
        for col in cols:
            val = row.get(col)
            if pd.isna(val) or val is None:
                values.append("-")
            elif col == '股息率_TTM':
                values.append(f"{val:.2f}%")
            elif col in ['PE_TTM', 'PE_LYR', 'PB_MRQ', 'PS_TTM', 'EV_EBITDA', 'PEG']:
                values.append(f"{val:.2f}")
            elif col in ['总市值_亿', '企业价值_亿']:
                values.append(f"{val:.1f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

def print_consensus(df: pd.DataFrame):
    """打印分析师一致预期数据"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 分析师一致预期\n")

    cols = ['股票简称', '预测年度', '分析师数量', 'EPS一致预期', 'EPS最低', 'EPS最高',
          '归母净利润一致预期_亿', '营业收入一致预期_亿', 'ROE一致预期']
    cols = [c for c in cols if c in df.columns]

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df.iterrows():
        values = []
        for col in cols:
            val = row.get(col)
            if pd.isna(val) or val is None:
                values.append("-")
            elif col == 'ROE一致预期':
                values.append(f"{val:.1f}%")
            elif col in ['EPS一致预期', 'EPS最低', 'EPS最高']:
                values.append(f"{val:.2f}")
            elif col in ['归母净利润一致预期_亿', '营业收入一致预期_亿']:
                values.append(f"{val:.1f}")
            else:
                values.append(str(int(val)) if isinstance(val, (int, float)) else str(val))
        print("| " + " | ".join(values) + " |")

    print("\n*数据来源: 恒生聚源 c_RR_ProfitForecast 表（分析师预测汇总）")

def print_percentile(df: pd.DataFrame):
    """打印估值历史分位数"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 估值历史分位数（近3年）\n")

    # 表头
    print("| 股票简称 | 样本数 | PE分位 | PB分位 | PS分位 | 当前PE | PE区间 | 当前PB | PB区间 | 当前PS | PS区间 |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")

    # 数据行
    for _, row in df.iterrows():
        name = row.get('股票简称', '-')
        samples = int(row.get('样本数', 0)) if row.get('样本数') else 0

        pe_pct = row.get('PE分位数')
        pb_pct = row.get('PB分位数')
        ps_pct = row.get('PS分位数')

        pe_curr = row.get('当前PE')
        pe_min = row.get('PE_最小')
        pe_avg = row.get('PE_均值')
        pe_max = row.get('PE_最大')

        pb_curr = row.get('当前PB')
        pb_min = row.get('PB_最小')
        pb_avg = row.get('PB_均值')
        pb_max = row.get('PB_最大')

        ps_curr = row.get('当前PS')
        ps_min = row.get('PS_最小')
        ps_avg = row.get('PS_均值')
        ps_max = row.get('PS_最大')

        def fmt_pct(v):
            return f"{v:.1f}%" if v and not pd.isna(v) else "-"

        def fmt_val(v):
            return f"{v:.2f}" if v and not pd.isna(v) else "-"

        def fmt_range(lo, hi):
            if lo and hi and not pd.isna(lo) and not pd.isna(hi):
                return f"{lo:.1f}-{hi:.1f}"
            return "-"

        print(f"| {name} | {samples} | {fmt_pct(pe_pct)} | {fmt_pct(pb_pct)} | {fmt_pct(ps_pct)} | {fmt_val(pe_curr)} | {fmt_range(pe_min, pe_max)} | {fmt_val(pb_curr)} | {fmt_range(pb_min, pb_max)} | {fmt_val(ps_curr)} | {fmt_range(ps_min, ps_max)} |")

    print("\n*分位数说明: 0%=历史最低, 100%=历史最高, 50%=中位数")
    print("*数据来源: 恒生聚源 LC_DIndicesForValuation 表（近3年日度估值数据）")

def print_multi_period(df: pd.DataFrame):
    """打印多期财务数据"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 历史财务指标趋势\n")

    cols = ['报告期', 'EPS', 'ROE', '毛利率', '净利率', '营收同比', '净利润同比', '流动比率', '资产负债率']
    cols = [c for c in cols if c in df.columns]

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df.iterrows():
        values = []
        for col in cols:
            val = row.get(col)
            if pd.isna(val) or val is None:
                values.append("-")
            elif col in ['ROE', '毛利率', '净利率', '营收同比', '净利润同比', '资产负债率']:
                values.append(f"{val:.1f}%")
            elif col in ['EPS', '流动比率']:
                values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

def print_consensus(df: pd.DataFrame):
    """打印分析师一致预期"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 分析师一致预期\n")

    cols = ['股票简称', '预测年度', '分析师数量', 'EPS一致预期', 'EPS最低', 'EPS最高',
                  '归母净利润一致预期_亿', '营业收入一致预期_亿', 'ROE一致预期']
    cols = [c for c in cols if c in df.columns]

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df.iterrows():
        values = []
        for col in cols:
            val = row.get(col)
            if pd.isna(val) or val is None:
                values.append("-")
            elif col == 'ROE一致预期':
                values.append(f"{val:.1f}%")
            elif col in ['EPS一致预期', 'EPS最低', 'EPS最高']:
                values.append(f"{val:.2f}")
            elif col in ['归母净利润一致预期_亿', '营业收入一致预期_亿']:
                values.append(f"{val:.1f}")
            elif col == '分析师数量':
                values.append(str(int(val)))
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    print("\n*数据来源: 恒生聚源 c_RR_ProfitForecast 表（分析师预测汇总）")

# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票综合概览查询 - 一站式获取财务+估值数据",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 600519                    # 贵州茅台综合概览
  %(prog)s 600519,000858             # 多股对比
  %(prog)s 600519                    # 贵州茅台综合概览
  %(prog)s 600519,000858             # 多股对比
  %(prog)s 600519 --years 5          # 指定历史年数
  %(prog)s 600519 --valuation        # 仅查看估值
  %(prog)s 600519 --trend            # 查看多期趋势
  %(prog)s 600519 --consensus         # 分析师一致预期
  %(prog)s 600519,000858 --consensus  # 多股对比预测

数据说明:
  - 估值指标来自 LC_DIndicesForValuation (日频)
  - 财务指标来自 LC_MainIndexNew (季频)
  - 一致预期来自 c_RR_ProfitForecast (分析师预测)
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--years", "-y", type=int, default=3, help="查询历史年数，默认3年")
    parser.add_argument("--valuation", "-v", action="store_true", help="仅查看最新估值")
    parser.add_argument("--trend", "-t", action="store_true", help="查看多期趋势")
    parser.add_argument("--consensus", action="store_true", help="查看分析师一致预期")
    parser.add_argument("--percentile", action="store_true", help="查看估值历史分位数")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--output", "-o", help="输出Excel")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        # 判断市场
        hk_codes = [c for c in codes if is_hk_stock(c)]
        a_codes = [c for c in codes if not is_hk_stock(c)]

        if hk_codes:
            print(f"提示: 港股 {hk_codes} 功能有限")
            if not a_codes:
                query = HKShareOverviewQuery(conn)
                df = query.get_overview(hk_codes, args.years)
                print_overview(df, "港股综合概览")
                return

        if a_codes:
            print(f"查询A股: {a_codes}")
            query = AShareOverviewQuery(conn)

            if args.valuation:
                # 仅估值
                df = query.get_latest_valuation(a_codes)
                print_valuation(df)
                results = {"估值": df}
            elif args.trend and len(a_codes) == 1:
                # 多期趋势
                df = query.get_multi_period_data(a_codes[0], 12)
                print_multi_period(df)
                results = {"趋势": df}
            elif args.consensus:
                # 分析师一致预期
                df = query.get_consensus_forecast(a_codes, years=[datetime.now().year, datetime.now().year + 1, datetime.now().year + 2])
                print_consensus(df)
                results = {"一致预期": df}
            elif args.percentile:
                # 估值历史分位数
                df = query.get_valuation_percentile(a_codes, years=args.years)
                print_percentile(df)
                results = {"估值分位": df}
            else:
                # 综合概览
                df = query.get_overview(a_codes, args.years)
                print_overview(df)
                results = {"概览": df}

                # 如果是单股，也显示最新估值
                if len(a_codes) == 1:
                    val_df = query.get_latest_valuation(a_codes)
                    print_valuation(val_df)
                    results["估值"] = val_df

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
