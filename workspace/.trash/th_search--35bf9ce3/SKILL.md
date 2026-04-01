---
name: th_search
description: "天弘搜索技能，提供多数据源统一搜索和URL内容获取能力。用于：金融信息检索、研报搜索、公告查询、新闻搜索、路演会议查询、公众号文章搜索、网页内容抓取。"
metadata:
  category: search
  data_sources:
    - research
    - roadshow
    - web
    - wechat
    - notice
---

# 天弘搜索技能

提供统一搜索接口，支持多数据源检索，以及 URL 内容获取功能。

## 核心原则

**unified_search 是默认首选**：当不确定使用哪个功能时，优先使用 unified_search。它会同时搜索多个数据源（研报、公告、路演、公众号、互联网），返回最相关的结果。

**single_search 用于特定需求**：当你明确知道要搜索哪个数据源，或需要使用精细过滤条件（如按行业、报告类型、评级等筛选）时使用。

---

## 什么时候使用哪个功能？

| 场景 | 推荐功能 | 说明 |
|------|----------|------|
| **默认搜索** | unified_search | 不确定时首选，自动搜索全部数据源 |
| 快速搜索多个主题 | unified_search | 支持多个查询词同时搜索，一次调用获取多个主题 |
| 查找特定数据源 | single_search | 指定单一数据源搜索，支持精细过滤条件 |
| 按行业/类型筛选研报 | single_search | 使用filter参数过滤行业、报告类型、评级等 |
| 获取搜索结果的全文 | fetch_url | 从搜索结果的link获取完整内容 |
| 抓取外部网页内容 | fetch_url | 获取任意URL的正文内容 |

---

## 使用技巧

### 技巧1：写财报点评时如何搜索

写财报点评时，建议组合使用多种搜索方式：

```bash
# 第一步：用unified_search快速获取全貌（推荐首选）
python scripts/unified_search.py --query "贵州茅台 年报,贵州茅台 业绩,贵州茅台 财报" --start-date 20250101

# 第二步：如需更详细的业绩点评研报，用single_search过滤
python scripts/single_search.py --query "贵州茅台" --search-type research --filter reportSubType=业绩点评

# 第三步：搜索公告类型的财报（重要！）
python scripts/single_search.py --query "贵州茅台 年度报告" --search-type notice --filter fromDate=2024-01-01 --filter toDate=2026-03-05

# 第四步：如需获取原文，用fetch_url
python scripts/fetch_url.py --url "搜索结果中的link"
```

# 第三步：如需获取原文，用fetch_url
python scripts/fetch_url.py --url "搜索结果中的link"
```

### 技巧2：搜索特定行业研报

```bash
# 搜索轻工制造行业的行业研究
python scripts/single_search.py --query "" --search-type research --filter industryL1=轻工制造 --filter reportType=行业研究

# 搜索食品饮料行业的行业点评
python scripts/single_search.py --query "" --search-type research --filter industryL1=食品饮料 --filter reportSubType=行业点评
```

### 技巧3：多数据源对比搜索

```bash
# 一次搜索多个相关主题，对比不同来源的观点
python scripts/unified_search.py --query "白酒行业,茅台估值,白酒动销"
```

---

## 功能列表

| 功能 | 脚本 | 用途 |
|------|------|------|
| unified_search | `python scripts/unified_search.py --query "..."` | 多数据源统一搜索（快速检索） |
| single_search | `python scripts/single_search.py --query "..." --search-type research` | 单一数据源搜索（精细过滤） |
| fetch_url | `python scripts/fetch_url.py --url "..."` | 获取URL全文内容 |

---

## 详细说明

### 1. unified_search - 统一搜索

多数据源统一搜索接口，**支持多个查询词同时搜索**，一次调用可获取多个主题的相关信息。

**用法:**
```bash
python scripts/unified_search.py --query "查询词1,查询词2,查询词3" [--start-date YYYYMMDD] [--end-date YYYYMMDD] [--symbol 股票代码] [--search-types 类型]
```

**参数说明:**

| 参数 | 短参数 | 必填 | 默认值 | 说明 |
|------|--------|------|--------|------|
| --query | -q | 是 | - | **搜索查询词，多个用逗号分隔，支持同时搜索多个主题** |
| --start-date | -s | 否 | 不限 | 起始日期，格式：YYYYMMDD |
| --end-date | -e | 否 | 今天 | 截止日期，格式：YYYYMMDD |
| --symbol | -S | 否 | 不限 | 股票代码，多个用逗号分隔 |
| --search-types | -t | 否 | **全部类型** | 搜索类型，**通常不需要指定，默认搜索全部数据源** |

**多查询词说明:**

- 支持 1-8 个查询词同时搜索
- 多个查询词用英文逗号分隔，如：`"贵州茅台,白酒行业,人工智能"`
- 结果会合并返回，按相关性和时间排序
- **推荐**: 一次性规划所有需要的查询词，避免多次调用

**--search-types 枚举值（通常不需要指定，默认搜索全部）:**

| 值 | 说明 | 适用场景 | 数据来源 |
|----|------|----------|----------|
| research | 券商研报 | 查找个股/行业研究报告、投资观点、深度分析 | 外部券商研报库 |
| roadshow | 路演会议 | 查找公司调研、业绩说明会、电话会议纪要 | 路演会议记录 |
| web | 互联网搜索 | 查找实时新闻、公告、行业动态、通用信息 | 阿里通义搜索 |
| wechat | 精选公众号 | 查找财经类公众号文章、市场评论 | 微信公众号 |
| notice | 公司公告 | 查找上市公司公告、财报、重大事项 | 交易所公告 |

**示例:**
```bash
# 基本搜索（默认搜索全部数据源，推荐）
python scripts/unified_search.py --query "贵州茅台"

