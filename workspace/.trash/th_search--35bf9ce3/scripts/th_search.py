#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# Author：wangzhe@thfund.com.cn
# Date ：2025/6/10 14:35
"""
天弘搜索核心模块 - 包含所有搜索相关的类和工具函数

包含:
- 工具函数 (utils)
- AShareSearch 搜索类
- THSearch 对外接口类
"""

import concurrent.futures
import json
import logging
import re
import string
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from difflib import SequenceMatcher
from threading import Lock

import html2text
import requests
from markdownify import markdownify as md
from readabilipy import simple_json_from_html_string

logger = logging.getLogger(__name__)

# ============ URL 配置 ============
# 原 k8s 内部地址已替换为统一的外部访问地址
BASE_URL = "http://algoplatform.thfund.work/assistant"

# ============ 工具函数 ============


def remove_punctuation(text):
    """移除字符串中的标点符号"""
    if not text:
        return ""
    return re.sub(r"[^\w\s]", "", str(text))


def similarity(a, b):
    """计算两个字符串的相似度（0-1之间）"""
    a_clean = remove_punctuation(a).lower().strip()
    b_clean = remove_punctuation(b).lower().strip()

    if not a_clean and not b_clean:
        return 1.0
    if not a_clean or not b_clean:
        return 0.0

    return SequenceMatcher(None, a_clean, b_clean).ratio()


def filter_duplicate_items(items, similarity_threshold=0.95):
    """根据title去重，考虑去除标点后的字符串相似度"""
    unique_items = []
    seen_titles = []

    for item in items:
        if "title" not in item:
            unique_items.append(item)
            continue

        current_title = item["title"]
        is_duplicate = False

        for seen_title in seen_titles:
            if similarity(current_title, seen_title) >= similarity_threshold:
                is_duplicate = True
                break

        if not is_duplicate:
            unique_items.append(item)
            seen_titles.append(current_title)

    return unique_items


def rewrite_query(query):
    """重写查询词，将相对日期转换为绝对日期"""
    date_match = re.search(r"(今日|今天|今早|昨日|昨天)", query)
    if date_match:
        if date_match.group(1) in ["今日", "今天", "今早"]:
            today = datetime.today().strftime("%Y年%m月%d日")
            query = query.replace(date_match.group(1), today)
        else:
            yesterday = (datetime.today() - timedelta(1)).strftime("%Y年%m月%d日")
            query = query.replace(date_match.group(1), yesterday)
    return query


def advanced_non_printable_filter(text, mode="moderate"):
    """高级非打印字符过滤器"""
    patterns = {
        "light": r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]",
        "moderate": r"[\x00-\x1F\x7F\u0080-\u009F\u200B-\u200F\u2028\u2029]",
    }
    pattern = patterns.get(mode, patterns["moderate"])
    return re.sub(pattern, "", text)


def convert_wind_code(symbol):
    """将股票代码转换为Wind格式（添加交易所后缀）"""
    if len(symbol) == 6:
        if symbol.startswith("6"):
            return f"{symbol}.SH"
        elif symbol.startswith(("0", "3")):
            return f"{symbol}.SZ"
        elif symbol.startswith("9"):
            return f"{symbol}.BJ"
        else:
            return symbol
    elif len(symbol) == 5:
        return f"{symbol}.HK"
    else:
        return symbol


def extract_numbers(text):
    """提取字符串中的数字部分"""
    return re.sub(r"\D", "", text)


