# MEMORY.md - 长期记忆

_这是你的长期记忆文件，记录重要的信息、决策和偏好。_

---

## 核心行为准则

**配置文件修改权限**：在未获得用户明确指令或同意的情况下，绝对禁止擅自修改系统配置文件（如 `openclaw.json`、`.env` 等）。提供指导和示例是可以的，但执行修改操作必须获得明确授权。

---

## 搜索规则

默认使用th_search技能

### 金融报告搜索（默认搜索全部数据源）

**命令：**
```bash
python scripts/unified_search.py --query "搜索关键词"
```

**特点：**
- 同时搜索多个数据源：券商研报、公司公告、路演会议、公众号、互联网
- 返回最相关的金融信息
- 适合查找投资研究资料

### 网络搜索（仅搜索互联网）

**命令：**
```bash
python scripts/unified_search.py --query "搜索关键词" --search-types "web"
```

**特点：**
- 仅搜索互联网公开信息
- 使用阿里通义搜索
- 适合查找实时新闻、通用信息

### 使用建议

| 场景 | 推荐命令 |
|------|----------|
| 查找研报/公告/路演 | `unified_search --query "关键词"`（默认） |
| 查找实时新闻 | `unified_search --query "关键词" --search-types "web"` |
| 获取全文内容 | `fetch_url --url "链接地址"` |

---

## 图片生成规则

默认使用 **volcengine-artist** 技能（火山云豆包大模型）

### 单图生成

**主题模式（自动优化Prompt）：**
```bash
python ~/skills/volcengine-artist/scripts/generate_image.py --topic "主题" --size "9:16" --output ./outputs/
```

**提示词模式（直接使用用户描述）：**
```bash
python ~/skills/volcengine-artist/scripts/generate_image.py --prompt "详细描述" --size "9:16" --no-watermark --output ./outputs/
```

### 批量生成

```bash
python ~/skills/volcengine-artist/scripts/generate_image.py --batch topics.json --output ./outputs/
```

### 直接调用API（无openai库时）

```bash
curl -s -X POST "${ARK_BASE_URL}/images/generations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${ARK_API_KEY}" \
  -d '{"model": "doubao-seedream-5-0-260128", "prompt": "描述", "size": "1440x2560", "response_format": "b64_json"}'
```

### 尺寸参数

| 比例 | 分辨率 | 适用场景 |
|------|--------|----------|
| 16:9 | 2560x1440 | PPT配图、横版海报 |
| 1:1 | 1920x1920 | 社交媒体头像 |
| 9:16 | 1440x2560 | 手机海报、竖版配图 |
| 4K | 3840x2160 | 高清大图 |

### 注意事项

- 火山云API要求图片至少 3,686,400 像素
- 系统环境无法访问外网pypi，openai库未安装，优先用curl直接调API
- 生成的图片URL有24小时有效期，需及时下载保存
- 使用 `response_format: "b64_json"` 可直接获取base64数据，避免下载链接过期问题

---
