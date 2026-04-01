#!/usr/bin/env python3
"""
查询世纪华通(002602)财务数据
"""

import pymysql
import pandas as pd
import numpy as np
from datetime import datetime

# 数据库配置
DB_CONFIG = {
    'host': '10.65.69.253',
    'port': 3306,
    'user': 'ro_ciawind_yanjiuzu@tn_pro_ciawind#cl_p_ob4_sj',
    'password': 'Ro_Ci09a_Y6jz',
    'database': 'gildata',
    'charset': 'utf8mb4'
}

def get_company_code(conn, secu_code):
    """获取CompanyCode"""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT CompanyCode, SecuAbbr 
            FROM secumain 
            WHERE SecuCode=%s AND SecuCategory=1 
            LIMIT 1
        """, (secu_code,))
        r = cur.fetchone()
    return {'CompanyCode': r[0], 'Name': r[1]} if r else None

def query_financial_data(conn, company_code):
    """查询财务数据"""
    with conn.cursor() as cur:
        # 查询主要财务指标
        cur.execute("""
            SELECT 
                EndDate,
                TotalOperatingRevenuePS,
                OperatingRevenueGrowRate,
                NetProfit,
                NetProfitGrowRate,
                ROEAvg,
                ROEWeighted,
                GrossIncomeRatio,
                NetProfitRatio,
                BasicEPS,
                NetAssetPS,
                DebtAssetsRatio,
                CurrentRatio,
                NetOperateCashFlow,
                OperCashFlowPS
            FROM lc_mainindexnew
            WHERE CompanyCode = %s
            ORDER BY EndDate DESC
            LIMIT 20
        """, (company_code,))
        
        columns = [desc[0] for desc in cur.description]
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df

def query_income_statement(conn, company_code):
    """查询利润表"""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                EndDate,
                TotalOperatingRevenue,
                OperatingRevenue,
                TotalOperatingCost,
                OperatingCost,
                OperatingProfit,
                TotalProfit,
                NetProfit
            FROM lc_incomestatementall
            WHERE CompanyCode = %s
            ORDER BY EndDate DESC
            LIMIT 20
        """, (company_code,))
        
        columns = [desc[0] for desc in cur.description]
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df

def query_balance_sheet(conn, company_code):
    """查询资产负债表"""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                EndDate,
                TotalAssets,
                TotalLiability,
                TotalShareholderEquity,
                TotalCurrentAssets,
                TotalCurrentLiability
            FROM lc_balancesheetall
            WHERE CompanyCode = %s
            ORDER BY EndDate DESC
            LIMIT 20
        """, (company_code,))
        
        columns = [desc[0] for desc in cur.description]
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df

def query_cash_flow(conn, company_code):
    """查询现金流量表 - 简化版"""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                EndDate,
                NetOperateCashFlow
            FROM lc_cashflowstatementall
            WHERE CompanyCode = %s
            ORDER BY EndDate DESC
            LIMIT 20
        """, (company_code,))
        
        columns = [desc[0] for desc in cur.description]
        data = cur.fetchall()
        df = pd.DataFrame(data, columns=columns)
        return df

def main():
    conn = pymysql.connect(**DB_CONFIG)
    
    try:
        # 获取公司代码
        info = get_company_code(conn, '002602')
        if not info:
            print("未找到世纪华通(002602)")
            return
        
        print(f"公司: {info['Name']} (002602), CompanyCode={info['CompanyCode']}")
        print("\n" + "="*80)
        
        # 查询主要财务指标
        print("\n【主要财务指标】")
        df_main = query_financial_data(conn, info['CompanyCode'])
        print(df_main.to_string(index=False))
        
        # 查询利润表
        print("\n【利润表】")
        df_income = query_income_statement(conn, info['CompanyCode'])
        print(df_income.to_string(index=False))
        
        # 查询资产负债表
        print("\n【资产负债表】")
        df_balance = query_balance_sheet(conn, info['CompanyCode'])
        print(df_balance.to_string(index=False))
        
        # 查询现金流量表
        print("\n【现金流量表】")
        df_cash = query_cash_flow(conn, info['CompanyCode'])
        print(df_cash.to_string(index=False))
        
    finally:
        conn.close()

if __name__ == "__main__":
    main()
