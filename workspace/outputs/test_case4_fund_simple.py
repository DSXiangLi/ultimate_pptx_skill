#!/usr/bin/env python3
"""
测试用例4: 查询基金(008263)的基本信息和净值
简化版本
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


def get_fund_info(conn, fund_code: str):
    """获取基金信息"""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT InnerCode, SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=8 LIMIT 1",
            (fund_code,)
        )
        result = cur.fetchone()
    if result:
        return {"InnerCode": result[0], "Name": result[1], "Code": fund_code}
    return None


def query_fund_nav(conn, inner_code: int):
    """查询基金净值"""
    with conn.cursor() as cur:
        sql = """
        SELECT 
            EndDate,
            UnitNV
        FROM mf_netvalue
        WHERE InnerCode = %s 
        ORDER BY EndDate DESC
        LIMIT 10
        """
        cur.execute(sql, (inner_code,))
        rows = cur.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "日期": row[0],
                "单位净值": round(row[1], 4) if row[1] else None
            })
        return pd.DataFrame(data)


def main():
    print("=" * 60)
    print("测试用例4: 查询基金(008263)净值表现")
    print("=" * 60)
    
    config = load_config()
    conn = get_connection(config)
    
    try:
        # 获取基金信息
        fund = get_fund_info(conn, "008263")
        if not fund:
            print("未找到基金信息")
            return
        
        print(f"\n基金名称: {fund['Name']}")
        print(f"基金代码: {fund['Code']}")
        print(f"InnerCode: {fund['InnerCode']}")
        
        # 查询净值
        df = query_fund_nav(conn, fund['InnerCode'])
        
        if df.empty:
            print("未获取到数据")
            return
        
        print("\n" + "=" * 60)
        print("最近10个交易日净值:")
        print("=" * 60)
        print(df.to_string(index=False))
        
        # 保存到Excel
        output_path = Path(__file__).parent / "case4_result.xlsx"
        df.to_excel(output_path, index=False)
        print(f"\n数据已保存至: {output_path}")
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