# 多个查询词同时搜索（推荐）
python scripts/unified_search.py --query "贵州茅台,白酒行业,人工智能"

# 指定股票代码和时间范围
python scripts/unified_search.py --query "业绩,财报" --symbol "600519" --start-date "20240101" --end-date "20241231"

# 仅搜索互联网（特殊场景使用）
python scripts/unified_search.py --query "人工智能,大模型" --search-types "web"
```

---

### 2. single_search - 单一数据源搜索

更灵活的单一数据源搜索接口，支持精细的过滤条件和搜索范围控制。

**用法:**
```bash
python scripts/single_search.py --query "搜索词" --search-type research [可选参数]
```

**参数说明:**

| 参数 | 短参数 | 必填 | 默认值 | 说明 |
|------|--------|------|--------|------|
| --query | -q | 否 | "" | 搜索查询词（可为空，启用默认召回） |
| --search-type | -t | 否 | research | 数据源类型 |
| --search-scope | -s | 否 | all | 搜索范围（all/title） |
| --start-date | | 否 | 不限 | 起始日期（YYYY-MM-DD 或 YYYYMMDD） |
| --end-date | | 否 | 不限 | 截止日期（YYYY-MM-DD 或 YYYYMMDD） |
| --from | | 否 | 0 | 起始位置（分页用） |
| --size | | 否 | 10 | 返回数量 |
| --filter | -f | 否 | 无 | 过滤条件，格式: key=value（可多次使用） |

**--search-type 枚举值:**

| 值 | 说明 | 特有过滤字段 |
|----|------|--------------|
| research | 券商研报 | reportType, reportSubType, orgName, secCode, author, industryL1, currentRating |
| weixin | 微信公众号 | flag, fromSource, author, chainName |
| notice | 公司公告 | noticeType, noticeSubType, industryL1/2/3, fromMarket, secCode, isImportant |
| roadshow_meeting | 路演会议 | meetingType, meetingTopic, speakerType, status, organizer |
| web | 互联网搜索（夸克） | - |

**--filter 详细说明:**

**research（券商研报）常用过滤字段:**

| 字段 | 说明 | 常用值示例 |
|------|------|----------|
| reportType | 报告类型 | 见下方研报类型列表 |
| reportSubType | 报告子类型 | 见下方研报子类型列表 |
| industryL1 | 一级行业 | 见下方行业列表 |
| currentRating | 评级 | 买入, 增持, 持有, 中性 |
| orgName | 券商机构 | 中信证券, 华泰证券, 中金公司 |
| secCode | 股票代码 | 600519, 000858 |
| author | 作者 | 分析师姓名 |

**reportType（研报类型）:**

| 类型 | 子类型 (reportSubType) |
|------|----------------------|
| 宏观经济 | 中国经济, 海外经济 |
| 投资策略 | 债券策略, 市场策略, 行业策略, 金工策略, 基金策略, 新三板策略 |
| 行业研究 | 行业动态, 行业定期, 行业深度, 行业点评 |
| 公司研究 | 业绩点评, 事件点评, 公司深度, 新股研究, 首次覆盖, 调研纪要 |
| 晨会纪要 | 早间资讯, 晨会纪要 |
| 金融工程 | 动态点评（金工）, 金工定期, 金工深度 |
| 债券研究 | 债券定期, 债券深度, 动态点评（债券） |
| 基金研究 | 基金定期, 基金深度, 动态点评（基金） |
| 期货研究 | 商品期货, 金融期货 |
| 期权研究 | - |
| 外汇研究 | - |
| 新三板研究 | 新三板定期 |

**industryL1（一级行业）:**

农林牧渔、电力设备、食品饮料、医药生物、家用电器、纺织服饰、轻工制造、美容护理、社会服务、石油石化、煤炭、有色金属、基础化工、建筑材料、钢铁、机械设备、环保、公用事业、建筑装饰、交通运输、房地产、银行、非银金融、汽车、电子、计算机、通信、国防军工、传媒、电力设备及新能源、综合

**notice（公司公告）常用过滤字段:**

| 字段 | 说明 | 常用值示例 |
|------|------|----------|
| noticeType | 公告类型 | 见下方A股/港股公告类型列表 |
| noticeSubType | 公告子类型 | 见下方公告子类型列表 |
| industryL1/2/3 | 行业分类 | 食品饮料/白酒/白酒 |
| fromMarket | 市场 | 上交所, 深交所, 北交所, 港交所 |
| secCode | 股票代码 | 600519, 000858 |
| isImportant | 是否重要 | Y, N |

**A股公告类型 (noticeType):**

| 类型 (noticeType) | 子类型 (noticeSubType) |
|------|----------------------|
| 财务报告 | 业绩预告, 业绩快报, 季度报告, 半年报告, 年度报告, 补充更正 |
| 重大事项 | 利润分配, 股份增减持, 资金投向, 资产重组, 收购兼并, 重大合同, 股权激励, 关联交易, 借贷担保, 违纪违规, 政策影响, 人事变动, 委托理财 |
| 交易提示 | 澄清公告, 停牌提示, 交易异动, 风险提示, 特别处理, 终止上市, 恢复上市, 暂停上市 |
| 招股 | 申报稿, 招股说明书, 发行定价, 申报反馈, 发行结果, 上市公告书 |
| 配股 | 配股预案, 配股说明书, 配股获取, 配股发行, 配股上市 |
| 增发 | 增发预案, 增发说明书, 增发获准, 增发发行, 增发上市 |
| 股权股本 | 权益变动, 股本变动, 质押冻结, 押式回购, 回购股权, 约定购回, 股权分置改革 |
| 一般公告 | 员工持股, 法律纠纷, 产销经营快报, ESG报告, 董事会公告, 函件, 股东大会, 权证公告 |

**港股公告类型 (noticeType):**

| 类型 (noticeType) | 子类型 (noticeSubType) |
|------|----------------------|
| 公告及通函 | 杂项, 财务资料, 公司变动, 须公布的交易, 关联交易, 会议/表决, 新上市, 重大事项 |
| 上市文件 | 发售现有证券, 介绍上市, 资本化发行, 供股, 公开招股, 发售以供认购, 预览资料, 聆讯资料 |
| 财务报告 | 年度报告(HK), 中期报告(HK), 季度报告(HK), 环境及管治报告, 其它上市文件 |
| 债券及结构性产品 | 债务证券公告, 权证上市, 权证公告 |
| 业绩快报(HK) | 业绩发布会, 末期业绩, 中期业绩, 季度业绩, 业绩预告(HK) |
| 股权股本 | 翌日报表, 证券/股本, 权益变动, 交易披露 |
| 港交所基金 | ETF交易数据, ETF发行上市 |
| 其他 | 创业板资料, 监管者公告, 宪章文件, 版本及聆讯资料, 月报表, 委任代表表格, 交易安排, 一般公告 |

**--filter 使用示例:**
```bash
# 过滤研报类型
--filter reportType=公司研究 --filter currentRating=买入

