#!/usr/bin/env python3
"""
查询世纪华通(002602)财务数据
"""

import pymysql
import yaml
import pandas as pd
from pathlib import Path
import re

def load_config():
    """加载配置文件"""
    config_path = Path(__file__).parent / 'skills/gildata_query/config/config.yaml'
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def parse_env(value):
    """解析 ${VAR:-default} 格式"""
    if not isinstance(value, str): return value
    m = re.search(r'\$\{[^:]+:-([^}]+)\}', value)
    return m.group(1) if m else value

def get_conn(config):
    """获取数据库连接"""
    m = config['mysql']
    return pymysql.connect(
        host=parse_env(m['host']), port=m.get('port', 3306),
        user=parse_env(m['user']), password=parse_env(m['password']),
        database=parse_env(m['database']), charset='utf8mb4'
    )

def get_company_code(conn, secu_code):
    """获取公司代码"""
    with conn.cursor() as cur:
        cur.execute("SELECT CompanyCode, SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=1 LIMIT 1", (secu_code,))
        r = cur.fetchone()
    return {'CompanyCode': r[0], 'Name': r[1]} if r else None

def query_financial_data(conn, company_code):
    """查询财务数据"""
    
    # 查询主要财务指标
    sql_main = """
    SELECT 
        EndDate,
        BasicEPS,
        EPSTTM,
        NetAssetPS,
        ROEAvg,
        ROEWeighted,
        GrossIncomeRatio,
        NetProfitRatio,
        DebtAssetsRatio,
        NetOperateCashFlow,
        OperatingRevenueGrowRate,
        NetProfitGrowRate,
        NPParentCompanyYOY,
        TotalOperatingRevenuePS,
        OperatingExpenseRate,
        AdminiExpenseRate,
        FinancialExpenseRate
    FROM lc_mainindexnew 
    WHERE CompanyCode = %s 
    AND EndDate >= '2022-12-31'
    ORDER BY EndDate DESC
    LIMIT 20
    """
    
    # 查询利润表
    sql_income = """
    SELECT 
        EndDate,
        TotalOperatingRevenue,
        OperatingRevenue,
        OperatingCost,
        OperatingProfit,
        TotalProfit,
        NetProfit,
        NPParentCompanyOwners,
        OperatingExpense,
        TotalAdminExpense,
        RAndD,
        FinancialExpense
    FROM lc_incomestatementall 
    WHERE CompanyCode = %s 
    AND IfMerged = 1
    AND IfAdjusted = 2
    AND EndDate >= '2022-12-31'
    ORDER BY EndDate DESC
    LIMIT 20
    """
    
    # 查询资产负债表
    sql_balance = """
    SELECT 
        EndDate,
        TotalAssets,
        TotalCurrentAssets,
        TotalNonCurrentAssets,
        TotalLiability,
        TotalCurrentLiability,
        TotalNonCurrentLiability,
        SEWithoutMI,
        TotalShareholderEquity,
        CashEquivalents,
        GoodWill
    FROM lc_balancesheetall 
    WHERE CompanyCode = %s 
    AND IfMerged = 1
    AND IfAdjusted = 2
    AND EndDate >= '2022-12-31'
    ORDER BY EndDate DESC
    LIMIT 20
    """
    
    with conn.cursor() as cur:
        cur.execute(sql_main, (company_code,))
        main_data = cur.fetchall()
        
        cur.execute(sql_income, (company_code,))
        income_data = cur.fetchall()
        
        cur.execute(sql_balance, (company_code,))
        balance_data = cur.fetchall()
    
    return main_data, income_data, balance_data

def main():
    config = load_config()
    conn = get_conn(config)
    
    try:
        # 获取世纪华通公司代码
        company_info = get_company_code(conn, '002602')
        if not company_info:
            print("未找到世纪华通(002602)的公司代码")
            return
        
        print(f"公司: {company_info['Name']} (002602), CompanyCode={company_info['CompanyCode']}")
        
        # 查询财务数据
        main_data, income_data, balance_data = query_financial_data(conn, company_info['CompanyCode'])
        
        # 打印主要财务指标
        print("\n=== 主要财务指标 ===")
        columns_main = ['EndDate', 'BasicEPS', 'EPSTTM', 'NetAssetPS', 'ROEAvg', 'ROEWeighted', 
                       'GrossIncomeRatio', 'NetProfitRatio', 'DebtAssetsRatio', 'NetOperateCashFlow',
                       'OperatingRevenueGrowRate', 'NetProfitGrowRate', 'NPParentCompanyYOY',
                       'TotalOperatingRevenuePS', 'OperatingExpenseRate', 'AdminiExpenseRate', 'FinancialExpenseRate']
        df_main = pd.DataFrame(main_data, columns=columns_main)
        print(df_main.to_string(index=False))
        
        # 打印利润表数据
        print("\n=== 利润表数据(亿元) ===")
        columns_income = ['EndDate', 'TotalOperatingRevenue', 'OperatingRevenue', 'OperatingCost',
                         'OperatingProfit', 'TotalProfit', 'NetProfit', 'NPParentCompanyOwners',
                         'OperatingExpense', 'TotalAdminExpense', 'RAndD', 'FinancialExpense']
        df_income = pd.DataFrame(income_data, columns=columns_income)
        # 转换为亿元
        for col in columns_income[1:]:
            df_income[col] = df_income[col] / 100000000
        print(df_income.to_string(index=False))
        
        # 打印资产负债表数据
        print("\n=== 资产负债表数据(亿元) ===")
        columns_balance = ['EndDate', 'TotalAssets', 'TotalCurrentAssets', 'TotalNonCurrentAssets',
                          'TotalLiability', 'TotalCurrentLiability', 'TotalNonCurrentLiability',
                          'SEWithoutMI', 'TotalShareholderEquity', 'CashEquivalents', 'GoodWill']
        df_balance = pd.DataFrame(balance_data, columns=columns_balance)
        # 转换为亿元
        for col in columns_balance[1:]:
            df_balance[col] = df_balance[col] / 100000000
        print(df_balance.to_string(index=False))
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()
