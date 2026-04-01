# TH Search 技能测试说明

## 问题诊断

当前th_search技能无法正常工作，原因是缺少必要的环境变量配置：

1. `TH_MCP_BASE_URL` - 用于unified_search和web类型的single_search
2. `TH_DOCSEARCH_URL` - 用于single_search（非web类型）

当前环境变量状态：
- `TH_MCP_BASE_URL`: 未设置
- `TH_DOCSEARCH_URL`: 设置为占位符值 "your_docsearch_url_here"

## 解决方案

要正确配置th_search技能，请按照以下步骤操作：

### 1. 获取正确的URL值

联系系统管理员或查看相关文档，获取以下服务的实际URL：

- MCP服务基础URL（例如：`https://mcp.example.com/api`）
- DocSearch服务URL（例如：`https://docsearch.example.com/search`）

### 2. 设置环境变量

#### 方法A: 临时设置（当前会话有效）
```bash
export TH_MCP_BASE_URL="https://your-mcp-base-url.com"
export TH_DOCSEARCH_URL="https://your-docsearch-url.com"
```

#### 方法B: 永久设置（推荐）
在`/home/jovyan/.openclaw/workspace/.env`文件中添加：
```env
TH_MCP_BASE_URL=https://your-mcp-base-url.com
TH_DOCSEARCH_URL=https://your-docsearch-url.com
```

然后在openclaw.json的env.vars部分添加这些变量，或者确保系统能够加载.env文件。

### 3. 测试th_search技能

配置完成后，可以使用以下命令测试：

#### unified_search（推荐默认使用）
```bash
cd /home/jovyan/.openclaw/workspace/skills/th_search/scripts
python unified_search.py --query "测试查询词"
```

#### single_search（特定数据源）
```bash
# 搜索券商研报
python single_search.py --query "贵州茅台" --search-type research

# 搜索互联网内容
python single_search.py --query "NBA比赛结果" --search-type web
```

#### fetch_url（获取URL内容）
```bash
python fetch_url.py --url "https://example.com/article"
```

## 使用建议

根据SKILL.md文档：

- **默认搜索**: 使用`unified_search`，它会同时搜索多个数据源（研报、公告、路演、公众号、互联网）
- **特定需求**: 使用`single_search`指定单一数据源和过滤条件
- **获取全文**: 使用`fetch_url`从搜索结果的链接获取完整内容

## 注意事项

- unified_search支持多个查询词同时搜索，用逗号分隔
- single_search支持精细过滤条件（如按行业、报告类型等）
- 搜索结果内容会被截取，如需全文请使用fetch_url