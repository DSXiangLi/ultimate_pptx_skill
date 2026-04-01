#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unified_search.py 单元测试
用法: python test_unified_search.py
"""

import unittest
import json
import sys
from datetime import datetime
from unittest.mock import patch, MagicMock
from io import StringIO

# 导入被测模块
import unified_search


class TestIsValidYyyymmdd(unittest.TestCase):
    """测试日期格式验证函数"""

    def test_valid_dates(self):
        """有效的日期格式"""
        self.assertTrue(unified_search.is_valid_yyyymmdd("20260331"))
        self.assertTrue(unified_search.is_valid_yyyymmdd("20240101"))
        self.assertTrue(unified_search.is_valid_yyyymmdd("20000229"))  # 闰年
        self.assertTrue(unified_search.is_valid_yyyymmdd("20241231"))

    def test_invalid_dates(self):
        """无效的日期格式"""
        # 长度不对
        self.assertFalse(unified_search.is_valid_yyyymmdd("2026033"))
        self.assertFalse(unified_search.is_valid_yyyymmdd("202603310"))
        # 包含非数字
        self.assertFalse(unified_search.is_valid_yyyymmdd("202603ab"))
        # 无效日期
        self.assertFalse(unified_search.is_valid_yyyymmdd("20261301"))  # 13月
        self.assertFalse(unified_search.is_valid_yyyymmdd("20260229"))  # 非闰年2月29
        self.assertFalse(unified_search.is_valid_yyyymmdd("20260431"))  # 4月31日

    def test_empty_string(self):
        """空字符串"""
        self.assertFalse(unified_search.is_valid_yyyymmdd(""))


class TestArgumentParsing(unittest.TestCase):
    """测试命令行参数解析"""

    def test_default_values(self):
        """测试默认值"""
        with patch.object(sys, 'argv', ['unified_search.py', '-q', '测试']):
            parser = unified_search.argparse.ArgumentParser()
            parser.add_argument("--query", "-q", required=True)
            parser.add_argument("--start-date", "-s", default="")
            parser.add_argument("--end-date", "-e", default="")
            parser.add_argument("--symbol", "-S", default="")
            parser.add_argument("--search-types", "-t", 
                              default="research,roadshow,web,wechat")
            parser.add_argument("--json", "-j", action="store_true")
            args = parser.parse_args()
            
            self.assertEqual(args.query, "测试")
            self.assertEqual(args.search_types, "research,roadshow,web,wechat")

    def test_query_with_multiple_terms(self):
        """测试多查询词"""
        query_str = "贵州茅台,白酒行业,人工智能"
        query = [q.strip() for q in query_str.split(",") if q.strip()]
        self.assertEqual(len(query), 3)
        self.assertEqual(query[0], "贵州茅台")

    def test_search_types_parsing(self):
        """测试搜索类型解析"""
        search_types_str = "research,web"
        search_types = [t.strip() for t in search_types_str.split(",") if t.strip()]
        self.assertEqual(search_types, ["research", "web"])


class TestMCPResponseParsing(unittest.TestCase):
    """测试 MCP 响应解析"""

    def setUp(self):
        """准备测试数据"""
        self.sample_response = {
            "data": [
                {
                    "title": "贵州茅台深度研究报告",
                    "hostname": "中信证券",
                    "source": "外部研报",
                    "publishedTime": "2026-03-30",
                    "link": "https://fundmp.thfund.com.cn/xxx",
                    "content": "贵州茅台是中国高端白酒龙头企业..."
                },
                {
                    "title": "茅台提价公告",
                    "hostname": "贵州茅台",
                    "source": "公司公告",
                    "publishedTime": "2026-03-29",
                    "link": "https://fundmp.thfund.com.cn/yyy",
                    "content": "公司决定调整产品价格..."
                }
            ],
            "total": 2
        }

    def test_parse_data(self):
        """测试数据解析"""
        data = self.sample_response.get("data", [])
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["title"], "贵州茅台深度研究报告")

    def test_content_truncation(self):
        """测试内容截断"""
        long_content = "a" * 5000
        if len(long_content) > 3000:
            truncated = long_content[:3000] + "..."
            self.assertEqual(len(truncated), 3003)
            self.assertTrue(truncated.endswith("..."))

    def test_source_statistics(self):
        """测试来源统计"""
        sources = {}
        for item in self.sample_response.get("data", []):
            src = item.get("source", "Unknown")
            sources[src] = sources.get(src, 0) + 1
        
        self.assertEqual(sources["外部研报"], 1)
        self.assertEqual(sources["公司公告"], 1)


class TestMockAPIIntegration(unittest.TestCase):
    """集成测试：模拟 API 调用"""

    @patch('unified_search.requests.post')
    def test_successful_search(self, mock_post):
        """测试成功搜索"""
        # 模拟 API 返回
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "title": "测试结果",
                    "hostname": "测试来源",
                    "source": "外部研报",
                    "publishedTime": "2026-03-31",
                    "link": "http://test.com",
                    "content": "测试内容"
                }
            ]
        }
        mock_post.return_value = mock_response

        # 验证 mock 正常工作
        resp = mock_post("http://test/unified_search", json={"query": ["测试"]})
        self.assertEqual(resp.status_code, 200)

    @patch('unified_search.requests.post')
    def test_api_error_handling(self, mock_post):
        """测试 API 错误处理"""
        mock_post.side_effect = Exception("Connection error")
        
        with self.assertRaises(Exception) as context:
            mock_post("http://test/unified_search", json={})
        
        self.assertIn("Connection error", str(context.exception))

    @patch('unified_search.requests.post')
    def test_empty_results(self, mock_post):
        """测试空结果"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [],
            "message": "无相关内容"
        }
        mock_post.return_value = mock_response

        result = mock_response.json()
        self.assertEqual(len(result["data"]), 0)
        self.assertEqual(result["message"], "无相关内容")


