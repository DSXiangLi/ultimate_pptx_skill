# 布局与文本安全契约

## 适用范围

本文件定义 Slide IR 在导出/渲染前必须通过的布局与文本安全规则。判定由 `scripts/check_layout_safety.py` 执行。

## 命令

```bash
python3 scripts/check_layout_safety.py \
  <workdir>/build/deck.ir.json \
  --report <workdir>/verification/layout-report.json
```

示例：

```bash
python3 scripts/check_layout_safety.py \
  build/glass-fintech-benchmark/glass-fintech-benchmark.ir.json \
  --report build/glass-fintech-benchmark/glass-fintech-benchmark-layout-safety-report.json
```

脚本遇到阻断项时返回非零状态。

## 报告字段

```json
{
  "issue_count": 0,
  "blocking_count": 0,
  "release_decision": "pass",
  "issues": []
}
```

## 关键角色

以下角色按业务关键内容处理：

```text
title, body, risk, source, footnote, metric, metric-note, table, chart
```

背景、光球等装饰可按设计出血；装饰性页码仍需检查，因为它可能与标题碰撞或形成模板感。

## 默认阈值

| Rule | Default | 阻断条件 |
|---|---:|---|
| side/top safe zone | 48 px | priority>=4 或关键对象违反侧边/顶部边距 |
| bottom safe zone | 64 px | 关键 text/chart/table/metric/card 进入底部不安全区域 |
| footer separation | 16 px above footer rail | 非页脚内容进入页脚分隔带 |
| table columns | 5 core fields | 金融表格核心字段过多，无法保持 PPT 可读 |
| compliance body paragraphs | max 4 | 合规/适当性页变成密集文档页 |
| title length | 34 chars | 标题过长，不适合单行金融演示标题 |
| text capacity | CJK-aware heuristic | priority>=4 文本高度不足 |
| table row height | 38 px | 金融表格行高过小 |
| container gap | 14 px | 视觉容器过近，warning |
| container overlap | 2% / 4 px | 非装饰容器重叠，blocking |
| title/content gap | 34 px | 标题带离首个内容容器太近 |
| title/text gap | 12 px | 标题命中框离优先级文本太近 |
| title orphan line | 4 weighted chars | 标题最后一行过短 |
| alignment tolerance | 8 px | 同行/成对容器破坏预期网格 |
| protected-term wrap | term-specific | 断行落入受保护中文术语内部 |
| page-number area | 1.2% slide area | 装饰页码成为主导母题 |
| long-deck page-number repetition | 35% slides | 过大页码母题在过多幻灯片重复 |
| title/decor gap | 56 px | 标题扩展框与页码装饰相交 |

## 文本容量模型

检查器使用保守 CJK 估算：

```text
CJK char width ~= 1em
ASCII char width ~= 0.55em
Office/LibreOffice CJK scale ~= 1.30x
usable line width = box width * 0.88
multi-line native text line height = font size * 1.38 + padding
```

失败时优先调整文案、字号、文本框或布局语法；不要用 rasterized text 绕过检查。

## 发布条件

| Gate | 条件 |
|---|---|
| exit code | `check_layout_safety.py` 返回 0 |
| report | `release_decision == pass` |
| blockers | `blocking_count == 0` |
| exceptions | 例外必须写入用户可读验证记录 |
| rerun | 修复后同一命令重新通过 |

## 阻断代码

常见阻断项：

```text
BOTTOM_SAFE_ZONE
FOOTER_SEPARATION
TEXT_OVERFLOW_RISK
PROTECTED_TERM_WRAP_RISK
TITLE_ORPHAN_WRAP
TITLE_TEXT_GAP_TOO_SMALL
CONTENT_ROW_TOP_MISALIGNMENT
CARD_ROW_EDGE_MISALIGNMENT
TITLE_DECOR_COLLISION
OVERSIZED_PAGE_NUMBER
TABLE_TOO_MANY_COLUMNS
COMPLIANCE_TEXT_DENSITY
TABLE_CELL_OVERFLOW_RISK
CONTAINER_OVERLAP
```

## 修复路径

- `TEXT_OVERFLOW_RISK`：缩短文本、扩大 box、降低密度或调整页面拓扑。
- `BOTTOM_SAFE_ZONE` / `FOOTER_SEPARATION`：移动内容、扩大 footer rail 或调整安全区。
- `TITLE_DECOR_COLLISION`：移动装饰/页码或降低标题长度。
- `TABLE_*`：拆分表格、减少核心列、提高行高或改成摘要卡片。
- `CONTAINER_OVERLAP`：修复 layout grammar 或 component contract；透明/后景不豁免。
