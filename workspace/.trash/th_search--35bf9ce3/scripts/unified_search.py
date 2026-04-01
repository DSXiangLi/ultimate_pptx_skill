#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一搜索脚本 - 多数据源统一搜索接口
用法: python unified_search.py --query "搜索词" [--start-date YYYYMMDD] [--end-date YYYYMMDD] [--symbol 股票代码] [--search-types 类型1,类型2]
"""

import argparse
import json
import sys
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from th_search import THSearch


def main():
    parser = argparse.ArgumentParser(description="统一搜索接口")
    parser.add_argument("--query", "-q", required=True, help="搜索查询词，多个用逗号分隔")
    parser.add_argument("--start-date", "-s", default="", help="起始日期，格式：YYYYMMDD")
    parser.add_argument("--end-date", "-e", default="", help="截止日期，格式：YYYYMMDD")
    parser.add_argument("--symbol", "-S", default="", help="股票代码，多个用逗号分隔")
    parser.add_argument(
        "--search-types", "-t",
        default="research,roadshow,web,wechat",
        help="搜索类型，多个用逗号分隔 (research,roadshow,web,wechat,notice)"
    )
    parser.add_argument("--json", "-j", action="store_true", help="以JSON格式输出")
    args = parser.parse_args()

    # 解析参数
    query = [q.strip() for q in args.query.split(",") if q.strip()]
    symbol = [s.strip() for s in args.symbol.split(",") if s.strip()]
    search_types = [t.strip() for t in args.search_types.split(",") if t.strip()]

    # 初始化搜索实例
    search = THSearch()

    # 执行搜索
    result = search.unified_search(
        query=query,
        start_date=args.start_date,
        end_date=args.end_date,
        symbol=symbol,
        used_search_types=search_types,
    )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if "message" in result:
            print(f"消息: {result['message']}")
        print(f"找到 {len(result['data'])} 条结果:")
        for i, item in enumerate(result["data"], 1):
            print(f"\n--- 结果 {i} ---")
            print(f"标题: {item.get('title', 'N/A')}")
            print(f"来源: {item.get('hostname', 'N/A')} ({item.get('source', 'N/A')})")
            print(f"时间: {item.get('publishedTime', 'N/A')}")
            print(f"链接: {item.get('link', 'N/A')}")
            content = item.get('content', '')
            if len(content) > 200:
                content = content[:200] + "..."
            print(f"内容: {content}")


if __name__ == "__main__":
    main()
