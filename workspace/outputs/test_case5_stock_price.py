#!/usr/bin/env python3
"""
测试用例5: 查询宁德时代(300750)最近30个交易日的行情数据
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


def get_stock_info(conn, secu_code: str):
    """获取股票信息"""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT InnerCode, SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=1 LIMIT 1",
            (secu_code,)
        )
        result = cur.fetchone()
    if result:
        return {"InnerCode": result[0], "Name": result[1], "Code": secu_code}
    return None


def query_stock_performance(conn, inner_code: int, days: int = 30):
    """查询股票行情表现"""
    with conn.cursor() as cur:
        sql = """
        SELECT 
            TradingDay,
            ClosePrice,
            TurnoverRate,
            ChangePCT
        FROM qt_stockperformance
        WHERE InnerCode = %s 
        ORDER BY TradingDay DESC
        LIMIT %s
        """
        cur.execute(sql, (inner_code, days))
        rows = cur.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "日期": row[0],
                "收盘价": round(row[1], 2) if row[1] else None,
                "换手率(%)": round(row[2], 2) if row[2] else None,
                "涨跌幅(%)": round(row[3], 2) if row[3] else None
            })
        return pd.DataFrame(data)


def main():
    print("=" * 60)
    print("测试用例5: 查询宁德时代(300750)最近30日行情")
    print("=" * 60)
    
    config = load_config()
    conn = get_connection(config)
    
    try:
        # 获取股票信息
        stock = get_stock_info(conn, "300750")
        if not stock:
            print("未找到股票信息")
            return
        
        print(f"\n股票名称: {stock['Name']}")
        print(f"股票代码: {stock['Code']}")
        print(f"InnerCode: {stock['InnerCode']}")
        
        # 查询行情
        df = query_stock_performance(conn, stock['InnerCode'], days=30)
        
        if df.empty:
            print("未获取到数据")
            return
        
        print("\n" + "=" * 60)
        print("最近10个交易日行情:")
        print("=" * 60)
        print(df.head(10).to_string(index=False))
        
        # 保存到Excel
        output_path = Path(__file__).parent / "case5_result.xlsx"
        df.to_excel(output_path, index=False)
        print(f"\n数据已保存至: {output_path}")
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
