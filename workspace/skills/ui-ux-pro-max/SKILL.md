---
name: ui-ux-pro-max
description: 'AI驱动的UI/UX设计智能技能。根据产品需求生成完整设计系统，包括UI风格、配色方案、字体搭配、落地页模式等。适用于需要设计美观界面的开发任务。触发条件：用户要求设计UI、生成设计系统、查询配色方案、选择字体风格等。'
metadata:
  {
    "openclaw": { "emoji": "🎨", "requires": { "tools": ["exec", "write"] } },
  }
---

# UI UX Pro Max - 设计智能技能

## 触发条件

当用户要求以下内容时激活此技能：
- "设计一个XXX的界面"
- "帮我生成设计系统"
- "查询UI风格"
- "推荐配色方案"
- "选择字体搭配"
- "设计落地页"

## 使用方法

### 通过 Python 脚本生成设计系统

```bash
# 生成设计系统（Markdown格式）
python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "产品类型" --design-system -p "产品名称" -f markdown

# 生成设计系统（ASCII格式）
python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "产品类型" --design-system -p "产品名称" -f ascii

# 指定域名搜索
python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "glassmorphism" --domain style
python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "elegant serif" --domain typography
python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "dashboard" --domain chart

# 保存到文件
python3 ~/.openclaw/workspace/skills/ui-ux-pro-max/src/ui-ux-pro-max/scripts/search.py "fintech" --design-system -p "MyApp" --persist
```

## 数据库资源

| 资源类型 | 数量 | 说明 |
|----------|------|------|
| UI 风格 | 67种 | Glassmorphism, Neumorphism, Minimalism 等 |
| 配色方案 | 161套 | 行业特定配色 |
| 字体搭配 | 57种 | Google Fonts 集成 |
| 图表类型 | 25种 | Chart.js, Recharts, D3.js |
| 落地页模式 | 24种 | 转化优化结构 |
| UX 指南 | 99条 | 最佳实践和反模式 |

## 输出示例

```markdown
## Design System: 我的银行App

### Pattern
- **Name:** Trust & Authority
- **Sections:** Hero > Features > CTA

### Style
- **Name:** Exaggerated Minimalism
- **Best For:** Banks, finance, fintech

### Colors
| Role | Hex |
|------|-----|
| Primary | #2563EB |
| Secondary | #3B82F6 |
| CTA | #F97316 |

### Typography
- **Heading:** IBM Plex Sans
- **Body:** IBM Plex Sans
```

## 技术栈支持

- React, Next.js, shadcn/ui
- Vue, Nuxt.js, Nuxt UI
- Svelte, Astro
- SwiftUI
- React Native, Flutter
- HTML + Tailwind (默认)

## 依赖工具

- `exec`：执行 Python 脚本
- `write`：生成设计系统文档
