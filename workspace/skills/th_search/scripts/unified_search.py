#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一搜索脚本 - 直接调用 MCP 接口
用法: python unified_search.py --query "搜索词" [--start-date YYYYMMDD] [--end-date YYYYMMDD] [--symbol 股票代码] [--search-types 类型1,类型2]
"""

import argparse
import json
import os
from datetime import date, datetime

import requests

MCP_BASE_URL = os.environ.get("TH_MCP_BASE_URL")


def is_valid_yyyymmdd(date_str):
    """检查日期字符串是否为有效的YYYYMMDD格式"""
    if len(date_str) != 8 or not date_str.isdigit():
        return False
    try:
        datetime(int(date_str[0:4]), int(date_str[4:6]), int(date_str[6:8]))
        return True
    except ValueError:
        return False


def main():
    parser = argparse.ArgumentParser(description="统一搜索接口（MCP）")
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

    # 处理参数
    query = [q.strip() for q in args.query.split(",") if q.strip()]
    symbol = [s.strip() for s in args.symbol.split(",") if s.strip()]
    search_types = [t.strip() for t in args.search_types.split(",") if t.strip()]
    
    # 日期默认值
    end_date = args.end_date if is_valid_yyyymmdd(args.end_date) else date.today().strftime("%Y%m%d")
    start_date = args.start_date if is_valid_yyyymmdd(args.start_date) else ""

    # 调用 MCP
    try:
        resp = requests.post(
            f"{MCP_BASE_URL}/unified_search",
            headers={"Content-Type": "application/json", "used-search-types": ",".join(search_types)},
            json={"query": query, "start_date": start_date, "end_date": end_date, "symbol": symbol},
            timeout=60
        )
        resp.raise_for_status()
        result = resp.json()
    except Exception as e:
        print(f"错误: 搜索服务调用失败 - {e}")
        return

    # 输出结果
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        data = result.get("data", [])
        if "message" in result:
            print(f"消息: {result['message']}")
        print(f"找到 {len(data)} 条结果:")
        for i, item in enumerate(data, 1):
            print(f"\n--- 结果 {i} ---")
            print(f"标题: {item.get('title', 'N/A')}")
            print(f"来源: {item.get('hostname', 'N/A')} ({item.get('source', 'N/A')})")
            print(f"时间: {item.get('publishedTime', 'N/A')}")
            print(f"链接: {item.get('link', 'N/A')}")
            content = item.get('content', '')
            if len(content) > 3000:
                content = content[:3000] + "..."
            print(f"内容: {content}")


if __name__ == "__main__":
    main()
