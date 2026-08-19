# 叙事与视觉扩展运行契约

## 适用范围

本文件约束 `ultimate-pptx-builder` 在扩展叙事能力和视觉锚点时的运行方式。它不是开发计划，也不记录方案选择历史。

## 编译链路

```text
content_contract
→ narrative_kernel
→ narrative_rules
→ visual_anchor
→ controlled_visual_language
→ pptx_material_policy
→ executable_qa_gates
```

## 必需产物

新增或修改叙事/视觉扩展时，同步维护以下文件：

| 能力 | 产物 | 验证命令 |
|---|---|---|
| 叙事内核 | `references/narrative-kernel.md`, `schemas/narrative-kernel.schema.json`, `examples/narrative-kernel.finance.json` | `python3 scripts/check_narrative_safety.py <contract>` |
| 视觉锚点 | `references/visual-anchor-system.md`, `schemas/visual-anchor.schema.json`, `examples/visual-anchors/*.anchor.json` | `python3 scripts/check_visual_anchor.py <anchor> <deck.ir.json>` |
| 视觉语言差异 | `references/visual-variant-distinctiveness.md`, `examples/variants/*.contract.json` | `python3 scripts/check_narrative_visual_orthogonality.py && python3 scripts/validate_glass_variants.py` |
| 多系统泛化 | `references/visual-system-generalization.md`, `examples/*style.json` | `python3 scripts/validate_visual_systems.py` |

## Narrative Kernel Contract

每个 deck contract 必须声明：

```yaml
audience_job: decision | understanding | persuasion | memory
scenario: string
expected_after_state: string
slides:
  - narrative_job: hero_thesis | chart_focus | matrix | scenario | process | action_plan | compliance
    claim: string
    evidence: list
    takeaway: string
    source_risk: list
```

阻断代码由 `check_narrative_safety.py` 输出，包括但不限于：

| Code | 含义 |
|---|---|
| `MISSING_AUDIENCE_JOB` | 缺少受众/场景/期望结果 |
| `MISSING_NARRATIVE_JOB` | 幻灯片缺少主要叙事任务 |
| `TITLE_NOT_CLAIM` | 关键页标题不是结论或行动主张 |
| `CLAIM_WITHOUT_EVIDENCE` | 主张无数据、理由或来源支撑 |
| `EVIDENCE_WITHOUT_TAKEAWAY` | 数据存在但缺少解读 |
| `ARC_GAP` | deck 缺少开场、证据、转折/风险、解决/行动链路 |
| `MISSING_RISK_OR_SOURCE` | 金融主张缺少来源或风险说明 |

## Visual Anchor Contract

每个视觉锚点必须声明：

```yaml
id: glass-fintech-pptx
immutable_dna: []
mutable_coordinates: {}
mutation_operators: []
density_modes: {}
page_role_variants: {}
material_policy: {}
anti_drift_rules: []
qa_gates: []
```

最低接受标准：

| Gate | 发布条件 |
|---|---|
| anchor schema | JSON/schema 通过 |
| immutable DNA | 删除任一核心 DNA 后样式可识别度下降 |
| controlled coordinates | 视觉变化来自坐标，不来自业务场景改名 |
| PPTX material policy | 关键文本和数据保持 native/editable |
| rendered evidence | `.pptx` 渲染图显示可见差异 |
| regression | layout/text/editability/visual gates 通过 |

## Controlled Variation Contract

同一内容基础上验证至少三种视觉语言：

```text
matte-institutional × same_narrative_intent
luminous-glass × same_narrative_intent
terminal-cockpit × same_narrative_intent
```

固定项：slide count、拓扑序列、标题、正文、指标、图表数据、来源/风险、`narrative_intent`。

可变项：`visual_language`、visual grammar、panel/material/typography/palette/motif/chart treatment/source-band treatment。

## 发布命令

```bash
python3 scripts/check_narrative_safety.py examples/glass-fintech-benchmark.contract.json
python3 scripts/check_visual_anchor.py examples/visual-anchors/glass-fintech-pptx.anchor.json build/validation-phase1.ir.json
python3 scripts/check_narrative_visual_orthogonality.py
python3 scripts/validate_glass_variants.py
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

## 失败处理

- 叙事失败：修复 content contract 或 narrative kernel，不通过视觉装饰掩盖缺失主张/证据/收束。
- 视觉语言耦合：重命名或重建 `visual_language`，业务任务放入 `narrative_intent`。
- 变体距离不足：修改组件语法、材料、排版、图表/表格处理或 source/risk band，而不是只换色。
- 可编辑性失败：调整 material policy 或 exporter，关键文本/数据不进入 raster。
