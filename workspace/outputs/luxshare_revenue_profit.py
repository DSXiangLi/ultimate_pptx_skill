#!/usr/bin/env python3
"""
查询立讯精密(002475)最近三年营收及净利润数据并绘制柱状图
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import pymysql
import yaml
import matplotlib.pyplot as plt
from matplotlib import font_manager

# ============ 中文字体设置 ============
def setup_chinese_font():
    """自动检测系统中可用的中文字体"""
    chinese_fonts = ['Noto Sans CJK SC', 'Noto Sans CJK JP', 'SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
    available = [f.name for f in font_manager.fontManager.ttflist]
    for font in chinese_fonts:
        if font in available:
            plt.rcParams['font.sans-serif'] = [font]
            plt.rcParams['axes.unicode_minus'] = False
            return font
    # 模糊匹配
    for f in font_manager.fontManager.ttflist:
        if any(k in f.name.lower() for k in ['cjk', 'chinese', 'noto sans', 'source han']):
            plt.rcParams['font.sans-serif'] = [f.name]
            plt.rcParams['axes.unicode_minus'] = False
            return f.name
    return None

font_name = setup_chinese_font()
print(f"使用字体: {font_name}")

# ============ 配置加载 ============
def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).parent.parent / "skills" / "gildata_search" / "config" / "config.yaml"
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


def get_company_info(conn: pymysql.Connection, code: str) -> Optional[dict]:
    """获取公司信息"""
    with conn.cursor() as cur:
        cur.execute("""
            SELECT CompanyCode, InnerCode, SecuAbbr 
            FROM secumain 
            WHERE SecuCode = %s AND SecuCategory = 1
        """, (code,))
        row = cur.fetchone()
        if row:
            return {
                "CompanyCode": row[0],
                "InnerCode": row[1],
                "CompanyName": row[2] if row[2] else "立讯精密"
            }
    return None


def get_financial_data(conn: pymysql.Connection, company_code: int, years: int = 3) -> pd.DataFrame:
    """获取财务数据（营收和净利润）"""
    # 查询LC_MainIndexNew表，获取主要财务指标
    with conn.cursor() as cur:
        cur.execute("""
            SELECT 
                EndDate,
                TotalOperatingRevenue,
                NetProfit
            FROM lc_mainindexnew
            WHERE CompanyCode = %s 
            AND EndDate >= DATE_SUB(CURDATE(), INTERVAL %s YEAR)
            AND (MONTH(EndDate) = 12 OR MONTH(EndDate) = 6 OR MONTH(EndDate) = 9 OR MONTH(EndDate) = 3)
            ORDER BY EndDate DESC
        """, (company_code, years + 1))
        
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append({
                "报告期": row[0],
                "营业总收入(亿元)": round(row[1] / 100000000, 2) if row[1] else None,
                "净利润(亿元)": round(row[2] / 100000000, 2) if row[2] else None
            })
        
        return pd.DataFrame(data)


def get_annual_data(conn: pymysql.Connection, company_code: int, years: int = 3) -> pd.DataFrame:
    """获取年度财务数据 - 使用利润表LC_IncomeStatementAll"""
    with conn.cursor() as cur:
        # 查询利润表获取营业收入和净利润
        cur.execute("""
            SELECT 
                a.EndDate,
                a.TotalOperatingRevenue,
                a.NetProfit
            FROM lc_incomestatementall a
            WHERE a.CompanyCode = %s 
            AND MONTH(a.EndDate) = 12
            AND a.IfAdjusted = 2
            AND a.IfMerged = 1
            ORDER BY a.EndDate DESC
            LIMIT %s
        """, (company_code, years))
        
        rows = cur.fetchall()
        data = []
        for row in rows:
            data.append({
                "年度": row[0].year,
                "营业总收入(亿元)": round(row[1] / 100000000, 2) if row[1] else None,
                "净利润(亿元)": round(row[2] / 100000000, 2) if row[2] else None
            })
        
        return pd.DataFrame(data)


def plot_revenue_profit(df: pd.DataFrame, company_name: str, output_path: str):
    """绘制营收和净利润柱状图"""
    # 按年度升序排列
    df = df.sort_values("年度")
    
    years = df["年度"].astype(str).tolist()
    revenue = df["营业总收入(亿元)"].tolist()
    profit = df["净利润(亿元)"].tolist()
    
    x = np.arange(len(years))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    bars1 = ax.bar(x - width/2, revenue, width, label='营业总收入', color='#4472C4', edgecolor='white', linewidth=0.5)
    bars2 = ax.bar(x + width/2, profit, width, label='净利润', color='#ED7D31', edgecolor='white', linewidth=0.5)
    
    # 添加数值标签
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    for bar in bars2:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('年度', fontsize=12)
    ax.set_ylabel('金额（亿元）', fontsize=12)
    ax.set_title(f'{company_name}（002475）营收与净利润', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.legend(loc='upper left', fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # 添加数据来源
    fig.text(0.99, 0.01, '数据来源：恒生聚源', ha='right', fontsize=9, color='gray')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    print(f"图表已保存至: {output_path}")
    
    return fig, ax


def main():
    # 加载配置
    config = load_config()
    conn = get_connection(config)
    
    try:
        # 获取立讯精密公司信息
        company_info = get_company_info(conn, "002475")
        if not company_info:
            print("未找到立讯精密(002475)的公司信息")
            return
        
        print(f"公司名称: {company_info['CompanyName']}")
        print(f"公司代码: {company_info['CompanyCode']}")
        
        # 获取最近三年年度财务数据
        df = get_annual_data(conn, company_info['CompanyCode'], years=3)
        
        if df.empty:
            print("未获取到财务数据")
            return
        
        print("\n=== 立讯精密最近三年财务数据 ===")
        print(df.to_string(index=False))
        
        # 保存数据到Excel
        excel_path = Path(__file__).parent / "luxshare_finance_data.xlsx"
        df.to_excel(excel_path, index=False)
        print(f"\n数据已保存至: {excel_path}")
        
        # 绘制柱状图
        output_path = Path(__file__).parent / "luxshare_revenue_profit_chart.png"
        plot_revenue_profit(df, company_info['CompanyName'], str(output_path))
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
