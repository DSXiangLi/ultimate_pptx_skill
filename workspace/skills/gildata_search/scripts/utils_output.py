#!/usr/bin/env python3
"""
统一输出格式化工具
- Markdown 表格格式
- 合理的精度控制
- 简洁可控的输出
"""

import pandas as pd
from typing import Optional, List


def format_markdown_table(df: pd.DataFrame, 
                          title: str = None,
                          max_rows: int = 10,
                          float_format: str = "{:.2f}",
                          int_cols: List[str] = None) -> str:
    """
    将DataFrame格式化为Markdown表格
    
    Args:
        df: 数据框
        title: 标题
        max_rows: 最大行数
        float_format: 浮点数格式
        int_cols: 整数列名列表
    """
    if df.empty:
        return f"**{title}**: 无数据" if title else "无数据"
    
    # 限制行数
    if len(df) > max_rows:
        df_display = df.head(max_rows)
        truncated = f"\n*...共 {len(df)} 条，显示前 {max_rows} 条*"
    else:
        df_display = df
        truncated = ""
    
    # 格式化
    result = []
    if title:
        result.append(f"### {title}")
    result.append("")
    
    # 表头
    headers = list(df_display.columns)
    result.append("| " + " | ".join(str(h) for h in headers) + " |")
    result.append("|" + "|".join(["---"] * len(headers)) + "|")
    
    # 数据行
    for _, row in df_display.iterrows():
        values = []
        for col in headers:
            val = row[col]
            if pd.isna(val):
                values.append("-")
            elif int_cols and col in int_cols:
                values.append(f"{int(val):,}")
            elif isinstance(val, float):
                # 智能精度：大数用亿，小数保留合理精度
                if abs(val) >= 1e8:
                    values.append(f"{val/1e8:.2f}亿")
                elif abs(val) >= 1e4:
                    values.append(f"{val/1e4:.2f}万")
                elif abs(val) < 0.01 and val != 0:
                    values.append(f"{val:.4f}")
                else:
                    values.append(float_format.format(val))
            elif hasattr(val, 'strftime'):
                values.append(val.strftime('%Y-%m-%d'))
            else:
                values.append(str(val))
        result.append("| " + " | ".join(values) + " |")
    
    result.append(truncated)
    return "\n".join(result)


def format_currency(value: float, unit: str = "元") -> str:
    """智能货币格式化"""
    if pd.isna(value):
        return "-"
    if abs(value) >= 1e8:
        return f"{value/1e8:.2f}亿{unit}"
    elif abs(value) >= 1e4:
        return f"{value/1e4:.2f}万{unit}"
    else:
        return f"{value:.2f}{unit}"


def format_percent(value: float) -> str:
    """百分比格式化"""
    if pd.isna(value):
        return "-"
    return f"{value:.2f}%"


def format_number(value: float, decimals: int = 2) -> str:
    """数字格式化，带千分位"""
    if pd.isna(value):
        return "-"
    return f"{value:,.{decimals}f}"


def print_summary(title: str, items: dict):
    """打印键值对摘要"""
    print(f"\n### {title}")
    print()
    for key, value in items.items():
        print(f"- **{key}**: {value}")


# 预定义的列格式化规则
COLUMN_FORMATS = {
    # 金额类（转换为亿）
    "总市值": lambda x: f"{x/1e8:.0f}亿" if pd.notna(x) else "-",
    "流通市值": lambda x: f"{x/1e8:.0f}亿" if pd.notna(x) else "-",
    "成交额": lambda x: f"{x/1e4:.0f}万" if pd.notna(x) else "-",
    "分红总额": lambda x: f"{x:.2f}亿" if pd.notna(x) else "-",
    
    # 百分比类
    "ROE": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "ROA": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "毛利率": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "净利率": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "资产负债率": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "涨跌幅": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "换手率": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "股息率": lambda x: f"{x:.2f}%" if pd.notna(x) else "-",
    "PE": lambda x: f"{x:.1f}" if pd.notna(x) else "-",
    "PB": lambda x: f"{x:.2f}" if pd.notna(x) else "-",
    "PS": lambda x: f"{x:.2f}" if pd.notna(x) else "-",
    
    # 价格类
    "收盘价": lambda x: f"{x:.2f}" if pd.notna(x) else "-",
    "每股收益": lambda x: f"{x:.2f}" if pd.notna(x) else "-",
    "每股净资产": lambda x: f"{x:.2f}" if pd.notna(x) else "-",
    "每股股利": lambda x: f"{x:.4f}" if pd.notna(x) else "-",
}
