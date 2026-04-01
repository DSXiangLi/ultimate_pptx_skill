#!/usr/bin/env python3
"""
测试用例2: 查询沪深300指数(000300)的历史PE数据
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


def get_index_inner_code(conn, secu_code: str):
    """获取指数InnerCode"""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT InnerCode, SecuAbbr FROM secumain WHERE SecuCode=%s AND SecuCategory=4 LIMIT 1",
            (secu_code,)
        )
        result = cur.fetchone()
    if result:
        return {"InnerCode": result[0], "Name": result[1]}
    return None


def query_index_pe(conn, inner_code: int, months: int = 12):
    """查询指数PE历史数据"""
    with conn.cursor() as cur:
        sql = """
        SELECT 
            TradingDay,
            IndexPERatio1 as PE,
            IndexDYRatio1 as 股息率
        FROM qt_csiindexquote
        WHERE IndexCode = %s 
        AND TradingDay >= DATE_SUB(CURDATE(), INTERVAL %s MONTH)
        ORDER BY TradingDay DESC
        LIMIT 10
        """
        cur.execute(sql, (inner_code, months))
        rows = cur.fetchall()
        
        data = []
        for row in rows:
            data.append({
                "日期": row[0],
                "PE": round(row[1], 2) if row[1] else None,
                "股息率(%)": round(row[2], 2) if row[2] else None
            })
        return pd.DataFrame(data)


def main():
    print("=" * 60)
    print("测试用例2: 查询沪深300指数(000300)历史PE数据")
    print("=" * 60)
    
    config = load_config()
    conn = get_connection(config)
    
    try:
        # 获取指数信息
        index = get_index_inner_code(conn, "000300")
        if not index:
            print("未找到指数信息")
            return
        
        print(f"\n指数名称: {index['Name']}")
        print(f"InnerCode: {index['InnerCode']}")
        
        # 查询数据
        df = query_index_pe(conn, index['InnerCode'], months=12)
        
        if df.empty:
            print("未获取到数据")
            return
        
        print("\n" + "=" * 60)
        print("查询结果 (最近10个交易日):")
        print("=" * 60)
        print(df.to_string(index=False))
        
        # 保存到Excel
        output_path = Path(__file__).parent / "case2_result.xlsx"
        df.to_excel(output_path, index=False)
        print(f"\n数据已保存至: {output_path}")
        
    finally:
        conn.close()


if __name__ == "__main__":
    main()
