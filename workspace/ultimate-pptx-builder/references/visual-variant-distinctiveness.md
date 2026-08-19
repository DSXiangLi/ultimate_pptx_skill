# 视觉语言差异契约

## 适用范围

本文件约束同一内容在不同视觉语言下的变体验证。视觉语言只描述页面如何被表达；业务场景、会议类型、风险复盘、策略更新等都属于 `narrative_intent`。

## 字段契约

使用：

```json
{
  "narrative_intent": "strategy_update",
  "visual_language": "terminal-cockpit"
}
```

废弃字段：

```json
{
  "visual_variant": "dense-risk-review"
}
```

## 当前视觉语言

| visual_language | 视觉含义 | 不承载 |
|---|---|---|
| `matte-institutional` | 克制发光、正式网格、哑光玻璃、紧凑台账指标 | 投委会/正式会议语义 |
| `luminous-glass` | 高光能量、聚光光球、发光面板、主视觉 KPI | 战略会/路演语义 |
| `terminal-cockpit` | 终端网格、密集驾驶舱、状态 chips、监控来源带 | 风险评审语义 |

## 固定项与可变项

固定项：

```text
slide_count
topology_sequence
titles/body/metrics/chart_data/source/risk
narrative_intent
native_text_fingerprint
```

可变项：

```text
visual_language
visual_grammar
palette/material/typography/motif/container/chart_table_treatment/source_band_treatment
```

## 阻断代码

| Code | 阻断条件 |
|---|---|
| `VISUAL_NARRATIVE_COUPLING` | 视觉语言名称或坐标包含业务场景/叙事任务术语 |
| `LEGACY_VISUAL_VARIANT` | 契约仍使用 `visual_variant` |
| `WEAK_COORDINATE_REALIZATION` | 坐标没有物化为 PPTX 对象角色或样式差异 |
| `COMPONENT_GRAMMAR_UNCHANGED` | 容器、图表、表格、页脚/来源带语法未变化 |
| `VISUAL_VARIANT_DISTANCE_TOO_LOW` | 两个视觉语言签名过近 |
| `CONTENT_FINGERPRINT_DRIFT` | 用不同内容伪装成视觉差异 |

## 验收命令

```bash
python3 scripts/check_narrative_visual_orthogonality.py
python3 scripts/validate_glass_variants.py
```

发布条件：

| Gate | 条件 |
|---|---|
| field separation | `narrative_intent` 与 `visual_language` 均存在，且无 legacy 字段 |
| same-content base | 使用 `examples/variants/glass-fintech-visual-language-base.contract.json` |
| content fingerprint | 所有视觉语言中的幻灯片/原生文本指纹一致 |
| grammar distance | 视觉语言改变了可见组件语法 |
| rendered evidence | contact sheet 显示视觉语言层面的差异 |
| validator result | 两个命令均返回 pass |

## 修复路径

- 业务词进入视觉语言：迁移到 `narrative_intent`，并重命名视觉语言。
- 差异只来自颜色：增加容器、排版、材料、图表/表格或 source band 语法差异。
- 内容指纹漂移：回到同一 base contract，不用不同案例证明视觉语言。
- PPTX 对象无差异：更新 compiler/exporter，让坐标变化写入 IR 和 PPTX 对象。
