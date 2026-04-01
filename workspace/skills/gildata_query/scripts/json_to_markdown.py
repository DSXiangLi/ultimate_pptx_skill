#!/usr/bin/env python3
"""
将 output 文件夹中的 JSON 文件转换为 Markdown 格式
用法: python scripts/json_to_markdown.py
"""

import json
import os
import argparse
from pathlib import Path
from datetime import datetime


def json_to_markdown(data: dict) -> str:
    """将JSON数据转换为Markdown格式"""
    lines = []

    # 标题
    table_name = data.get('tableName', 'Unknown')
    table_chi_name = data.get('tableChiName', '')
    lines.append(f"# {table_name}")
    lines.append("")
    lines.append(f"**中文名**: {table_chi_name}")
    lines.append("")

    # 基本信息
    lines.append("## 基本信息")
    lines.append("")
    lines.append("| 属性 | 值 |")
    lines.append("|------|-----|")
    lines.append(f"| 表名 | `{table_name}` |")
    lines.append(f"| MySQL表名 | `{table_name.lower()}` |")
    lines.append(f"| 中文名 | {table_chi_name} |")
    lines.append(f"| 路径 | {data.get('path', 'N/A')} |")
    lines.append(f"| 更新频率 | {data.get('tableUpdateTime', 'N/A')} |")
    lines.append(f"| 字段数量 | {data.get('column_count', 'N/A')} |")
    lines.append(f"| 版本 | {data.get('tableVersion', 'N/A')} |")
    lines.append("")

    # 描述
    desc = data.get('description', '')
    if desc:
        lines.append("## 表描述")
        lines.append("")
        # 处理多行描述
        for line in desc.split('\n'):
            line = line.strip()
            if line:
                lines.append(line)
        lines.append("")

    # 字段列表
    columns = data.get('columns', [])
    if columns:
        lines.append("## 字段列表")
        lines.append("")
        lines.append("| 序号 | 字段名 | 中文名 | 类型 | 可空 | 填充率 | 说明 |")
        lines.append("|------|--------|--------|------|------|--------|------|")

        for col in columns:
            col_order = col.get('columnOrderId', '')
            col_name = col.get('columnName', '')
            col_chi = col.get('columnChiName', '')
            col_type = col.get('columnType', '')
            nullable = "✓" if col.get('isNullable') == 1 else "✗"
            value_rate = col.get('valueRate', '') or ''
            if value_rate:
                value_rate = f"{value_rate}%"
            remark = col.get('remark', '') or ''

            # 截断过长的remark
            if len(remark) > 60:
                remark = remark[:60] + "..."
            # 转义管道符
            remark = remark.replace('|', '\\|').replace('\n', ' ')

            lines.append(f"| {col_order} | `{col_name}` | {col_chi} | {col_type} | {nullable} | {value_rate} | {remark} |")

        lines.append("")

    # 关键字段（带remark的字段）
    key_columns = [col for col in columns if col.get('remark')]
    if key_columns:
        lines.append("## 字段说明")
        lines.append("")
        for col in key_columns[:10]:  # 最多显示10个
            col_name = col.get('columnName', '')
            col_chi = col.get('columnChiName', '')
            remark = col.get('remark', '')
            lines.append(f"### {col_name} ({col_chi})")
            lines.append("")
            lines.append(remark)
            lines.append("")

    # 使用示例
    lines.append("## SQL示例")
    lines.append("")
    lines.append("```sql")
    lines.append(f"-- 查询 {table_chi_name} 数据")
    lines.append(f"SELECT *")
    lines.append(f"FROM {table_name.lower()}")

    # 根据字段生成条件示例
    has_trading_day = any(col.get('columnName') == 'TradingDay' for col in columns)
    has_inner_code = any(col.get('columnName') == 'InnerCode' for col in columns)
    has_index_code = any(col.get('columnName') == 'IndexCode' for col in columns)

    conditions = []
    if has_trading_day:
        conditions.append("WHERE TradingDay >= '2024-01-01'")
    if has_inner_code:
        conditions.append("  AND InnerCode = 12345  -- 替换为实际的InnerCode")
    if has_index_code and not has_inner_code:
        conditions.append("  AND IndexCode = 12345  -- 替换为实际的IndexCode")

    if conditions:
        lines.append('\n'.join(conditions))
    lines.append("LIMIT 10;")
    lines.append("```")
    lines.append("")

    # 元信息
    lines.append("---")
    lines.append("")
    lines.append(f"*文档生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")

    return '\n'.join(lines)


