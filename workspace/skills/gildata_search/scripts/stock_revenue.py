#!/usr/bin/env python3
"""
股票主营业务分项目收入查询
用法:
    python stock_revenue.py 600519                    # 贵州茅台主营业务收入
    python stock_revenue.py 600519 --year 2024        # 指定年份
    python stock_revenue.py 600519,000858             # 多股对比
    python stock_revenue.py 600519 --top 5            # 只看前5个项目

数据表:
  - LC_MainOperIncome (A股主营业务分产品/分行业收入)

数据口径说明:
  - 数据来源: 恒生聚源数据库 (Gildata)
  - 表名: LC_MainOperIncome (上市公司主营业务收入表)
  - 披露频率: 年报、半年报、季报
  - 口径: 合并报表 (IfMerged=1)
  - 单位: 元 (输出时转换为亿元)
  - 字段说明:
    * MainOperIncome: 当期主营业务收入
    * MainOperIncomeFormerYear: 上年同期主营业务收入
    * MainIncomeGrowRateYOY: 主营业务收入同比增长率
    * GrossProfit: 毛利率
    * Project: 经营项目名称
    * ParentName: 上级科目名称
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

from pathlib import Path
from typing import List
from decimal import Decimal

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
    """判断是否港股（5位数字）"""
    return len(code) == 5 and code.isdigit()

def format_codes(codes: List[str]) -> str:
    return "(" + ", ".join(f"'{c}'" for c in codes) + ")"

# ============ A股主营业务收入查询 ============
class AShareRevenueQuery:
    """A股主营业务分项目收入查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_revenue_by_project(self, codes: List[str], year: int = None, top_n: int = None) -> pd.DataFrame:
        """
        获取主营业务分项目收入

        返回字段:
        - 个股名称、截止日期、信息来源、经营项目名称、上级科目名称
        - 当年主营业务收入(元)、上年同期主营业务收入(元)、主营业务收入同比(%)
        - 毛利率(%)
        """
        codes_str = format_codes(codes)

        year_filter = f"AND YEAR(arc.EndDate) >= {year}" if year else "AND arc.EndDate >= DATE_SUB(NOW(), INTERVAL 2 YEAR)"
        limit_clause = f"LIMIT {top_n * len(codes)}" if top_n else ""

        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 个股名称,
                DATE_FORMAT(arc.EndDate, '%Y-%m-%d') as 截止日期,
                arc.InfoSource as 信息来源,
                arc.Project as 经营项目名称,
                arc.ParentName as 上级科目名称,
                arc.MainOperIncome as 当年主营业务收入,
                arc.MainOperIncomeFormerYear as 上年同期主营业务收入,
                arc.MainIncomeGrowRateYOY as 主营业务收入同比,
                arc.GrossProfit as 毛利率,
                arc.MainOperCost as 主营业务成本,
                arc.MainOperProfit as 主营业务利润
            FROM SecuMain sm
            JOIN LC_MainOperIncome arc ON sm.CompanyCode = arc.CompanyCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90, 81)
            AND arc.IfMerged = 1
            {year_filter}
            ORDER BY sm.SecuCode, arc.EndDate DESC, arc.MainOperIncome DESC
            {limit_clause}
        """
        df = pd.read_sql(sql, self.conn)

        # 数据类型转换 - 注意处理 Decimal 和 str 类型
        if not df.empty:
            # 转换收入为亿元 (MainOperIncome 可能是 str 或 Decimal)
            df['当年主营业务收入_亿'] = df['当年主营业务收入'].apply(
                lambda x: float(Decimal(str(x)))/1e8 if pd.notna(x) else None
            )
            df['上年同期主营业务收入_亿'] = df['上年同期主营业务收入'].apply(
                lambda x: float(Decimal(str(x)))/1e8 if pd.notna(x) else None
            )
            # 毛利率已经是小数形式，转换为百分比 (GrossProfit 是 Decimal)
            df['毛利率_百分比'] = df['毛利率'].apply(
                lambda x: float(Decimal(str(x)))*100 if pd.notna(x) else None
            )
            # 同比字段也是小数形式，需要乘以100转换为百分比
            df['主营业务收入同比_百分比'] = df['主营业务收入同比'].apply(
                lambda x: float(Decimal(str(x)))*100 if pd.notna(x) else None
            )

        return df

# ============ 输出格式化 ============
def print_revenue_table(df: pd.DataFrame, top_n: int = None):
    """打印主营业务收入表格"""
    if df.empty:
        print("*无数据*")
        return

    # 按股票分组，每组取前N个
    if top_n:
        df = df.groupby('个股名称').head(top_n).reset_index(drop=True)

    print("\n### 主营业务分项目收入（亿元）\n")

    # 表头
    cols = ['个股名称', '截止日期', '信息来源', '经营项目名称', '当年主营业务收入_亿',
            '上年同期主营业务收入_亿', '主营业务收入同比_百分比', '毛利率_百分比']
    cols = [c for c in cols if c in df.columns]

    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    # 数据行
    for _, row in df.iterrows():
        values = []
        for col in cols:
            val = row.get(col)
            if pd.isna(val):
                values.append("-")
            elif '收入_亿' in col:
                values.append(f"{val:.2f}")
            elif '百分比' in col or '毛利率' in col:
                values.append(f"{val:.1f}%")
            elif col == '经营项目名称' or col == '信息来源':
                values.append(str(val)[:15] if val else "-")
            else:
                values.append(str(val) if val else "-")
        print("| " + " | ".join(values) + " |")

def print_revenue_detail(df: pd.DataFrame, code: str):
    """打印单个公司的详细收入信息 - 完整字段版"""
    company_df = df[df['个股名称'].notna()].copy()
    if company_df.empty:
        print("*无数据*")
        return

    # 取最新报告期
    latest_date = company_df['截止日期'].max()
    latest_df = company_df[company_df['截止日期'] == latest_date]

    # 按收入排序
    latest_df = latest_df.sort_values('当年主营业务收入_亿', ascending=False)

    # 定义输出列
    cols = ['个股名称', '截止日期', '信息来源', '经营项目名称', '上级科目名称',
            '当年主营业务收入_亿', '上年同期主营业务收入_亿', '主营业务收入同比_百分比', '毛利率_百分比']

    print(f"\n{'='*100}")
    print(f"【主营业务分项目收入】")
    print(f"{'='*100}\n")

    # 表头
    headers = ['个股名称', '截止日期', '信息来源', '经营项目名称', '上级科目名称',
               '当年主营业务收入(亿)', '上年同期主营业务收入(亿)', '主营业务收入同比(%)', '毛利率(%)']
    print("| " + " | ".join(headers) + " |")
    print("|" + "|".join(["---"] * len(headers)) + "|")

    # 数据行
    for _, row in latest_df.iterrows():
        values = []

        # 个股名称
        values.append(str(row['个股名称']) if pd.notna(row['个股名称']) else "-")

        # 截止日期
        values.append(str(row['截止日期']) if pd.notna(row['截止日期']) else "-")

        # 信息来源
        source = str(row['信息来源'])[:10] if pd.notna(row['信息来源']) else "-"
        values.append(source)

        # 经营项目名称
        project = str(row['经营项目名称'])[:15] if pd.notna(row['经营项目名称']) else "-"
        values.append(project)

        # 上级科目名称
        parent = str(row['上级科目名称'])[:10] if pd.notna(row['上级科目名称']) else "-"
        values.append(parent)

        # 当年主营业务收入(亿)
        if pd.notna(row['当年主营业务收入_亿']):
            values.append(f"{row['当年主营业务收入_亿']:.2f}")
        else:
            values.append("-")

        # 上年同期主营业务收入(亿)
        if pd.notna(row['上年同期主营业务收入_亿']):
            values.append(f"{row['上年同期主营业务收入_亿']:.2f}")
        else:
            values.append("-")

        # 主营业务收入同比(%)
        if pd.notna(row['主营业务收入同比_百分比']):
            values.append(f"{row['主营业务收入同比_百分比']:.1f}")
        else:
            values.append("-")

        # 毛利率(%)
        if pd.notna(row['毛利率_百分比']):
            values.append(f"{row['毛利率_百分比']:.1f}")
        else:
            values.append("-")

        print("| " + " | ".join(values) + " |")

    print()
    print("*数据来源: 恒生聚源 LC_MainOperIncome 表，合并报表口径")

# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票主营业务分项目收入查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 600519                    # 贵州茅台主营业务收入
  %(prog)s 600519 --year 2024        # 指定年份
  %(prog)s 600519,000858             # 多股对比
  %(prog)s 600519 --top 5            # 只看前5个项目
  %(prog)s 600519 --detail           # 详细格式

数据口径:
  - 数据来源: 恒生聚源数据库 LC_MainOperIncome 表
  - 口径: 合并报表 (IfMerged=1)
  - 单位: 元 (输出转换为亿元)
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--year", "-y", type=int, help="指定年份，默认近2年")
    parser.add_argument("--top", "-n", type=int, default=10, help="每个公司显示前N个项目，默认10")
    parser.add_argument("--detail", "-d", action="store_true", help="详细格式输出")
    parser.add_argument("--config", "-c", help="配置文件路径")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        # 判断是否港股
        hk_codes = [c for c in codes if is_hk_stock(c)]
        a_codes = [c for c in codes if not is_hk_stock(c)]

        if hk_codes:
            print(f"提示: 港股 {hk_codes} 暂不支持主营业务分项目查询")
            codes = a_codes
            if not codes:
                return

        print(f"查询A股: {codes}")

        query = AShareRevenueQuery(conn)
        df = query.get_revenue_by_project(codes, args.year, args.top * 2)

        if args.detail and len(codes) == 1:
            print_revenue_detail(df, codes[0])
        else:
            print_revenue_table(df, args.top)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
