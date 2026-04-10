#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
单一数据源搜索脚本
用法: python single_search.py --query "搜索词" --search-type research [可选参数]
"""

import argparse
import json
import sys
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from th_search import THSearch


# search_type 枚举值说明
SEARCH_TYPES = {
    "research": "券商研报",
    "weixin": "微信公众号",
    "notice": "公司公告",
    "roadshow_meeting": "路演会议",
    "web": "互联网搜索（夸克）",
}

# search_scope 枚举值说明
SEARCH_SCOPES = {
    "all": "全文检索",
    "title": "标题检索",
}


def main():
    parser = argparse.ArgumentParser(
        description="单一数据源搜索",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
搜索类型 (--search-type):
  research        券商研报
  weixin          微信公众号
  notice          公司公告
  roadshow_meeting 路演会议
  web             互联网搜索（夸克）

搜索范围 (--search-scope):
  all             全文检索（默认）
  title           标题检索

示例:
  # 搜索研报
  python single_search.py --query "贵州茅台" --search-type research

  # 搜索公众号文章
  python single_search.py --query "人工智能" --search-type weixin

  # 互联网搜索
  python single_search.py --query "贵州茅台" --search-type web

  # 指定时间范围
  python single_search.py --query "业绩" --search-type notice --start-date "2024-01-01" --end-date "2024-12-31"

  # 标题检索
  python single_search.py --query "茅台" --search-type research --search-scope title
        """,
    )
    parser.add_argument("--query", "-q", default="", help="搜索查询词（可为空）")
    parser.add_argument(
        "--search-type", "-t",
        default="research",
        choices=list(SEARCH_TYPES.keys()),
        help="搜索类型（默认: research）"
    )
    parser.add_argument(
        "--search-scope", "-s",
        default="all",
        choices=list(SEARCH_SCOPES.keys()),
        help="搜索范围（默认: all 全文检索）"
    )
    parser.add_argument("--start-date", default="", help="起始日期（YYYY-MM-DD 或 YYYYMMDD）")
    parser.add_argument("--end-date", default="", help="截止日期（YYYY-MM-DD 或 YYYYMMDD）")
    parser.add_argument("--from", dest="from_", type=int, default=0, help="起始位置（默认: 0）")
    parser.add_argument("--size", type=int, default=10, help="返回数量（默认: 10）")
    parser.add_argument("--filter", "-f", action="append", help="过滤条件，格式: key=value（可多次使用）")
    args = parser.parse_args()

    # 解析过滤条件
    filters = {}
    if args.filter:
        for f in args.filter:
            if "=" in f:
                key, value = f.split("=", 1)
                # 日期字段保持字符串格式
                if key in ["fromDate", "toDate"]:
                    filters[key] = value
                # 支持逗号分隔的列表
                elif "," in value:
                    filters[key] = value.split(",")
                else:
                    filters[key] = [value] if value else []

    # 初始化搜索实例
    search = THSearch()

    # 执行搜索
    result = search.single_search(
        query=args.query,
        search_type=args.search_type,
        search_scope=args.search_scope,
        filters=filters if filters else None,
        from_=args.from_,
        size=args.size,
        start_date=args.start_date,
        end_date=args.end_date,
    )

    data = result.get("data", [])
    total_cnt = result.get("total_cnt", 0)
    error = result.get("error")

    if error:
        print(f"错误: {error}")
        return

    print(f"搜索类型: {SEARCH_TYPES.get(args.search_type, args.search_type)}")
    print(f"搜索范围: {SEARCH_SCOPES.get(args.search_scope, args.search_scope)}")
    print(f"找到 {total_cnt} 条结果，显示 {len(data)} 条:\n")

    for i, item in enumerate(data, 1):
        print(f"--- 结果 {i} ---")
        print(f"标题: {item.get('title', 'N/A')}")
        print(f"来源: {item.get('hostname', 'N/A')} ({item.get('source', 'N/A')})")
        print(f"时间: {item.get('publishedTime', 'N/A')}")
        print(f"链接: {item.get('link', 'N/A')}")

        # 显示摘要
        summary = item.get('summary', '')
        if summary:
            if len(summary) > 3000:
                summary = summary[:3000] + "..."
            print(f"摘要: {summary}")

        # 显示完整内容（web搜索）
        content = item.get('content', '')
        if content:
            if len(content) > 3000:
                content = content[:3000] + "..."
            print(f"内容: {content}")

        # 显示相关段落
        related_paragraphs = item.get('relatedParagraphs', [])
        if related_paragraphs:
            print(f"相关段落 ({len(related_paragraphs)}段):")
            for para in related_paragraphs[:5]:
                if len(para) > 3000:
                    para = para[:3000] + "..."
                print(f"  {para}")

        print()


if __name__ == "__main__":
    main()
