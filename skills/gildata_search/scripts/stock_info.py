#!/usr/bin/env python3
"""
股票公司基本信息查询
用法:
    python stock_info.py 600519              # 贵州茅台基本信息
    python stock_info.py 600519,000001       # 多股对比
    python stock_info.py 00700               # 港股

数据表:
  - LC_StockArchives (A股公司档案)
  - HK_CompanyArchives (港股公司档案)
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


# ============ A股公司信息查询 ============
class AShareInfoQuery:
    """A股公司基本信息查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_company_info(self, codes: List[str]) -> pd.DataFrame:
        """获取公司基本信息"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                arc.ChiName as 公司全称,
                DATE_FORMAT(arc.EstablishmentDate, '%Y-%m-%d') as 成立日期,
                arc.LegalRepr as 法人代表,
                arc.GeneralManager as 总经理,
                LEFT(arc.BriefIntroText, 200) as 公司简介,
                LEFT(arc.BusinessMajor, 200) as 主营业务,
                arc.RegAddr as 注册地址,
                arc.OfficeAddr as 办公地址,
                arc.Website as 公司网址,
                arc.ContactTel as 联系电话
            FROM SecuMain sm
            LEFT JOIN LC_StockArchives arc ON sm.CompanyCode = arc.CompanyCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
        """
        df = pd.read_sql(sql, self.conn)

        # 清理过长的文本，添加省略号
        for col in ['公司简介', '主营业务']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: str(x)[:150] + '...' if pd.notna(x) and len(str(x)) > 150 else x)

        return df

    def get_company_full(self, code: str) -> dict:
        """获取单个公司完整信息（用于详细展示）"""
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiNameAbbr as 股票简称,
                arc.ChiName as 公司全称,
                DATE_FORMAT(arc.EstablishmentDate, '%Y-%m-%d') as 成立日期,
                arc.LegalRepr as 法人代表,
                arc.GeneralManager as 总经理,
                arc.SecretaryBD as 董秘,
                arc.BriefIntroText as 公司简介,
                arc.BusinessMajor as 主营业务,
                ep.BusinessMajor as 经营范围,
                arc.RegAddr as 注册地址,
                arc.OfficeAddr as 办公地址,
                arc.Website as 公司网址,
                arc.ContactTel as 联系电话,
                arc.Email as 邮箱
            FROM SecuMain sm
            LEFT JOIN LC_StockArchives arc ON sm.CompanyCode = arc.CompanyCode
            LEFT JOIN ep_companyinfo ep ON sm.CompanyCode = ep.CompanyCode
            WHERE sm.SecuCode = '{code}'
            AND sm.SecuCategory = 1
            AND sm.SecuMarket IN (18, 83, 90)
            LIMIT 1
        """
        df = pd.read_sql(sql, self.conn)
        if df.empty:
            return {}
        return df.iloc[0].to_dict()


# ============ 港股公司信息查询 ============
class HKShareInfoQuery:
    """港股公司基本信息查询"""

    def __init__(self, conn: pymysql.Connection):
        self.conn = conn

    def get_company_info(self, codes: List[str]) -> pd.DataFrame:
        """获取港股公司基本信息"""
        codes_str = format_codes(codes)
        sql = f"""
            SELECT
                sm.SecuCode as 股票代码,
                sm.ChiName as 股票简称,
                arc.ChiName as 公司全称,
                DATE_FORMAT(arc.EstablishmentDate, '%Y-%m-%d') as 成立日期,
                arc.Chairman as 董事长,
                LEFT(arc.BriefIntroText, 200) as 公司简介,
                LEFT(arc.MainBusiness, 200) as 主营业务,
                arc.RegAddr as 注册地址,
                arc.HKOffice as 办公地址,
                arc.Website as 公司网址
            FROM HK_SecuMain sm
            LEFT JOIN HK_CompanyArchives arc ON sm.CompanyCode = arc.CompanyCode
            WHERE sm.SecuCode IN {codes_str}
            AND sm.SecuMarket = 72
            AND sm.SecuCategory IN (3, 51, 53, 78)
        """
        df = pd.read_sql(sql, self.conn)

        for col in ['公司简介', '主营业务']:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: str(x)[:150] + '...' if pd.notna(x) and len(str(x)) > 150 else x)

        return df


# ============ 输出格式化 ============
def print_company_table(df: pd.DataFrame):
    """打印公司信息表格"""
    if df.empty:
        print("*无数据*")
        return

    # 选择显示的列（A股和港股略有不同）
    cols = ['股票代码', '股票简称', '公司全称', '法人代表', '总经理', '董事长', '成立日期']
    cols = [c for c in cols if c in df.columns]
    df_show = df[cols].copy()

    # 打印Markdown表格
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join(["---"] * len(cols)) + "|")

    for _, row in df_show.iterrows():
        values = []
        for col in cols:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            else:
                values.append(str(val).replace('\n', ' ')[:30])
        print("| " + " | ".join(values) + " |")


def print_company_detail(info: dict):
    """打印单个公司详细信息"""
    if not info:
        print("*无数据*")
        return

    print("\n" + "=" * 50)
    print(f"【{info.get('股票简称', '')}】{info.get('股票代码', '')}")
    print("=" * 50)

    # 基本信息
    basic_fields = [
        ('公司全称', '公司全称'),
        ('成立日期', '成立日期'),
        ('法人代表', '法人代表'),
        ('总经理', '总经理'),
        ('董秘', '董秘'),
    ]

    print("\n## 基本信息")
    for label, key in basic_fields:
        val = info.get(key)
        if pd.notna(val) and val:
            print(f"  {label}: {val}")

    # 联系方式
    contact_fields = [
        ('注册地址', '注册地址'),
        ('办公地址', '办公地址'),
        ('公司网址', '公司网址'),
        ('联系电话', '联系电话'),
        ('邮箱', '邮箱'),
    ]

    print("\n## 联系方式")
    for label, key in contact_fields:
        val = info.get(key)
        if pd.notna(val) and val:
            print(f"  {label}: {val}")

    # 公司简介
    intro = info.get('公司简介')
    if pd.notna(intro) and intro:
        print("\n## 公司简介")
        print(f"  {str(intro).replace(chr(10), ' ')}")

    # 主营业务
    business = info.get('主营业务')
    if pd.notna(business) and business:
        print("\n## 主营业务")
        print(f"  {str(business).replace(chr(10), ' ')}")

    # 经营范围
    scope = info.get('经营范围')
    if pd.notna(scope) and scope:
        print("\n## 经营范围")
        print(f"  {str(scope).replace(chr(10), ' ')}")

    print("\n" + "=" * 50)


# ============ 主函数 ============
def main():
    parser = argparse.ArgumentParser(
        description="股票公司基本信息查询",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s 600519                    # 贵州茅台基本信息
  %(prog)s 600519,000001             # 多股对比
  %(prog)s 00700                     # 港股腾讯
  %(prog)s 600519 --full             # 详细信息
        """
    )
    parser.add_argument("codes", help="股票代码，多个用逗号分隔")
    parser.add_argument("--full", "-f", action="store_true", help="显示完整详细信息")
    parser.add_argument("--config", "-c", help="配置文件路径")

    args = parser.parse_args()
    codes = [c.strip() for c in args.codes.split(",")]

    config = load_config(args.config)
    conn = get_connection(config)

    try:
        # 分离A股和港股
        a_codes = [c for c in codes if not is_hk_stock(c)]
        hk_codes = [c for c in codes if is_hk_stock(c)]

        if args.full:
            # 详细信息模式（支持A股港股混合）
            for code in codes:
                if is_hk_stock(code):
                    query = HKShareInfoQuery(conn)
                    df_temp = query.get_company_info([code])
                    info = df_temp.iloc[0].to_dict() if not df_temp.empty else {}
                else:
                    query = AShareInfoQuery(conn)
                    info = query.get_company_full(code)
                print_company_detail(info)
        else:
            # 表格形式（支持A股港股混合）
            all_dfs = []
            if a_codes:
                query_a = AShareInfoQuery(conn)
                df_a = query_a.get_company_info(a_codes)
                if not df_a.empty:
                    all_dfs.append(df_a)
            if hk_codes:
                query_hk = HKShareInfoQuery(conn)
                df_hk = query_hk.get_company_info(hk_codes)
                if not df_hk.empty:
                    all_dfs.append(df_hk)

            if all_dfs:
                import pandas as pd
                df = pd.concat(all_dfs, ignore_index=True)
                # 按原始顺序排列
                df['sort_key'] = df['股票代码'].apply(lambda x: codes.index(x) if x in codes else 999)
                df = df.sort_values('sort_key').drop('sort_key', axis=1)
                print()
                print_company_table(df)

    finally:
        conn.close()


if __name__ == "__main__":
    main()
