# 搜索能力使用规则

## 默认搜索策略

### 金融报告搜索
- **技能**: `th_search`
- **方法**: `unified_search`（默认）
- **说明**: 自动搜索全部数据源（研报、公告、路演、公众号、互联网），返回最相关结果

### 网络搜索  
- **技能**: `th_search`
- **方法**: `unified_search --search-types "web"`
- **说明**: 仅搜索互联网数据源，用于通用信息检索

## 使用示例

```bash
# 金融报告搜索（默认）
cd /home/jovyan/.openclaw/workspace/skills/th_search && python3 scripts/unified_search.py --query "世纪华通 研报"

# 网络搜索（指定web数据源）
cd /home/jovyan/.openclaw/workspace/skills/th_search && python3 scripts/unified_search.py --query "世纪华通 股票代码" --search-types "web"
```

## 配置说明
- 所有搜索功能统一通过 `th_search` 技能实现
- 避免直接使用 `web_search` 工具（可能存在网络限制）
- `unified_search` 是首选方法，支持多查询词和自动数据源选择