# 过滤行业研究
--filter reportType=行业研究

# 过滤行业点评
--filter reportSubType=行业点评

# 过滤特定行业的行业研究
--filter industryL1=轻工制造 --filter reportType=行业研究

# 过滤行业
--filter industryL1=食品饮料

# 过滤日期范围
--filter fromDate=2024-01-01 --filter toDate=2024-12-31

# 过滤公告类型
--filter noticeType=财务报告 --filter isImportant=Y
```

**示例:**
```bash
# 搜索研报（默认）
python scripts/single_search.py --query "贵州茅台" --search-type research

# 搜索公告
python scripts/single_search.py --query "业绩" --search-type notice

# 互联网搜索（夸克）
python scripts/single_search.py --query "贵州茅台 最新消息" --search-type web

# 标题检索
python scripts/single_search.py --query "茅台" --search-type research --search-scope title

# 指定时间范围
python scripts/single_search.py --query "业绩" --search-type notice --start-date "2024-01-01" --end-date "2024-12-31"

# 使用过滤条件 - 公司研究
python scripts/single_search.py --query "" --search-type research --filter reportType=公司研究 --filter currentRating=买入

# 使用过滤条件 - 行业研究
python scripts/single_search.py --query "" --search-type research --filter reportType=行业研究

# 使用过滤条件 - 行业点评
python scripts/single_search.py --query "" --search-type research --filter reportSubType=行业点评

