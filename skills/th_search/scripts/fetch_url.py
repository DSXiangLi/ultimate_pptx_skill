#!/usr/bin/env python3
"""
URL内容获取脚本 - 直接调用 MCP 接口
用法: python fetch_url.py --url "URL地址"
"""

import argparse
import json
import os

import requests

MCP_BASE_URL = os.environ.get("TH_MCP_BASE_URL")


def main():
    parser = argparse.ArgumentParser(description="URL内容获取（MCP）")
    parser.add_argument("--url", "-u", required=True, help="需要获取全文的完整URL")
    parser.add_argument("--json", "-j", action="store_true", help="以JSON格式输出")
    args = parser.parse_args()

    # 调用 MCP
    try:
        response = requests.post(
            f"{MCP_BASE_URL}/fetch_url",
            headers={"Content-Type": "application/json"},
            json={"url": args.url},
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
    except Exception as e:
        print(f"错误: 无法获取内容 - {e}")
        return

    # 输出结果
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"URL: {result.get('url', args.url)}")
        print(f"\n内容:\n{result.get('data', '未能获取对应正文结果')}")


if __name__ == "__main__":
    main()
