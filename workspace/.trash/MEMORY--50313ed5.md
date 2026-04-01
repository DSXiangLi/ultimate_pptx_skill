# 龙虾智能体长期记忆

## 搜索能力使用规则

**重要**: 所有搜索功能必须使用 `th_search` 技能，不要直接使用 `web_search` 工具。

### 金融报告搜索
- **方法**: `unified_search`（默认）
- **说明**: 自动搜索全部数据源（研报、公告、路演、公众号、互联网）

### 网络搜索  
- **方法**: `unified_search --search-types "web"`
- **说明**: 仅搜索互联网数据源

### 使用示例
```bash
# 金融报告搜索
cd /home/jovyan/.openclaw/workspace/skills/th_search && python3 scripts/unified_search.py --query "公司 研报"

# 网络搜索  
cd /home/jovyan/.openclaw/workspace/skills/th_search && python3 scripts/unified_search.py --query "信息" --search-types "web"
```

## 项目配置
- **输出目录**: `/home/jovyan/.openclaw/workspace/outputs/`
- **核心能力**: 金融数据获取、图表生成、文档生成已验证可用