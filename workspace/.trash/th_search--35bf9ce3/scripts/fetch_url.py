#!/usr/bin/env python3
"""
URL内容获取脚本 - 给定URL获取对应全文
用法: python fetch_url.py --url "URL地址"
"""

import argparse
import json
import sys
from pathlib import Path

# 添加当前目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from th_search import THSearch


def main():
    parser = argparse.ArgumentParser(description="URL内容获取")
    parser.add_argument("--url", "-u", required=True, help="需要获取全文的完整URL")
    parser.add_argument("--json", "-j", action="store_true", help="以JSON格式输出")
    args = parser.parse_args()

    # 初始化搜索实例
    search = THSearch()

    # 执行获取
    result = search.fetch_url(args.url)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"URL: {result['url']}")
        print(f"\n内容:\n{result['data']}")


if __name__ == "__main__":
    main()