def convert_date_format(input_date, output_format="%Y-%m-%d %H:%M:%S"):
    """将 ISO 8601 格式日期转换为指定的日期格式"""
    try:
        if input_date.endswith("Z"):
            input_date = input_date[:-1] + "+00:00"

        tz_match = re.search(r"([+-]\d{2}:\d{2})$", input_date)
        tz_offset = None

        if tz_match:
            tz_str = tz_match.group(1)
            base_date = input_date[: -len(tz_str)]
            sign = -1 if tz_str[0] == "-" else 1
            hours, minutes = map(int, tz_str[1:].split(":"))
            tz_offset = timedelta(hours=hours, minutes=minutes) * sign
        else:
            base_date = input_date

        if "." in base_date:
            date_part, time_part = base_date.split(".", 1)
            fractional = re.match(r"(\d{1,6})", time_part)
            if fractional:
                microsecond = fractional.group(1).ljust(6, "0")[:6]
                rest = time_part[len(fractional.group(0)) :]
                base_date = f"{date_part}.{microsecond}{rest}"

        for fmt in (
            "%Y-%m-%dT%H:%M:%S.%f",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
        ):
            try:
                dt = datetime.strptime(base_date, fmt)
                if tz_offset is not None:
                    dt = dt.replace(tzinfo=timezone(tz_offset))
                    dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
                return dt.strftime(output_format)
            except ValueError:
                continue

        raise ValueError(f"无法解析日期: {input_date}")

    except Exception as e:
        raise ValueError(f"日期转换失败: {e}")


def deduplicate_dict_list(data, key="content"):
    """根据指定键去重字典列表"""
    seen = set()
    result = []

    for item in data:
        value = item.get(key)
        if value not in seen:
            seen.add(value)
            result.append(item)

    return result


def subtract_three_months(effect_end_date):
    """从日期减去3个月"""
    dt = datetime.strptime(effect_end_date, "%Y%m%d")
    if dt.month > 3:
        try:
            new_date = dt.replace(year=dt.year, month=dt.month - 3)
        except ValueError:
            if dt.month - 3 == 2:
                year = dt.year
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    last_day = 29
                else:
                    last_day = 28
                new_date = dt.replace(year=dt.year, month=2, day=last_day)
            else:
                if dt.month - 3 in [4, 6, 9, 11]:
                    last_day = 30
                else:
                    last_day = 31
                new_date = dt.replace(year=dt.year, month=dt.month - 3, day=last_day)
    else:
        new_year = dt.year - 1
        new_month = dt.month + 9
        try:
            new_date = dt.replace(year=new_year, month=new_month)
        except ValueError:
            if new_month == 2:
                if (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0):
                    last_day = 29
                else:
                    last_day = 28
                new_date = dt.replace(year=new_year, month=2, day=last_day)
            else:
                if new_month in [4, 6, 9, 11]:
                    last_day = 30
                else:
                    last_day = 31
                new_date = dt.replace(year=new_year, month=new_month, day=last_day)

    return new_date.strftime("%Y%m%d")


def contains_only_special_chars(s):
    """检查字符串是否只包含特殊字符"""
    allowed_chars = string.punctuation + string.whitespace
    return all(char in allowed_chars for char in s)


def html_to_markdown(html_content):
    """将HTML内容转换为Markdown格式"""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.bypass_tables = False
    h.wrap_links = True

    if html_content:
        markdown_content = h.handle(html_content)
    else:
        markdown_content = ""

    return markdown_content


def get_web_search_context(query, item):
    """获取网页搜索上下文"""
    title = item["title"]
    url = item["link"]
    main_text = item["mainText"]
    if main_text is None:
        main_text = "无正文内容"
    try:
        if main_text is None:
            headers = {
                "Authorization": "Bearer jina_3efd033aa5c145eea76fa63abcb3c3a6mdR8Z8Wx0jf2qshw3vCazkv-Nro0",
                "X-Retain-Images": "none",
                "X-Return-Format": "html",
                "X-Timeout": "60",
            }
            if "weixin" in url:
                headers["X-Engine"] = "cf-browser-rendering"
            data = {"url": url}
            response = requests.post("https://r.jina.ai/", headers=headers, json=data)
            html = response.text
            article = simple_json_from_html_string(html, use_readability=True)
            main_text = md(article["content"])
    except Exception:
        pass

    extract_content = [main_text[:20000]] if len(main_text) >= 5000 else [main_text]
    publishedTime = (
        convert_date_format(item["publishedTime"]) if item["publishedTime"] else ""
    )
    output_dict = {
        "title": title,
        "link": url,
        "content": "\n".join(extract_content),
        "publishedTime": publishedTime,
        "hostname": item["hostname"],
    }
    return output_dict