# 使用过滤条件 - 特定行业的行业研究
python scripts/single_search.py --query "" --search-type research --filter industryL1=轻工制造 --filter reportType=行业研究

# 分页获取更多结果
python scripts/single_search.py --query "茅台" --search-type research --from 10 --size 10
```

---

### 3. fetch_url - URL内容获取

通用爬虫方法，给定URL获取对应全文内容。支持内部文档系统和外部网页。

**用法:**
```bash
python scripts/fetch_url.py --url "URL地址"
```

**参数说明:**

| 参数 | 短参数 | 必填 | 说明 |
|------|--------|------|------|
| --url | -u | 是 | 需要获取全文的完整URL |

**支持的URL类型:**

| URL特征 | 数据来源 | 说明 |
|---------|----------|------|
| `fundmp.thfund.com.cn` (含research) | 券商研报 | 获取研报全文 |
| `fundmp.thfund.com.cn` (含notice) | 公司公告 | 获取公告全文 |
| `fundmp.thfund.com.cn` (含allRoadShow) | 路演会议 | 获取会议纪要全文 |
| `fundmp.thfund.com.cn` (含meetingComments) | 内部研报 | 获取天弘内部研报全文 |
| `fundmp.thfund.com.cn` (含wxOfficial) | 公众号 | 获取公众号文章全文 |
| 其他URL | 外部网页 | 通过jina.ai抓取网页内容 |

**示例:**
```bash
# 获取外部网页
python scripts/fetch_url.py --url "https://example.com/article"

# 获取研报全文（从搜索结果中的link）
python scripts/fetch_url.py --url "https://fundmp.thfund.com.cn/#/ai/intelligentSearch/details/xxx/research"
```

---

## 返回数据格式

### unified_search 返回格式

```
找到 3 条结果:

--- 结果 1 ---
标题: 贵州茅台2024年年度报告
来源: 上交所 (公司公告)
时间: 2024-03-28 18:00:00
链接: https://fundmp.thfund.com.cn/#/ai/intelligentSearch/announcement/details/xxx/notice
内容: 公司2024年度实现营业收入...

--- 结果 2 ---
标题: 贵州茅台深度研究报告
来源: 中信证券 (券商研报)
时间: 2024-03-15 10:00:00
链接: https://fundmp.thfund.com.cn/#/ai/intelligentSearch/details/xxx/research
内容: 公司作为高端白酒龙头...
```

**返回字段说明:**

| 字段 | 说明 |
|------|------|
| title | 文章/报告标题 |
| link | 原文链接（可用于fetch_url获取全文） |
| content | 内容摘要（截取前3000字符） |
| publishedTime | 发布时间 |
| hostname | 来源名称 |
| source | 数据源类型（券商研报/公司公告/互联网搜索等） |

### fetch_url 返回格式

```
URL: https://fundmp.thfund.com.cn/#/ai/intelligentSearch/details/xxx/research

内容:
[研报全文内容...]
```

---

## 注意事项

### 股票代码格式

| 市场 | 格式 | 示例 |
|------|------|------|
| A股（沪市） | 6位数字，以6开头 | 600519 |
| A股（深市） | 6位数字，以0或3开头 | 000001, 300750 |
| A股（北交所） | 6位数字，以8或4开头 | 830799 |
| 港股 | 5位或4位数字 | 00700, 3690 |

### 日期格式

- 格式：`YYYYMMDD`
- 示例：`20240101`, `20241231`
- 不限制时间时可省略 start-date 和 end-date 参数

### 搜索词建议

1. **简洁明了**: 使用2-5个核心关键词，避免完整句子
2. **包含主体**: 确保包含查询的主体实体（公司名、行业名等）
3. **避免模糊词**: 禁止使用"最近动态"、"股价走势"、"最新消息"等无效词汇
4. **禁止高级运算符**: 不要使用 `site:`、`inurl:` 等搜索运算符

### 返回限制

- 每个结果内容截取前500字符
- single_search 默认返回10条结果
- unified_search 最多返回28条结果
- 如需全文，使用 fetch_url 获取

---

## 常见问题

### 搜索结果为空

```
消息: 无相关内容
```

**可能原因:**
1. 搜索词过于模糊或具体
2. 时间范围限制过窄
3. 股票代码不正确

**解决方案:**
1. 尝试更换搜索词
2. 扩大时间范围或去掉时间限制
3. 确认股票代码格式正确

### fetch_url 获取失败

```
内容: 未能获取对应正文结果
```

**可能原因:**
1. URL需要登录权限
2. 页面需要动态渲染
3. 网络超时

**解决方案:**
1. 确认URL是否可公开访问
2. 尝试其他URL
