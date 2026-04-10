#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""
天弘搜索 - 仅 single_search（MCP 未支持精细过滤）

其他功能直接调用 MCP：
- unified_search: th_search/scripts/unified_search.py
- fetch_url: th_search/scripts/fetch_url.py
- single_search web类型: 复用 MCP unified_search 限定 web
"""

import os
import re

import requests

DOCSEARCH_URL = os.environ.get(
    "TH_DOCSEARCH_URL")
)
MCP_BASE_URL = os.environ.get(
    "TH_MCP_BASE_URL")
)


class THSearch:
    """仅 single_search（MCP 暂不支持精细过滤）"""

    def single_search(
        self,
        query="",
        search_type="research",
        search_scope="all",
        filters=None,
        from_=0,
        size=20,
        start_date="",
        end_date="",
        time_sorted="",
    ):
        """单一数据源搜索"""
        # web 类型复用 MCP unified_search
        if search_type == "web":
            return self._web_search_via_mcp(query, size)

        filters = filters or {}
        
        # 日期格式转换
        for key, date_val in [("fromDate", start_date), ("toDate", end_date)]:
            if date_val:
                filters[key] = f"{date_val[:4]}-{date_val[4:6]}-{date_val[6:8]}" if len(date_val) == 8 and date_val.isdigit() else date_val

        resp = requests.post(
            DOCSEARCH_URL,
            headers={"Content-Type": "application/json"},
            json={
                "query": query,
                "filters": filters,
                "from": from_,
                "size": size,
                "user_id": "ssoadmin01",
                "search_type": search_type,
                "search_scope": search_scope,
                "time_sorted": time_sorted,
            },
            timeout=30
        ).json()

        # 格式化输出
        source_map = {"research": "券商研报", "weixin": "微信公众号", "notice": "公司公告", "roadshow_meeting": "路演会议", "web": "互联网搜索"}
        formatted = []
        for doc in resp.get("recall_docs", []):
            doc_id = doc.get("docId", "")
            highlights = doc.get("highlightText", {}).get("content", [])
            formatted.append({
                "title": doc.get("title", ""),
                "link": f"https://fundmp.thfund.com.cn/#/ai/intelligentSearch/details/{doc_id}/{doc.get('docType', search_type)}",
                "summary": doc.get("summary", "")[:3000] if doc.get("summary") else "",
                "relatedParagraphs": [re.sub(r"<span[^>]*>|</span>", "", h.get("text", "")) for h in highlights],
                "publishedTime": doc.get("publishTime", "") or doc.get("publishDate", ""),
                "hostname": doc.get("fromSource", "") or doc.get("orgName", ""),
                "source": source_map.get(search_type, search_type),
                "docId": doc_id,
            })

        return {"data": formatted, "total_cnt": resp.get("total_cnt", 0)}

    def _web_search_via_mcp(self, query, size=10):
        """web 搜索复用 MCP unified_search"""
        try:
            resp = requests.post(
                f"{MCP_BASE_URL}/unified_search",
                headers={"Content-Type": "application/json", "used_search_types": "web"},
                json={"query": [query], "start_date": "", "end_date": "", "symbol": []},
                timeout=60
            ).json()
            
            # 过滤并截取
            data = [r for r in resp.get("data", []) if r.get("source") == "互联网搜索"]
            return {"data": data[:size], "total_cnt": len(data)}
        except Exception as e:
            return {"data": [], "total_cnt": 0, "error": str(e)}
