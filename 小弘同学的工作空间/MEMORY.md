# MEMORY.md - 长期记忆

_这是你的长期记忆文件，记录重要的信息、决策和偏好。_

---

## 核心行为准则

**配置文件修改权限**：在未获得用户明确指令或同意的情况下，绝对禁止擅自修改系统配置文件（如 `openclaw.json`、`.env` 等）。提供指导和示例是可以的，但执行修改操作必须获得明确授权。

**子智能体超时设置**：使用 `sessions_spawn` 启动子智能体时，超时时间 `timeoutSeconds` 必须设置为至少 **30分钟（1800秒）**，避免子智能体因超时过早终止任务。

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

## PPT生成规则

### 技术选型

| 操作 | 工具 |
|------|------|
| 创建新 PPT / 复杂排版 | **pptxgenjs** (Node.js) |
| 读/改文本、提取内容 | python-pptx |

> ⚠️ **绝对不要用 python-pptx 创建新 PPT** — 三次重写全部排版错乱，根因是 EMU 坐标与文本渲染尺寸不可控。换 pptxgenjs 一次通过。

```bash
# pptxgenjs v4 已全局安装
NODE_PATH=$(npm root -g) node script.js
```

### 字体/字号/布局/配色

**每次制作 PPT 前，用 `ui-ux-pro-max` 技能查询设计系统：**

```bash
python3 ~/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "产品类型/主题" --design-system -p "项目名" -f markdown
```

根据返回的 Style / Colors / Typography 决定本次的具体设计参数，不要复用上次的配色和字体。

### 布局约束（防溢出）⚠️

- **16:9 幻灯片尺寸：10 × 5.625 英寸。** 所有元素的 (x+w, y+h) 必须在此范围内。这是硬约束，每次设置坐标前先心算确认。
- ❌ 任何元素底部 `y + h > 5.3"`（留 0.3" 底边距）
- ❌ 任何元素右边 `x + w > 9.8"`（留 0.2" 右边距）
- ❌ 封面/总结页尤其容易溢出：用 `x:0, y:0, w:'100%', h:'100%'` 铺满背景后，容易忘记页面只有 5.625" 高。封面上所有文字（包括日期、来源等附属信息）必须落在 5.3" 以内
- ❌ 第一个内容元素 y < 0.3"（标题从 0.3" 起，不要贴着顶边）
- ✅ 元素之间 y 间距 ≥ 0.1"
- ✅ 生成脚本后自检：逐页逐个元素口算 `y + h` 和 `x + w`，确保全部在边界内

### 避坑清单

- ❌ hex 颜色**不带 `#`**：`'FF0000'` ✅，`'#FF0000'` ❌
- ❌ 不重用 option 对象（pptxgenjs 会原地修改），用工厂函数
- ❌ 不加 `breakLine: true` 导致多行文本粘连
- ❌ 在 ROUNDED_RECTANGLE 上叠加 accent 条（边角不齐）
- ❌ 同一个 slide 放 >3 个图表（视觉噪音）
- ❌ 标题下画装饰线（AI味太浓，用留白/颜色替代）
- ❌ 正文居中（左对齐！居中只用于封面/评级页的标题）
- ❌ 单系列图表保留 legend（`showLegend: false`）
- ❌ 饼图/环形图不设 `showPercent: true`
- ❌ 垂直网格线不关（`catGridLine: { style: 'none' }`）

---

## 文档与图表生成规则

### 中文字体检查（必做）

生成图表、PDF、Word 文档时，**必须先检查系统中可用的中文字体**，使用对应字体避免乱码。

**检查命令：**
```bash
fc-list :lang=zh
```

**Python 使用示例：**
```python
from PIL import ImageFont
# 图表使用无衬线字体
font = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 16)
```

---