#!/usr/bin/env python3
"""
测试用例3: 对比白酒行业头部公司(茅台、五粮液、泸州老窖)的营收和净利润
"""

import os
import re
from pathlib import Path
from datetime import datetime, timedelta

import pymysql
import yaml
import pandas as pd

# ============ 配置加载 ============
def load_config(config_path: str = None) -> dict:
    if config_path is None:
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


def get_company_info(conn, secu_code: str):
    """获取公司信息"""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT CompanyCode, SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=1 LIMIT 1",
            (secu_code,)
        )
        result = cur.fetchone()
    if result:
        return {"CompanyCode": result[0], "Name": result[1], "Code": secu_code}
    return None


def query_revenue_profit(conn, company_code: int, years: int = 3):
    """查询营收和净利润"""
    with conn.cursor() as cur:
        sql = """
        SELECT 
            EndDate,
            TotalOperatingRevenue,
            NetProfit
        FROM lc_incomestatementall
        WHERE CompanyCode = %s 
        AND MONTH(EndDate) = 12
        AND IfAdjusted = 2
        AND IfMerged = 1
        ORDER BY EndDate DESC
        LIMIT %s
        """
        cur.execute(sql, (company_code, years))
        rows = cur.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "年度": row[0].year,
                "营收(亿元)": round(row[1] / 100000000, 2) if row[1] else None,
                "净利润(亿元)": round(row[2] / 100000000, 2) if row[2] else None
            })
        return pd.DataFrame(data)


def main():
    print("=" * 70)
    print("测试用例3: 对比白酒行业头部公司营收和净利润")
    print("=" * 70)
    
    # 白酒行业头部公司
    stocks = [
        ("600519", "贵州茅台"),
        ("000858", "五粮液"),
        ("000568", "泸州老窖")
    ]
    
    config = load_config()
    conn = get_connection(config)
    
    try:
        all_data = []
        
        for code, name in stocks:
            company = get_company_info(conn, code)
            if not company:
                print(f"未找到 {name}({code}) 的信息")
                continue
            
            df = query_revenue_profit(conn, company['CompanyCode'], years=3)
            if not df.empty:
                df = df.sort_values("年度")
                df["公司"] = name
                df["股票代码"] = code
                all_data.append(df)
        
        if not all_data:
            print("未获取到任何数据")
            return
        
        # 合并数据
        combined_df = pd.concat(all_data, ignore_index=True)
        
        # 重新排列列顺序
        combined_df = combined_df[["公司", "股票代码", "年度", "营收(亿元)", "净利润(亿元)"]]
        
        print("\n" + "=" * 70)
        print("查询结果:")
        print("=" * 70)
        print(combined_df.to_string(index=False))
        
        # 保存到Excel
        output_path = Path(__file__).parent / "case3_result.xlsx"
        combined_df.to_excel(output_path, index=False)
        print(f"\n数据已保存至: {output_path}")
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
