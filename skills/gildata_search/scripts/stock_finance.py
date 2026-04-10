#!/usr/bin/env python3
"""
股票财务数据综合查询
用法:
    # 基础财务报表
    python stock_finance.py 600519 --type balance        # 资产负债表
    python stock_finance.py 600519 --type income         # 利润表
    python stock_finance.py 600519 --type cash           # 现金流量表
    python stock_finance.py 600519 --type index          # 主要财务指标
    python stock_finance.py 600519 --type all            # 全部报表

    # 单季度数据（含同比环比）
    python stock_finance.py 600519 --quarter             # 单季度利润表+同比环比
    python stock_finance.py 600519 --quarter --cash      # 单季度现金流

    # 杜邦分析
    python stock_finance.py 600519 --dupont              # 杜邦分析（ROE拆解）
    python stock_finance.py 600519,000858 --dupont       # 多股杜邦对比

    # 多股对比
    python stock_finance.py 600519,000858 --type index   # 多股财务指标对比
    python stock_finance.py 00700 --type all             # 港股

数据表:
  - LC_BalanceSheetAll (A股资产负债表)
  - LC_IncomeStatementAll (A股利润表)
  - LC_CashFlowStatementAll (A股现金流量表)
  - LC_MainIndexNew (A股主要财务指标)
  - HK_* (港股对应表)
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
from typing import List, Optional, Dict, Any, Tuple

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


def is_stib_stock(code: str) -> bool:
    """判断是否科创板股票"""
    return code.startswith('688')


def format_codes(codes: List[str]) -> str:
    return "(" + ", ".join(f"'{c}'" for c in codes) + ")"


def get_date_range(years: int = 3) -> tuple:
    end_date = datetime.now()
    start_date = end_date - timedelta(days=years * 365)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")


# ============ A股财务查询 ============
class AShareFinanceQuery:
    """A股财务数据查询"""

    BALANCE_COLUMNS = [
        "EndDate", "InfoSource",
        "CashEquivalents", "AccountReceivable", "Inventories",
        "TotalCurrentAssets", "FixedAssets", "IntangibleAssets", "GoodWill",
        "TotalAssets", "TotalCurrentLiability", "TotalLiability",
        "TotalShareholderEquity", "SEWithoutMI"
    ]

    INCOME_COLUMNS = [
        "EndDate", "InfoSource",
        "TotalOperatingRevenue", "OperatingRevenue", "TotalOperatingCost",
        "OperatingProfit", "TotalProfit", "NetProfit",
        "NPParentCompanyOwners", "BasicEPS", "DilutedEPS"
    ]

    CASH_COLUMNS = [
        "EndDate", "InfoSource",
        "NetOperateCashFlow", "NetInvestCashFlow", "NetFinanceCashFlow",
        "CashEquivalentIncrease", "EndPeriodCashEquivalent"
    ]

    INDEX_COLUMNS = [
        "EndDate", "BasicEPS", "NetAssetPS", "OperCashFlowPS",
        "ROE", "ROA", "GrossIncomeRatio", "NetProfitRatio",
        "CurrentRatio", "QuickRatio", "DebtAssetsRatio",
        "OperatingRevenueGrowRate", "NetProfitGrowRate", "NetProfitCashCover"
    ]

    # 科创板财务指标字段（lc_stibmainindex表缺少成长能力字段）
    STIB_INDEX_COLUMNS = [
        "EndDate", "BasicEPS", "NetAssetPS", "OperCashFlowPS",
        "ROE", "ROA", "GrossIncomeRatio", "NetProfitRatio",
        "CurrentRatio", "QuickRatio", "DebtAssetsRatio",
        "NetProfitCashCover"
    ]

    COLUMN_MAPPING = {
        "CashEquivalents": "货币资金", "AccountReceivable": "应收账款",
        "Inventories": "存货", "TotalCurrentAssets": "流动资产合计",
        "FixedAssets": "固定资产", "IntangibleAssets": "无形资产", "GoodWill": "商誉",
        "TotalAssets": "资产总计", "TotalCurrentLiability": "流动负债合计",
        "TotalLiability": "负债合计", "TotalShareholderEquity": "所有者权益合计",
        "SEWithoutMI": "归属母公司股东权益",
        "TotalOperatingRevenue": "营业总收入", "OperatingRevenue": "营业收入",
        "TotalOperatingCost": "营业总成本", "OperatingProfit": "营业利润",
        "TotalProfit": "利润总额", "NetProfit": "净利润",
        "NPParentCompanyOwners": "归母净利润", "BasicEPS": "基本每股收益",
        "DilutedEPS": "稀释每股收益",
        "NetOperateCashFlow": "经营活动现金流净额",
        "NetInvestCashFlow": "投资活动现金流净额",
        "NetFinanceCashFlow": "筹资活动现金流净额",
        "CashEquivalentIncrease": "现金及等价物净增加额",
        "EndPeriodCashEquivalent": "期末现金及等价物余额",
        "NetAssetPS": "每股净资产", "OperCashFlowPS": "每股经营现金流",
        "ROE": "ROE(摊薄)", "ROA": "ROA(摊薄)",
        "GrossIncomeRatio": "销售毛利率", "NetProfitRatio": "销售净利率",
        "CurrentRatio": "流动比率", "QuickRatio": "速动比率",
        "DebtAssetsRatio": "资产负债率", "OperatingRevenueGrowRate": "营收增速",
        "NetProfitGrowRate": "净利润增速", "NetProfitCashCover": "净利润现金含量",
        "EndDate": "截止日期", "InfoSource": "信息来源",
        "SecuCode": "股票代码", "SecuAbbr": "股票简称"
    }

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def _query_table(self, table: str, codes: List[str], columns: List[str],
                     start_date: str, end_date: str, filter_clause: str = "") -> pd.DataFrame:
        cols = ", ".join(columns)
        codes_str = format_codes(codes)
        sql = f"""
            SELECT SecuCode, SecuMain.ChiNameAbbr as SecuAbbr, {cols}
            FROM {table}
            JOIN SecuMain ON {table}.CompanyCode = SecuMain.CompanyCode
            WHERE SecuCode IN {codes_str}
            AND SecuMain.SecuCategory = 1 AND SecuMain.SecuMarket IN (18, 83, 90)
            AND IfMerged = 1 AND IfComplete = 1 AND IfAdjusted IN (1, 2)
            AND AccountingStandards = 1
            AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
            {filter_clause}
            ORDER BY SecuCode, EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)
        return df

    def get_balance_sheet(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        df = self._query_table(
            "LC_BalanceSheetAll", codes, self.BALANCE_COLUMNS,
            start_date, end_date,
            "AND InfoSource IN ('季度报告', '半年度报告', '年度报告')"
        )
        return self._format_amount(df)

    def get_income_sheet(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        df = self._query_table(
            "LC_IncomeStatementAll", codes, self.INCOME_COLUMNS,
            start_date, end_date,
            "AND InfoSource IN ('季度报告', '半年度报告', '年度报告')"
        )
        return self._format_amount(df)

    def get_cash_sheet(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        df = self._query_table(
            "LC_CashFlowStatementAll", codes, self.CASH_COLUMNS,
            start_date, end_date,
            "AND InfoSource IN ('季度报告', '半年度报告', '年度报告')"
        )
        return self._format_amount(df)

    def get_main_index(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        codes_str = format_codes(codes)

        # 检测是否科创板（688开头）
        all_stib = all(is_stib_stock(c) for c in codes)

        if all_stib:
            # 科创板使用 lc_stibmainindex 表，字段较少
            cols = ", ".join(self.STIB_INDEX_COLUMNS)
            sql = f"""
                SELECT SecuCode, SecuMain.ChiNameAbbr as SecuAbbr, {cols}
                FROM lc_stibmainindex
                JOIN SecuMain ON lc_stibmainindex.CompanyCode = SecuMain.CompanyCode
                WHERE SecuCode IN {codes_str}
                AND SecuMain.SecuCategory = 1 AND SecuMain.SecuMarket = 83
                AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
                AND IfMerged = 1 AND IfAdjusted IN (1, 2)
                ORDER BY SecuCode, EndDate DESC
            """
        else:
            # 普通A股使用 LC_MainIndexNew 表
            cols = ", ".join(self.INDEX_COLUMNS)
            sql = f"""
                SELECT SecuCode, SecuMain.ChiNameAbbr as SecuAbbr, {cols}
                FROM LC_MainIndexNew
                JOIN SecuMain ON LC_MainIndexNew.CompanyCode = SecuMain.CompanyCode
                WHERE SecuCode IN {codes_str}
                AND SecuMain.SecuCategory = 1 AND SecuMain.SecuMarket IN (18, 83, 90)
                AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
                ORDER BY SecuCode, EndDate DESC
            """
        df = pd.read_sql(sql, self.conn)
        df = df.rename(columns=self.COLUMN_MAPPING)
        return df

    def get_quarterly_income(self, code: str, quarters: int = 12) -> pd.DataFrame:
        """获取单季度利润表（含同比环比）"""
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                inc.InfoSource as 信息来源,
                inc.EndDate as 报告期,
                YEAR(inc.EndDate) as 年份,
                QUARTER(inc.EndDate) as 季度,
                inc.OperatingRevenue as 营业收入_累计,
                inc.NPParentCompanyOwners as 归母净利润_累计,
                inc.BasicEPS as EPS_累计
            FROM SecuMain sm
            JOIN LC_IncomeStatementAll inc ON sm.CompanyCode = inc.CompanyCode
            WHERE sm.SecuCode = '{code}'
            AND sm.SecuCategory = 1 AND sm.SecuMarket IN (18, 83, 90)
            AND inc.IfMerged = 1 AND inc.IfComplete = 1 AND inc.IfAdjusted IN (1, 2)
            AND inc.AccountingStandards = 1
            AND inc.InfoSource IN ('季度报告', '半年度报告', '年度报告')
            ORDER BY inc.EndDate DESC
            LIMIT {quarters}
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return df

        # 计算单季度数据
        df = df.sort_values('报告期')
        df['营业收入_单季'] = df['营业收入_累计'].diff()
        df['归母净利润_单季'] = df['归母净利润_累计'].diff()
        df['EPS_单季'] = df['EPS_累计'].diff()

        # Q1不需要diff
        df.loc[df['季度'] == 1, '营业收入_单季'] = df.loc[df['季度'] == 1, '营业收入_累计']
        df.loc[df['季度'] == 1, '归母净利润_单季'] = df.loc[df['季度'] == 1, '归母净利润_累计']
        df.loc[df['季度'] == 1, 'EPS_单季'] = df.loc[df['季度'] == 1, 'EPS_累计']

        # 计算同比环比
        df['营收_同比%'] = df.groupby('季度')['营业收入_单季'].pct_change() * 100
        df['利润_同比%'] = df.groupby('季度')['归母净利润_单季'].pct_change() * 100
        df['营收_环比%'] = df['营业收入_单季'].pct_change() * 100
        df['利润_环比%'] = df['归母净利润_单季'].pct_change() * 100

        # 转换单位
        df['营业收入_单季'] = df['营业收入_单季'] / 1e8
        df['归母净利润_单季'] = df['归母净利润_单季'] / 1e8

        return df.sort_values('报告期', ascending=False)

    def get_quarterly_cashflow(self, code: str, quarters: int = 12) -> pd.DataFrame:
        """获取单季度现金流量表"""
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                cf.InfoSource as 信息来源,
                cf.EndDate as 报告期,
                YEAR(cf.EndDate) as 年份,
                QUARTER(cf.EndDate) as 季度,
                cf.NetOperateCashFlow as 经营现金流_累计,
                cf.NetInvestCashFlow as 投资现金流_累计,
                cf.NetFinanceCashFlow as 筹资现金流_累计
            FROM SecuMain sm
            JOIN LC_CashFlowStatementAll cf ON sm.CompanyCode = cf.CompanyCode
            WHERE sm.SecuCode = '{code}'
            AND sm.SecuCategory = 1 AND sm.SecuMarket IN (18, 83, 90)
            AND cf.IfMerged = 1 AND cf.IfComplete = 1 AND cf.IfAdjusted IN (1, 2)
            AND cf.AccountingStandards = 1
            ORDER BY cf.EndDate DESC
            LIMIT {quarters}
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return df

        df = df.sort_values('报告期')
        df['经营现金流_单季'] = df['经营现金流_累计'].diff()
        df['投资现金流_单季'] = df['投资现金流_累计'].diff()
        df['筹资现金流_单季'] = df['筹资现金流_累计'].diff()

        df.loc[df['季度'] == 1, '经营现金流_单季'] = df.loc[df['季度'] == 1, '经营现金流_累计']
        df.loc[df['季度'] == 1, '投资现金流_单季'] = df.loc[df['季度'] == 1, '投资现金流_累计']
        df.loc[df['季度'] == 1, '筹资现金流_单季'] = df.loc[df['季度'] == 1, '筹资现金流_累计']

        for col in ['经营现金流_单季', '投资现金流_单季', '筹资现金流_单季']:
            df[col] = df[col] / 1e8

        return df.sort_values('报告期', ascending=False)

    def get_duPont_analysis(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        """获取杜邦分析数据"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        # 从利润表获取营业收入，使用DISTINCT去重
        sql = f"""
            SELECT DISTINCT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                YEAR(idx.EndDate) as 年份,
                idx.EndDate as 报告期,
                idx.ROE as ROE,
                idx.NetProfitRatio as 净利率,
                inc.TotalOperatingRevenue as 营业收入,
                bal.TotalAssets as 总资产,
                bal.TotalShareholderEquity as 净资产,
                idx.DebtAssetsRatio as 资产负债率
            FROM SecuMain sm
            JOIN LC_MainIndexNew idx ON sm.CompanyCode = idx.CompanyCode
            JOIN LC_BalanceSheetAll bal ON sm.CompanyCode = bal.CompanyCode AND idx.EndDate = bal.EndDate
            JOIN LC_IncomeStatementAll inc ON sm.CompanyCode = inc.CompanyCode AND idx.EndDate = inc.EndDate
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1 AND sm.SecuMarket IN (18, 83, 90)
            AND YEAR(idx.EndDate) >= {start_year}
            AND bal.IfMerged = 1 AND bal.IfComplete = 1
            AND inc.IfMerged = 1 AND inc.IfComplete = 1
            AND idx.EndDate LIKE '%%-12-%%'
            ORDER BY sm.SecuCode, idx.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return df

        # 计算杜邦分析指标
        df['资产周转率'] = df['营业收入'] / df['总资产']
        df['权益乘数'] = df['总资产'] / df['净资产']
        df['营业收入'] = df['营业收入'] / 1e8
        df['总资产'] = df['总资产'] / 1e8
        df['净资产'] = df['净资产'] / 1e8

        return df

    def get_all_summary(self, codes: List[str], years: int = 3) -> Dict[str, pd.DataFrame]:
        return {
            "主要财务指标": self.get_main_index(codes, years=years),
            "利润表": self.get_income_sheet(codes, years=years),
            "资产负债表": self.get_balance_sheet(codes, years=years),
            "现金流量表": self.get_cash_sheet(codes, years=years),
        }

    def _format_amount(self, df: pd.DataFrame) -> pd.DataFrame:
        amount_cols = [
            "货币资金", "应收账款", "存货", "流动资产合计",
            "固定资产", "无形资产", "商誉", "资产总计",
            "流动负债合计", "负债合计", "所有者权益合计", "归属母公司股东权益",
            "营业总收入", "营业收入", "营业总成本", "营业利润",
            "利润总额", "净利润", "归母净利润",
            "经营活动现金流净额", "投资活动现金流净额", "筹资活动现金流净额",
            "现金及等价物净增加额", "期末现金及等价物余额"
        ]
        for col in amount_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce') / 1e8
        return df


# ============ 港股财务查询 ============
class HKShareFinanceQuery:
    """港股财务数据查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_balance_sheet(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        codes_str = format_codes(codes)
        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName as 股票简称,
                   EndDate as 截止日期, InfoSource as 信息来源,
                   CashEquivalents as 货币资金, AccReceivable as 应收账款,
                   Inventories as 存货, TotalCurAssets as 流动资产合计,
                   TotalAssets as 资产总计, TotalCurLia as 流动负债合计,
                   TotalLiab as 负债合计, TotalShEquity as 股东权益合计
            FROM HK_BalanceSheetCN
            JOIN HK_SecuMain ON HK_BalanceSheetCN.CompanyCode = HK_SecuMain.CompanyCode
            WHERE SecuCode IN {codes_str} AND Mark IN (1, 2)
            AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
            ORDER BY SecuCode, EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return self._format_amount(df)

    def get_income_sheet(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        codes_str = format_codes(codes)
        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName as 股票简称,
                   EndDate as 截止日期, InfoSource as 信息来源,
                   TotOpeRev as 营业总收入, OpeRev as 营业收入,
                   OpeProfit as 营业利润, NetProfit as 净利润,
                   NPPCompOwners as 归母净利润, BasicEPS as 基本每股收益
            FROM HK_IncomeStatementCN
            JOIN HK_SecuMain ON HK_IncomeStatementCN.CompanyCode = HK_SecuMain.CompanyCode
            WHERE SecuCode IN {codes_str} AND Mark IN (1, 2)
            AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
            ORDER BY SecuCode, EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return self._format_amount(df)

    def get_cash_sheet(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        codes_str = format_codes(codes)
        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName as 股票简称,
                   EndDate as 截止日期, InfoSource as 信息来源,
                   NetOpeCFlow as 经营活动现金流净额,
                   NetInvCashFlow as 投资活动现金流净额,
                   NetFinCashFlow as 筹资活动现金流净额
            FROM HK_CashFlowStatementCN
            JOIN HK_SecuMain ON HK_CashFlowStatementCN.CompanyCode = HK_SecuMain.CompanyCode
            WHERE SecuCode IN {codes_str} AND Mark IN (1, 2)
            AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
            ORDER BY SecuCode, EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return self._format_amount(df)

    def get_main_index(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        start_date, end_date = get_date_range(years)
        codes_str = format_codes(codes)
        sql = f"""
            SELECT SecuCode, HK_SecuMain.ChiName as 股票简称,
                   EndDate as 截止日期, EPS as 每股收益,
                   ROE as ROE, DebtAssetsRatio as 资产负债率,
                   GrossIncomeRatio as 毛利率, NetProfitRatio as 净利率,
                   CurrentRatio as 流动比率, QuickRatio as 速动比率
            FROM HK_Derivative
            JOIN HK_SecuMain ON HK_Derivative.CompanyCode = HK_SecuMain.CompanyCode
            WHERE SecuCode IN {codes_str}
            AND EndDate >= '{start_date}' AND EndDate <= '{end_date}'
            ORDER BY SecuCode, EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        return df

    def get_quarterly_income(self, code: str, quarters: int = 12) -> pd.DataFrame:
        """港股单季度利润表"""
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                inc.EndDate as 报告期,
                YEAR(inc.EndDate) as 年份,
                QUARTER(inc.EndDate) as 季度,
                inc.TotOpeRev as 营业收入_累计,
                inc.NPPCompOwners as 归母净利润_累计,
                inc.BasicEPS as EPS_累计
            FROM HK_SecuMain sm
            JOIN HK_IncomeStatementCN inc ON sm.CompanyCode = inc.CompanyCode
            WHERE sm.SecuCode = '{code}' AND inc.Mark IN (1, 2)
            ORDER BY inc.EndDate DESC
            LIMIT {quarters}
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return df

        df = df.sort_values('报告期')
        df['营业收入_单季'] = df['营业收入_累计'].diff()
        df['归母净利润_单季'] = df['归母净利润_累计'].diff()
        df.loc[df['季度'] == 1, '营业收入_单季'] = df.loc[df['季度'] == 1, '营业收入_累计']
        df.loc[df['季度'] == 1, '归母净利润_单季'] = df.loc[df['季度'] == 1, '归母净利润_累计']

        df['营收_同比%'] = df.groupby('季度')['营业收入_单季'].pct_change() * 100
        df['利润_同比%'] = df.groupby('季度')['归母净利润_单季'].pct_change() * 100
        df['营收_环比%'] = df['营业收入_单季'].pct_change() * 100
        df['利润_环比%'] = df['归母净利润_单季'].pct_change() * 100

        df['营业收入_单季'] = df['营业收入_单季'] / 1e8
        df['归母净利润_单季'] = df['归母净利润_单季'] / 1e8
        return df.sort_values('报告期', ascending=False)

    def get_duPont_analysis(self, codes: List[str], years: int = 3) -> pd.DataFrame:
        """港股杜邦分析"""
        codes_str = format_codes(codes)
        start_year = datetime.now().year - years

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                YEAR(der.EndDate) as 年份,
                der.EndDate as 报告期,
                der.ROE as ROE,
                der.NetProfitRatio as 净利率,
                bal.TotalAssets as 总资产,
                bal.TotalShEquity as 净资产,
                inc.TotOpeRev as 营业收入
            FROM HK_SecuMain sm
            JOIN HK_Derivative der ON sm.CompanyCode = der.CompanyCode
            JOIN HK_BalanceSheetCN bal ON sm.CompanyCode = bal.CompanyCode AND der.EndDate = bal.EndDate
            JOIN HK_IncomeStatementCN inc ON sm.CompanyCode = inc.CompanyCode AND der.EndDate = inc.EndDate
            WHERE sm.SecuCode IN {codes_str}
            AND YEAR(der.EndDate) >= {start_year}
            AND der.EndDate LIKE '%%-12-%%'
            ORDER BY sm.SecuCode, der.EndDate DESC
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return df

        df['资产周转率'] = df['营业收入'] / df['总资产']
        df['权益乘数'] = df['总资产'] / df['净资产']
        df['营业收入'] = df['营业收入'] / 1e8
        df['总资产'] = df['总资产'] / 1e8
        df['净资产'] = df['净资产'] / 1e8
        return df

    def get_all_summary(self, codes: List[str], years: int = 3) -> Dict[str, pd.DataFrame]:
        return {
            "主要财务指标": self.get_main_index(codes, years=years),
            "利润表": self.get_income_sheet(codes, years=years),
            "资产负债表": self.get_balance_sheet(codes, years=years),
            "现金流量表": self.get_cash_sheet(codes, years=years),
        }

    def _format_amount(self, df: pd.DataFrame) -> pd.DataFrame:
        amount_cols = [
            "货币资金", "应收账款", "存货", "流动资产合计", "资产总计",
            "流动负债合计", "负债合计", "股东权益合计",
            "营业总收入", "营业收入", "营业利润", "净利润", "归母净利润",
            "经营活动现金流净额", "投资活动现金流净额", "筹资活动现金流净额"
        ]
        for col in amount_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce') / 1e8
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

    # 格式化日期
    for col in ['截止日期', '报告期']:
        if col in df_show.columns:
            df_show = df_show.copy()
            df_show[col] = df_show[col].apply(
                lambda x: x.strftime('%Y-%m-%d') if hasattr(x, 'strftime') else str(x)
            )

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
            elif isinstance(val, float):
                # 智能精度
                col_lower = col.lower()
                if '率' in col or 'roe' in col_lower or 'roa' in col_lower or '%' in col:
                    values.append(f"{val:.2f}%")
                elif 'eps' in col_lower or '每股' in col:
                    values.append(f"{val:.2f}")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共 {total} 条，显示前 {max_rows} 条*")


def print_quarter_income(df: pd.DataFrame, max_rows: int = 8):
    """打印单季度利润表"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 单季度利润表\n")

    cols = ['股票简称', '报告期', '营业收入_单季', '营收_同比%', '归母净利润_单季', '利润_同比%', 'EPS_累计']
    cols = [c for c in cols if c in df.columns]

    total = len(df)
    df_show = df.head(max_rows) if total > max_rows else df

    # 格式化日期
    if '报告期' in df_show.columns:
        df_show = df_show.copy()
        df_show['报告期'] = df_show['报告期'].apply(
            lambda x: x.strftime('%Y-%m-%d') if hasattr(x, 'strftime') else str(x)
        )

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df_show.iterrows():
        values = []
        for col in cols:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif isinstance(val, float):
                if '同比' in col or '%' in col:
                    values.append(f"{val:.1f}%")
                elif '亿' in col:
                    values.append(f"{val:.2f}亿")
                else:
                    values.append(f"{val:.2f}")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共 {total} 条，显示前 {max_rows} 条*")


def print_duPont(df: pd.DataFrame, max_rows: int = 6):
    """打印杜邦分析"""
    if df.empty:
        print("*无数据*")
        return

    print("\n### 杜邦分析: ROE = 净利率 × 资产周转率 × 权益乘数\n")

    cols = ['股票简称', '年份', 'ROE', '净利率', '资产周转率', '权益乘数']
    cols = [c for c in cols if c in df.columns]

    total = len(df)
    df_show = df.head(max_rows) if total > max_rows else df

    # 表头
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df_show.iterrows():
        values = []
        for col in cols:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif col in ['ROE', '净利率']:
                values.append(f"{val:.2f}%")
            elif col == '资产周转率':
                values.append(f"{val:.2f}次")
            elif col == '权益乘数':
                values.append(f"{val:.2f}倍")
            else:
                values.append(str(val))
        print("| " + " | ".join(values) + " |")

    if total > max_rows:
        print(f"\n*共 {total} 条，显示前 {max_rows} 条*")


# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票财务数据综合查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基础财务报表
  %(prog)s 600519 --type balance     # 资产负债表
  %(prog)s 600519 --type income      # 利润表
  %(prog)s 600519 --type cash        # 现金流量表
  %(prog)s 600519 --type index       # 主要财务指标
  %(prog)s 600519 --type all         # 全部报表

  # 单季度数据（含同比环比）
  %(prog)s 600519 --quarter          # 单季度利润表+同比环比
  %(prog)s 600519 --quarter --cash   # 单季度现金流

  # 杜邦分析
  %(prog)s 600519 --dupont           # 杜邦分析
  %(prog)s 600519,000858 --dupont    # 多股杜邦对比

  # 多股对比/港股
  %(prog)s 600519,000858 --type index
  %(prog)s 00700 --type all          # 港股
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--type", "-t", choices=["balance", "income", "cash", "index", "all"],
                        default="index", help="报表类型")
    parser.add_argument("--years", "-y", type=int, default=3, help="查询年数")
    parser.add_argument("--quarter", "-q", action="store_true", help="查询单季度数据")
    parser.add_argument("--cash", action="store_true", help="单季度现金流（配合--quarter）")
    parser.add_argument("--dupont", "-d", action="store_true", help="杜邦分析")
    parser.add_argument("--config", "-c", help="配置文件路径")
    parser.add_argument("--output", "-o", help="输出Excel")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        is_hk = all(is_hk_stock(c) for c in codes)
        if is_hk:
            query = HKShareFinanceQuery(conn)
            print(f"查询港股: {codes}")
        else:
            query = AShareFinanceQuery(conn)
            print(f"查询A股: {codes}")

        results = {}

        # 单季度数据
        if args.quarter:
            for code in codes:
                if args.cash:
                    df = query.get_quarterly_cashflow(code)
                    print_dataframe(df, f"{code} 单季度现金流量表（亿元）")
                    results[f"{code}_单季度现金流"] = df
                else:
                    df = query.get_quarterly_income(code)
                    print_dataframe(df, f"{code} 单季度利润表（亿元）")
                    results[f"{code}_单季度利润"] = df

        # 杜邦分析
        elif args.dupont:
            df = query.get_duPont_analysis(codes, args.years)
            print_duPont(df)
            results["杜邦分析"] = df

        # 标准财务报表
        else:
            if args.type == "balance":
                df = query.get_balance_sheet(codes, args.years)
                print_dataframe(df, "资产负债表（亿元）")
                results["资产负债表"] = df
            elif args.type == "income":
                df = query.get_income_sheet(codes, args.years)
                print_dataframe(df, "利润表（亿元）")
                results["利润表"] = df
            elif args.type == "cash":
                df = query.get_cash_sheet(codes, args.years)
                print_dataframe(df, "现金流量表（亿元）")
                results["现金流量表"] = df
            elif args.type == "index":
                df = query.get_main_index(codes, args.years)
                print_dataframe(df, "主要财务指标")
                results["主要财务指标"] = df
            elif args.type == "all":
                results = query.get_all_summary(codes, args.years)
                for name, df in results.items():
                    print_dataframe(df, f"{name}（亿元）" if name != "主要财务指标" else name)

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