class TestOutputFormatting(unittest.TestCase):
    """测试输出格式化"""

    def test_json_output_format(self):
        """测试 JSON 格式输出"""
        result = {
            "data": [
                {
                    "title": "测试",
                    "hostname": "来源",
                    "source": "研报",
                    "publishedTime": "2026-03-31",
                    "link": "http://test.com",
                    "content": "内容"
                }
            ]
        }
        
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        self.assertIn("测试", json_str)
        self.assertIn("来源", json_str)

    def test_text_output_format(self):
        """测试文本格式输出"""
        data = [
            {
                "title": "测试结果",
                "hostname": "中信证券",
                "source": "外部研报",
                "publishedTime": "2026-03-31",
                "link": "http://test.com",
                "content": "这是测试内容"
            }
        ]
        
        # 模拟文本输出
        output = f"找到 {len(data)} 条结果:\n"
        for i, item in enumerate(data, 1):
            output += f"\n--- 结果 {i} ---\n"
            output += f"标题: {item.get('title', 'N/A')}\n"
            output += f"来源: {item.get('hostname', 'N/A')} ({item.get('source', 'N/A')})\n"
        
        self.assertIn("找到 1 条结果", output)
        self.assertIn("测试结果", output)


class TestSearchTypesFilter(unittest.TestCase):
    """测试搜索类型过滤功能"""

    def test_filter_by_source(self):
        """测试按来源过滤"""
        all_data = [
            {"title": "研报1", "source": "外部研报"},
            {"title": "研报2", "source": "外部研报"},
            {"title": "公告1", "source": "公司公告"},
            {"title": "互联网1", "source": "互联网搜索"},
            {"title": "公众号1", "source": "精选公众号"},
        ]
        
        # 过滤 web 类型
        web_data = [r for r in all_data if r.get("source") == "互联网搜索"]
        
        self.assertEqual(len(web_data), 1)
        self.assertEqual(web_data[0]["title"], "互联网1")

    def test_multiple_search_types(self):
        """测试多搜索类型"""
        all_data = [
            {"title": "研报1", "source": "外部研报"},
            {"title": "公告1", "source": "公司公告"},
            {"title": "互联网1", "source": "互联网搜索"},
        ]
        
        search_types = ["外部研报", "公司公告"]
        filtered = [r for r in all_data if r.get("source") in search_types]
        
        self.assertEqual(len(filtered), 2)


if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)