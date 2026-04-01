#!/usr/bin/env python3
"""
测试用例1: 查询贵州茅台(600519)最近5年的ROE和毛利率
对比 gildata_query vs gildata_search 的执行方式
"""

import os
import re
from pathlib import Path
from datetime import datetime, timedelta

import pymysql
import yaml
import pandas as pd
import numpy as np

# ============ 配置加载 ============
def load_config(config_path: str = None) -> dict:
    if config_path is None:
        # 尝试两个技能目录
        for skill_dir in ['gildata_search', 'gildata_query']:
            config_path = Path(__file__).parent.parent / "skills" / skill_dir / "config" / "config.yaml"
            if config_path.exists():
                break
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_env(value: str) -> str:
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


def get_company_code(conn, secu_code: str):
    """获取公司代码"""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT CompanyCode, SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=1 LIMIT 1",
            (secu_code,)
        )
        result = cur.fetchone()
    if result:
        return {"CompanyCode": result[0], "Name": result[1]}
    return None


def query_roe_grossmargin(conn, company_code: int, years: int = 5):
    """查询ROE和毛利率"""
    with conn.cursor() as cur:
        sql = """
        SELECT 
            EndDate,
            ROEAvg,
            GrossIncomeRatio
        FROM lc_mainindexnew
        WHERE CompanyCode = %s 
        AND MONTH(EndDate) = 12
        ORDER BY EndDate DESC
        LIMIT %s
        """
        cur.execute(sql, (company_code, years))
        rows = cur.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "年度": row[0].year,
                "ROE(%)": round(row[1] * 100, 2) if row[1] else None,
                "毛利率(%)": round(row[2] * 100, 2) if row[2] else None
            })
        return pd.DataFrame(data)


def main():
    print("=" * 60)
    print("测试用例1: 查询贵州茅台(600519)最近5年ROE和毛利率")
    print("=" * 60)
    
    config = load_config()
    conn = get_connection(config)
    
    try:
        # 获取公司信息
        company = get_company_code(conn, "600519")
        if not company:
            print("未找到公司信息")
            return
        
        print(f"\n公司名称: {company['Name']}")
        print(f"公司代码: {company['CompanyCode']}")
        
        # 查询数据
        df = query_roe_grossmargin(conn, company['CompanyCode'], years=5)
        
        if df.empty:
            print("未获取到数据")
            return
        
        # 按年度升序排列
        df = df.sort_values("年度")
        
        print("\n" + "=" * 60)
        print("查询结果:")
        print("=" * 60)
        print(df.to_string(index=False))
        
        # 保存到Excel
        output_path = Path(__file__).parent / "case1_result.xlsx"
        df.to_excel(output_path, index=False)
        print(f"\n数据已保存至: {output_path}")
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