def get_category(path: str) -> str:
    """根据路径获取分类"""
    if not path:
        return "其他"
    if "指数数据库" in path:
        return "指数"
    if "上市公司数据库" in path or "股票" in path:
        return "股票"
    if "公募基金" in path or "基金" in path:
        return "基金"
    if "债券" in path:
        return "债券"
    if "期货" in path:
        return "期货"
    if "港股" in path:
        return "港股"
    if "常量库" in path:
        return "常量"
    return "其他"


def main():
    parser = argparse.ArgumentParser(description="将JSON文件转换为Markdown格式")
    parser.add_argument("--input", "-i", default="../../output", help="输入目录")
    parser.add_argument("--output", "-o", default="../resource", help="输出目录")
    parser.add_argument("--limit", "-l", type=int, default=0, help="限制处理数量 (0=不限制)")
    args = parser.parse_args()

    input_dir = Path(args.input)
    output_dir = Path(args.output)

    if not input_dir.exists():
        print(f"错误: 输入目录不存在 - {input_dir}")
        return

    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)

    # 获取所有JSON文件
    json_files = list(input_dir.glob("*.json"))
    total = len(json_files)
    print(f"找到 {total} 个JSON文件")

    if args.limit > 0:
        json_files = json_files[:args.limit]
        print(f"限制处理前 {args.limit} 个文件")

    # 统计信息
    stats = {
        "success": 0,
        "failed": 0,
        "categories": {}
    }

    # 索引内容
    index_lines = []
    index_lines.append("# 聚源数据库表结构文档")
    index_lines.append("")
    index_lines.append(f"共 {total} 张表，生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    index_lines.append("")

    # 按分类组织
    categorized = {}

    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            table_name = data.get('tableName', 'Unknown')
            table_chi = data.get('tableChiName', '')
            path = data.get('path', '')
            category = get_category(path)

            # 生成Markdown
            md_content = json_to_markdown(data)
            md_path = output_dir / f"{table_name}.md"

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(md_content)

            # 统计
            stats["success"] += 1
            stats["categories"][category] = stats["categories"].get(category, 0) + 1

            # 分类存储
            if category not in categorized:
                categorized[category] = []
            categorized[category].append({
                "name": table_name,
                "chi_name": table_chi,
                "path": path
            })

            if i % 100 == 0:
                print(f"进度: {i}/{len(json_files)} ({i*100//len(json_files)}%)")

        except Exception as e:
            stats["failed"] += 1
            print(f"处理失败: {json_file.name} - {e}")

    # 生成索引文件
    index_lines.append("## 分类索引")
    index_lines.append("")

    for category in sorted(categorized.keys()):
        tables = categorized[category]
        index_lines.append(f"### {category} ({len(tables)} 张表)")
        index_lines.append("")
        index_lines.append("| 表名 | 中文名 | 文档 |")
        index_lines.append("|------|--------|------|")

        for table in sorted(tables, key=lambda x: x['name']):
            index_lines.append(f"| `{table['name']}` | {table['chi_name']} | [{table['name']}.md]({table['name']}.md) |")

        index_lines.append("")

    # 写入索引文件
    index_path = output_dir / "README.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_lines))

    # 打印统计
    print("\n" + "=" * 50)
    print("转换完成!")
    print("=" * 50)
    print(f"成功: {stats['success']}")
    print(f"失败: {stats['failed']}")
    print(f"\n分类统计:")
    for cat, count in sorted(stats['categories'].items()):
        print(f"  {cat}: {count}")
    print(f"\n输出目录: {output_dir}")
    print(f"索引文件: {index_path}")


if __name__ == "__main__":
    main()