def remove_all_brackets_indices(text):
    """删除文本中所有[数字]格式的索引"""
    pattern = r"\[\d+\]"
    result = re.sub(pattern, "", text)
    return result


def is_valid_yyyymmdd(date_str):
    """检查日期字符串是否为有效的YYYYMMDD格式"""
    if len(date_str) != 8 or not date_str.isdigit():
        return False
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False


# ============ AShareSearch 类 ============


class AShareSearch:
    """A股搜索类 - 核心搜索功能实现"""

    def __init__(self):
        self.qwen_url = "https://cloud-iqs.aliyuncs.com/search/unified"
        self.qwen_key = "LB9utNnvz33XCa93Ds9dGDs0i3inUHc2ODQ5MTUxOQ"

        # 使用统一的外部访问地址
        self.search_url = f"{BASE_URL}/docsearch/smart_search"
        self.fetch_url = f"{BASE_URL}/docsearch/fetch_doc_info"
        self.local_search_url = f"{BASE_URL}/recall/index_recall"
        self.rerank_url = f"{BASE_URL}/rerank/rerank"
        self.expand_context_url = f"{BASE_URL}/recall/expand_context"
        self.web_search_url = f"{BASE_URL}/webscraper/th_qwen_search"

        self.rerank_max_words = 15000
        self.recalls_expand_length = 1500

    def fetch(self, url):
        """获取URL对应的全文内容"""
        headers = {"Content-Type": "application/json"}
        main_text = "未查询到全文信息"
        if "fundmp" in url:
            url = url.strip("/")
            if "research" in url:
                doc_id = url.split("/")[-2]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "research",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"][0]
                main_text = r["reportContent"]
            elif "notice" in url:
                doc_id = url.split("/")[-2]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "notice",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"][0]
                if "contentHtml" in r and r["contentHtml"] is not None:
                    main_text = html_to_markdown(r["contentHtml"])
                else:
                    main_text = r["content"]
            elif "allRoadShow" in url:
                doc_id = url.split("=")[-1]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "roadshow_meeting",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"][0]
                main_text = ""
                if "fullDigest" in r and r["fullDigest"] is not None:
                    main_text += r["fullDigest"]
                if "mainPoint" in r and r["mainPoint"] is not None:
                    main_text += r["mainPoint"]
                if "speechContent" in r and r["speechContent"] is not None:
                    main_text += r["speechContent"]
            elif "meetingComments" in url:
                doc_id = url.split("/")[-1]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "inner_research",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"][0]
                main_text = r["contentPlain"]
            elif "wxOfficial" in url:
                doc_id = url.split("/")[-1]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "wx_official",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"][0]
                main_text = r["contentPlain"]
            else:
                doc_id = url.split("/")[-2]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "news",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"][0]
                main_text = r["newsContentPlain"]
        else:
            headers = {
                "Authorization": "Bearer jina_3efd033aa5c145eea76fa63abcb3c3a6mdR8Z8Wx0jf2qshw3vCazkv-Nro0",
                "X-Retain-Images": "none",
                "X-Return-Format": "html",
                "X-Timeout": "60",
            }
            if "weixin" in url:
                headers["X-Engine"] = "cf-browser-rendering"
            data = {"url": url}
            response = requests.post("https://r.jina.ai/", headers=headers, json=data)
            html = response.text
            article = simple_json_from_html_string(html, use_readability=True)
            main_text = md(article["content"])
        if main_text is None or len(main_text) == 0:
            main_text = "未查询到全文信息，该地址无法查询全文信息"
        return main_text

    def fetch_abstract(self, url):
        """获取摘要"""
        headers = {"Content-Type": "application/json"}
        main_text = ""
        if "fundmp" in url:
            url = url.strip("/")
            if "research" in url:
                doc_id = url.split("/")[-2]
                input_data = {
                    "doc_ids": [doc_id],
                    "user_id": "ssoadmin01",
                    "search_type": "research",
                    "return_plain_content": True,
                }
                response = requests.post(
                    url=self.fetch_url, headers=headers, json=input_data
                )
                r = response.json()["recall_docs"]
                if len(r) == 0:
                    return ""
                main_text = r[0]["abstract"]
        if main_text is None or len(main_text) == 0:
            main_text = ""
        return main_text

    def wechat_search(self, queries, start_date, end_date, max_len=8):
        """微信公众号搜索"""
        headers = {"Content-Type": "application/json"}
        filters = {}
        if start_date:
            date_obj = datetime.strptime(start_date, "%Y%m%d")
            search_start_date = date_obj.strftime("%Y-%m-%d")
            filters["fromDate"] = search_start_date
        if end_date:
            date_obj = datetime.strptime(end_date, "%Y%m%d")
            search_end_date = date_obj.strftime("%Y-%m-%d")
            filters["toDate"] = search_end_date

        top_k = max_len
        outputs = []
        urls = set()
        for query in queries:
            input_data = {
                "query": query.replace("最近", "").replace("新闻", ""),
                "filters": {},
                "from": 0,
                "size": 2 * top_k,
                "user_id": "ssoadmin01",
                "search_type": "wx_official",
                "search_scope": "all",
                "time_sorted": "",
            }
            response = requests.post(
                url=self.search_url, headers=headers, json=input_data
            )
            results = response.json()["recall_docs"]
            doc_ids = [res["docId"] for res in results]
            input_data = {
                "doc_ids": doc_ids,
                "user_id": "ssoadmin01",
                "search_type": "wx_official",
                "return_plain_content": True,
            }
            response = requests.post(
                url=self.fetch_url, headers=headers, json=input_data
            )
            results = response.json()["recall_docs"]
            for item in results:
                if "contentPlain" not in item or item["contentPlain"] is None:
                    continue
                output_dict = {
                    "title": item["title"],
                    "link": f'https://fundmp.thfund.com.cn/#/ai/intelligentSearch/wxOfficial/details/{item["docId"]}',
                    "content": item["contentPlain"][:3000],
                    "query": query,
                    "publishtime": item["publishTime"],
                    "source": item["nickName"],
                    "viewSource": "精选公众号",
                }
                if item["docId"] not in urls:
                    outputs.append(output_dict)
                urls.add(item["docId"])

        results_merge_mark = requests.post(
            self.rerank_url,
            data=json.dumps({"data": outputs, "max_words": 10 * self.rerank_max_words}),
        ).json()["labels"]
        keep_results_list = []
        for mark in results_merge_mark:
            if mark.get("isTrue") or mark.get("bge_score", 0.0) >= 0.37:
                output_dict = {
                    "title": mark["title"],
                    "link": mark["link"],
                    "content": mark["content"],
                    "publishedTime": mark["publishtime"],
                    "hostname": mark["source"],
                    "source": "精选公众号",
                }
                keep_results_list.append(output_dict)

        keep_results_list.sort(
            key=lambda x: datetime.strptime(x["publishedTime"], "%Y-%m-%d %H:%M:%S"),
            reverse=True,
        )
        return keep_results_list[:15]

    def local_search(
        self,
        query,
        source,
        effect_start_date,
        effect_end_date,
        topn,
        inner_research_permission_level,
        filters=None,
    ):
        """本地搜索"""
        headers = {"Content-Type": "application/json"}
        input_data = {
            "search": [query],
            "source": source,
            "effect_start_date": effect_start_date,
            "effect_end_date": effect_end_date,
            "topn": 2 * topn,
            "return_raw": True,
            "research_team": True,
            "inner_research_permission_level": inner_research_permission_level,
        }
        if filters is not None:
            input_data["filters"] = filters

        response = requests.post(
            url=self.local_search_url, headers=headers, json=input_data
        )
        results = response.json()["recalls"]["fuse"]
        results.sort(key=lambda x: x["publishtime"], reverse=True)
        keep_results_list = []

        if results:
            for elem in results:
                if elem["viewSource"] == "内部研报":
                    elem["content"] = elem["title"] + "\n" + elem["content"]
            results_merge_mark = requests.post(
                self.rerank_url,
                data=json.dumps({"data": results, "max_words": self.rerank_max_words}),
            ).json()["labels"]
            for mark in results_merge_mark:
                if mark.get("isTrue") or (
                    mark.get("bge_score", 0.0) >= 0.37 and source != "notice"
                ):
                    keep_results_list.append(mark)
            for elem in keep_results_list:
                if elem["viewSource"] == "内部研报":
                    elem["content"] = "\n".join(elem["content"].split("\n")[1:])
            if keep_results_list:
                keep_results_list = self.recalls_expand(keep_results_list)
        return keep_results_list

    def recalls_expand(self, recalls):
        """扩展召回结果"""
        for _, recall in enumerate(recalls):
            if recall["viewSource"] in ["公司公告", "外部研报", "会议路演"]:
                data = {"recall": recall, "extract_length": self.recalls_expand_length}
                r = requests.post(self.expand_context_url, data=json.dumps(data))
                if r.status_code == 200 and r.json()["content"]:
                    recall["snippet"] = recall["content"]
                    recall["content"] = r.json()["content"]
                else:
                    recall["snippet"] = recall["content"]
                    recall["content"] = recall["content"]
        return recalls

    def batch_chart_search(self, queries, start_date, end_date, topn, filters):
        """图表搜索"""
        if start_date:
            date_obj = datetime.strptime(start_date, "%Y%m%d")
            filters["fromDate"] = date_obj.strftime("%Y-%m-%d")
        if end_date:
            date_obj = datetime.strptime(end_date, "%Y%m%d")
            filters["toDate"] = date_obj.strftime("%Y-%m-%d")
        headers = {"Content-Type": "application/json"}
        res = []
        for query in queries:
            input_data = {
                "query": query,
                "filters": filters,
                "from": 0,
                "size": 10,
                "user_id": "ssoadmin01",
                "search_type": "research",
                "search_scope": "chart",
                "time_sorted": "",
            }
            response = requests.post(
                url=self.search_url, headers=headers, json=input_data
            )
            results = response.json()["recall_docs"]
            for r in results:
                title = r["reportTitle"]
                link = f"https://fundmp.thfund.com.cn/#/ai/intelligentSearch/details/{r['reportId']}/research"
                if r["tableMarkdown"] is None:
                    continue
                output_dict = {
                    "title": title,
                    "link": link,
                    "content": (str(r["tableTitle"]) + "\n" + str(r["tableMarkdown"]))[
                        :4000
                    ],
                    "publishtime": r["publishTime"],
                    "fromSource": r["fromSource"],
                    "viewSource": "外部研报",
                }
                res.append(output_dict)
        return deduplicate_dict_list(res)

    def batch_local_search(
        self,
        queries,
        source,
        effect_start_date,
        effect_end_date,
        topn,
        inner_research_permission_level,
        filters,
        max_workers=5,
    ):
        """批量本地搜索"""
        three_month_ago = subtract_three_months(effect_end_date)
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(
                    self.local_search,
                    query,
                    source,
                    effect_start_date,
                    three_month_ago,
                    topn,
                    inner_research_permission_level,
                    filters,
                )
                for query in queries
            ]

            futures += [
                executor.submit(
                    self.local_search,
                    query,
                    source,
                    three_month_ago,
                    effect_end_date,
                    topn,
                    inner_research_permission_level,
                    filters,
                )
                for query in queries
            ]

            all_results = []
            for future in concurrent.futures.as_completed(futures):
                try:
                    results = future.result()
                    all_results.extend(results)
                except Exception as e:
                    print(f"Error in local search: {e}")
                    continue

        if source == "research":
            all_results.extend(
                self.batch_chart_search(
                    queries, effect_start_date, effect_end_date, 10, filters or {}
                )
            )

        link_groups = defaultdict(list)
        seen_chunks = set()

        for result in all_results:
            chunk_key = (result["link"], result.get("chunk_id", ""))
            if chunk_key not in seen_chunks:
                seen_chunks.add(chunk_key)
                link_groups[result["link"]].append(result)

        search_items = []
        for link, records in link_groups.items():
            sorted_records = sorted(records, key=lambda x: x.get("chunk_id", 0))
            combined_content = " ".join(r["content"] for r in sorted_records)

            if sorted_records:
                first_record = sorted_records[0]
                abstract = ""
                if first_record.get("viewSource", "") == "外部研报":
                    abstract = self.fetch_abstract(link)[:3000] + "\n\n"
                content = abstract + combined_content
                search_items.append(
                    {
                        "title": first_record.get("title", ""),
                        "link": link,
                        "content": content[:3000],
                        "publishedTime": first_record.get("publishtime", ""),
                        "hostname": first_record.get("fromSource", ""),
                        "source": first_record.get("viewSource", ""),
                    }
                )
        search_items.sort(
            key=lambda x: datetime.strptime(x["publishedTime"], "%Y-%m-%d %H:%M:%S"),
            reverse=True,
        )
        max_top = min(20, topn * len(queries) // 2)
        return search_items[:max_top]

    def each_web_search(self, query, timeRange="NoLimit", topn=10):
        """单次网页搜索"""
        query = rewrite_query(query)
        if timeRange not in ["OneDay", "OneWeek", "OneMonth", "OneYear", "NoLimit"]:
            timeRange = "NoLimit"
        params = {
            "engineType": "Generic",
            "contents": {
                "mainText": True,
                "markdownText": False,
                "summary": False,
                "rerankScore": True,
            },
        }
        params.update({"query": query, "timeRange": timeRange})
        headers = {
            "Authorization": f"Bearer {self.qwen_key}",
            "Content-Type": "application/json",
        }
        response = requests.post(
            self.qwen_url, headers=headers, data=json.dumps(params)
        )
        page_items = response.json()["pageItems"][:topn]
        results = []
        for item in page_items:
            if "mainText" in item and item["mainText"]:
                item["mainText"] = advanced_non_printable_filter(item["mainText"])
            title = item["title"]
            url = item["link"]
            main_text = item["mainText"]
            if main_text is None or len(main_text) <= 10:
                continue
            publishedTime = (
                convert_date_format(item["publishedTime"])
                if item["publishedTime"]
                else ""
            )
            output_dict = {
                "title": title,
                "link": url,
                "content": main_text[:2500],
                "publishedTime": publishedTime,
                "hostname": item["hostname"],
                "source": "互联网搜索",
            }
            results.append(output_dict)
        return [res for res in results if len(res["content"]) >= 10]

    def batch_web_search(
        self, queries, timeRange="NoLimit", topn=10, max_workers=5, dedup_field="link"
    ):
        """批量网页搜索"""
        output_list = []
        lock = Lock()
        seen_values = set()

        def process_single_query(query):
            try:
                results = self.each_web_search(query, timeRange, topn)
                with lock:
                    for result in results:
                        value = result.get(dedup_field)
                        if value and value not in seen_values:
                            seen_values.add(value)
                            output_list.append(result)
            except Exception as e:
                print(f"Error processing query '{query}': {str(e)}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_query = {
                executor.submit(process_single_query, query): query for query in queries
            }
            for future in concurrent.futures.as_completed(future_to_query):
                query = future_to_query[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"Query '{query}' generated an exception: {str(e)}")

        return filter_duplicate_items(output_list)


# ============ THSearch 类 - 对外接口 ============


class THSearch:
    """天弘搜索Skill - 对外接口类"""

    def __init__(self):
        self.sharesearch = AShareSearch()

    def unified_search(
        self,
        query,
        start_date="",
        end_date="",
        symbol=None,
        used_search_types=None,
    ):
        """统一搜索接口

        参数:
            query: 搜索查询词列表
            start_date: 起始日期 (YYYYMMDD)
            end_date: 截止日期 (YYYYMMDD)
            symbol: 股票代码列表
            used_search_types: 搜索类型列表 (research, roadshow, web, wechat, notice)

        返回值:
            dict: 搜索结果
        """
        if symbol is None:
            symbol = []
        if used_search_types is None:
            used_search_types = ["research", "roadshow", "web", "wechat"]

        if end_date == "" or not is_valid_yyyymmdd(end_date):
            today = date.today()
            end_date = today.strftime("%Y%m%d")
        if not is_valid_yyyymmdd(start_date):
            start_date = ""

        timeRange = "NoLimit"
        if start_date == "" or end_date == "":
            timeRange = "NoLimit"
            if end_date == "":
                end_date = date.today().strftime("%Y%m%d")
            if start_date == "":
                start_date = "20200101"
        else:
            today = date.today()
            today_str = today.strftime("%Y%m%d")
            date1 = datetime.strptime(today_str, "%Y%m%d").date()
            date2 = datetime.strptime(start_date, "%Y%m%d").date()
            delta = date1 - date2
            if delta.days <= 1:
                timeRange = "OneDay"
            elif delta.days <= 7:
                timeRange = "OneWeek"
            elif delta.days <= 30:
                timeRange = "OneMonth"
            elif delta.days <= 365:
                timeRange = "OneYear"
            else:
                timeRange = "NoLimit"

        topK = 3
        if len(query) <= 3:
            topK = 5
        results = []
        filters = {}
        if len(symbol) > 0:
            filter_symbols = []
            for each_symbol in symbol:
                if each_symbol != "":
                    filter_symbols.append(each_symbol)
                    filter_symbols.append(convert_wind_code(each_symbol))
                    if len(each_symbol) == 5:
                        sub_symbol = each_symbol[1:]
                        filter_symbols.append(sub_symbol)
                        filter_symbols.append(convert_wind_code(sub_symbol))
            if len(filter_symbols) > 0:
                filters = {"secCode": filter_symbols}

        valid_search_types = [
            t
            for t in used_search_types
            if t in ["research", "roadshow", "web", "wechat", "notice"]
        ]
        if not valid_search_types:
            valid_search_types = ["research", "roadshow", "web", "wechat"]

        logger.info(
            f"输入query：{query} 输入类型 {valid_search_types} 输入个股code {symbol}"
        )

        for search_type in valid_search_types:
            if search_type == "research":
                results.extend(
                    self.sharesearch.batch_local_search(
                        query, "research", start_date, end_date, 2 * topK, 2, filters
                    )
                )
            elif search_type == "roadshow":
                results.extend(
                    self.sharesearch.batch_local_search(
                        query,
                        "roadshow_meeting",
                        start_date,
                        end_date,
                        2 * topK,
                        2,
                        filters,
                    )
                )
            elif search_type == "notice":
                results.extend(
                    self.sharesearch.batch_local_search(
                        query, "notice", start_date, end_date, topK, 2, filters
                    )
                )

        results = results[:18]
        if "wechat" in valid_search_types:
            results.extend(
                self.sharesearch.wechat_search(query, start_date, end_date, topK)
            )
        results = results[:23]

        if len(results) <= 10:
            if len(query) <= 2:
                topK = 10
            else:
                topK = 3

        if "web" in valid_search_types:
            web_queries = []
            for each_query in query:
                web_queries.append(" ".join(symbol) + " " + each_query)
            web_search_results = self.sharesearch.batch_web_search(
                web_queries, timeRange, topn=topK, max_workers=5, dedup_field="link"
            )
            results.extend(web_search_results)

        results = results[:28]
        for result in results:
            result["content"] = remove_all_brackets_indices(result["content"])

        logger.info(f"输出：{query} 查询到 {len(results)} 条数据")

        if len(results) == 0:
            return {"data": results, "message": "无相关内容"}
        return {"data": results}

    def fetch_url(self, url):
        """获取URL内容

        参数:
            url: 需要获取全文的URL

        返回值:
            dict: 包含 data 和 url 字段的结果
        """
        try:
            res = self.sharesearch.fetch(url)[:30000]
            res = remove_all_brackets_indices(res)
        except Exception:
            res = "未能获取对应正文结果"
        return {"data": res, "url": url}

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
        """单一数据源搜索接口

        参数:
            query: 搜索词，可为空字符串（启动默认召回/标签搜索）
            search_type: 文档类别
                - research: 研报
                - weixin: 微信公众号
                - notice: 公告
                - roadshow_meeting: 路演会议
                - web: 互联网搜索（夸克搜索）
            search_scope: 搜索范围
                - all: 全文检索
                - title: 标题检索
            filters: 过滤条件字典，根据 search_type 不同有不同选项
            from_: 搜索起始位置
            size: 返回数量
            start_date: 起始日期 (YYYY-MM-DD 或 YYYYMMDD)
            end_date: 截止日期 (YYYY-MM-DD 或 YYYYMMDD)
            time_sorted: 排序方式
                - ASC: 时间升序
                - DESC: 时间降序

        返回值:
            dict: 包含 recall_docs 和 total_cnt 的结果
        """
        headers = {"Content-Type": "application/json"}

        # 处理日期格式
        from_date = ""
        to_date = ""
        if start_date:
            # 支持 YYYYMMDD 和 YYYY-MM-DD 两种格式
            if len(start_date) == 8 and start_date.isdigit():
                from_date = f"{start_date[:4]}-{start_date[4:6]}-{start_date[6:8]}"
            else:
                from_date = start_date
        if end_date:
            if len(end_date) == 8 and end_date.isdigit():
                to_date = f"{end_date[:4]}-{end_date[4:6]}-{end_date[6:8]}"
            else:
                to_date = end_date

        # 构建 filters
        if filters is None:
            filters = {}

        # 添加日期过滤
        if from_date:
            filters["fromDate"] = from_date
        if to_date:
            filters["toDate"] = to_date

        # web 类型使用夸克搜索
        if search_type == "web":
            return self._web_search_single(query, size)

        # 构建 请求数据
        input_data = {
            "query": query,
            "filters": filters,
            "from": from_,
            "size": size,
            "user_id": "ssoadmin01",
            "search_type": search_type,
            "search_scope": search_scope,
            "time_sorted": time_sorted,
        }

        try:
            response = requests.post(
                url=self.sharesearch.search_url, headers=headers, json=input_data
            )
            result = response.json()

            recall_docs = result.get("recall_docs", [])
            total_cnt = result.get("total_cnt", 0)

            # 格式化输出
            formatted_docs = []
            for doc in recall_docs:
                doc_id = doc.get("docId", "")
                doc_type = doc.get("docType", search_type)

                # 构建正确的链接格式
                link = f"https://fundmp.thfund.com.cn/#/ai/intelligentSearch/details/{doc_id}/{doc_type}"

                # 提取 highlightText 中的相关文字段落
                highlight_text = doc.get("highlightText", {})
                content_highlights = highlight_text.get("content", [])
                related_paragraphs = []
                for item in content_highlights:
                    text = item.get("text", "")
                    if text:
                        # 移除HTML高亮标签
                        clean_text = re.sub(r"<span[^>]*>|</span>", "", text)
                        related_paragraphs.append(clean_text)

                formatted_doc = {
                    "title": doc.get("title", ""),
                    "link": link,
                    "summary": doc.get("summary", "")[:3000] if doc.get("summary") else "",
                    "relatedParagraphs": related_paragraphs,
                    "publishedTime": doc.get("publishTime", "") or doc.get("publishDate", ""),
                    "hostname": doc.get("fromSource", "") or doc.get("orgName", ""),
                    "source": self._get_source_name(search_type),
                    "docId": doc_id,
                }
                formatted_docs.append(formatted_doc)

            return {
                "data": formatted_docs,
                "total_cnt": total_cnt,
            }
        except Exception as e:
            logger.error(f"single_search 错误: {e}")
            return {"data": [], "total_cnt": 0, "error": str(e)}

    def _web_search_single(self, query, size=20):
        """夸克搜索"""
        try:
            results = self.sharesearch.each_web_search(query, "NoLimit", size)
            return {
                "data": results,
                "total_cnt": len(results),
            }
        except Exception as e:
            logger.error(f"web_search 错误: {e}")
            return {"data": [], "total_cnt": 0, "error": str(e)}

    def _get_source_name(self, search_type):
        """获取数据源名称"""
        source_map = {
            "research": "券商研报",
            "weixin": "微信公众号",
            "notice": "公司公告",
            "roadshow_meeting": "路演会议",
            "web": "互联网搜索",
        }
        return source_map.get(search_type, search_type)
