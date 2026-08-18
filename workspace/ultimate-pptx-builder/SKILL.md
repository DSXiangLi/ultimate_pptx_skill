---
name: ultimate-pptx-builder
description: Use when creating high-end editable PowerPoint decks from rich visual concepts, HTML-like previews, financial narratives, programmable design systems, or existing PPTX files/templates that need cloning into reusable editable visual systems. Builds PPTX through Slide IR, native PowerPoint export, reverse-compilation, and executable QA gates.
version: 0.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [pptx, powerpoint, editable-decks, html-to-pptx, design-systems, qa]
    related_skills: [powerpoint, hermes-agent-skill-authoring, writing-plans]
---

# Ultimate PPTX Builder

## 运行原则

- 以 `Slide IR` 作为事实源；HTML 只用于预览、布局探针或视觉对照。
- 关键业务文本、数据、来源、风险提示保持原生可编辑；低优先级复杂材质才允许 raster/vector island。
- 每次交付同时产出 `.pptx`、渲染图、IR/spec/report/manifest；没有证据包不算完成。
- 视觉系统改动服务于可复用 PPTX 生成能力，不为单个 deck 做一次性补丁。
- QA 由脚本判定阻断项；正文不维护手工 checklist。

## 输入归一化

先把用户输入归一为一个工作目录，至少包含以下字段或文件：

```text
workdir/
  input/
    source.md | source.json | source.pptx | references/*
  spec/
    content-contract.json
    style-program.json
  build/
  verification/
  manifest.json
```

`content-contract.json` 至少写入：`audience`、`scenario`、`business_goal`、`narrative_jobs`、`data/source/risk fields`、`editability_priorities`。涉及金融内容时，不补造数字、来源、收益承诺或交易指令。

## 路线选择

| 场景 | 路线 | 首读文件 | 主要命令 |
|---|---|---|---|
| 从内容/视觉概念生成可编辑 PPTX | forward compiler | `references/architecture.md`, `references/authoring-contract.md` | `compile_spec_to_ir.py` → `render_ir_html.py` → `export_ir_pptx.py` → `run_qa.py` |
| 从现有 PPTX 学习可复用视觉系统 | reverse compiler / cloner | `references/pptx-cloner.md` | `run_pptx_cloner_loop.py` |
| 扩展或评估样式锚点 | visual system validation | `references/style-program.md`, `references/visual-dna-model.md` | `validate_glass_showcase.py`, `validate_glass_benchmark.py`, `validate_visual_systems.py` |
| 调查布局/文本/组件缺陷 | layout QA | `references/layout-text-safety.md`, `references/component-layout-contract-gate.md` | `check_layout_safety.py`, `check_component_layout_contract.py`, `check_rendered_perceptual_layout.py` |
| 修改技能本身 | skill maintenance | `references/acceptance-matrix.md` | `validate_skill.py` |

## 标准工作流

### 1. 建立内容契约

```bash
python3 scripts/compile_spec_to_ir.py \
  <workdir>/spec/content-contract.json \
  <workdir>/build/deck.ir.json
```

生成的 IR 必须包含稳定 `id`、`type`、`role`、`box`、`z`、`editability`、`render_policy`。关键对象 priority 使用 `4` 或 `5`。

### 2. 应用样式程序

使用或扩展 `examples/*.style.json`。新增样式时同步更新：

```text
examples/<style>.style.json
examples/visual-anchors/<style>.anchor.json
references/style-program.md
references/visual-dna-model.md
```

新增样式不以换色为充分差异；图表、表格、卡片、页脚/来源区、排版和页面骨架都要体现视觉 DNA。

### 3. 生成 HTML 预览和 PPTX

```bash
python3 scripts/render_ir_html.py \
  <workdir>/build/deck.ir.json \
  <workdir>/build/preview.html

python3 scripts/export_ir_pptx.py \
  <workdir>/build/deck.ir.json \
  <workdir>/build/deck.pptx \
  --report <workdir>/verification/export-report.json
```

HTML 节点通过 `data-ir-id` 回链到 IR。PPTX 导出报告记录每个对象的实际物化形式、可编辑性、fallback 和阻断项。

### 4. 执行 QA 与发布门禁

按产物类型运行对应脚本；脚本输出的 `release_decision`、`blocking_issues`、`blocking_count` 是发布判定源。

| 目标 | 命令 |
|---|---|
| 基础技能完整性 | `python3 scripts/validate_skill.py` |
| Office package | `python3 scripts/check_pptx_package.py <deck.pptx>` |
| 综合 QA | `python3 scripts/run_qa.py <deck.ir.json> <export-report.json> <qa-report.json> --pptx <deck.pptx>` |
| 布局/文本安全 | `python3 scripts/check_layout_safety.py <deck.ir.json> --report <layout-report.json>` |
| 组件布局契约 | `python3 scripts/check_component_layout_contract.py <deck.ir.json> --report <component-report.json>` |
| 视觉保真度 | `python3 scripts/run_visual_fidelity.py <deck.ir.json> <deck.pptx> <visual-report.json> --workdir <workdir>/visual-fidelity` |
| OOXML/渲染属性 | `python3 scripts/check_ooxml_visual_properties.py <deck.pptx> --report <ooxml-report.json>` |
| 多视觉系统 | `python3 scripts/validate_visual_systems.py` |

发布前把报告路径写入 `manifest.json`：

```json
{
  "deck": "build/deck.pptx",
  "ir": "build/deck.ir.json",
  "preview": "build/preview.html",
  "renders": "build/rendered/",
  "reports": [
    "verification/export-report.json",
    "verification/qa-report.json",
    "verification/layout-report.json"
  ],
  "release_decision": "pass|fail|pass_with_accepted_exceptions"
}
```

## Reverse Compiler / PPTX Cloner

用户提供现有 PPTX 或模板库样本时，先运行克隆验收循环：

```bash
python3 scripts/run_pptx_cloner_loop.py \
  <source.pptx> \
  --deck-id <deck-id> \
  --out <workdir>/specimens/<deck-id> \
  --require-render \
  --max-iterations 3
```

只在当前阶段报告 `release_decision: pass` 后推进下一阶段。`--skip-render` 只用于本地渲染不可用的开发测试，不能作为视觉抽象或样式学习证据。

克隆路线的产物顺序：

```text
source.pptx
→ specimen analysis pack
→ decompiled raw Slide IR
→ rebuilt PPTX + fidelity/editability report
→ layout archetypes + visual DNA + component contracts
→ reusable generator + benchmark/gate promotion
```

## 样式锚点与回归验证

第一个生产级样式锚点先跑完整 glass fintech 线：

```bash
python3 scripts/validate_glass_showcase.py
python3 scripts/validate_glass_benchmark.py
python3 scripts/check_narrative_visual_orthogonality.py
python3 scripts/validate_glass_variants.py
python3 scripts/validate_visual_systems.py
```

视觉变体要保持 `narrative_intent` 与 `visual_language` 解耦。若 rendered contact sheet 近似相同，即使 schema、fidelity 或 editability 分数通过，也按生成/样式系统缺陷处理并补脚本门禁。

## 失败处理

- 脚本报告阻断项：修复源 spec、style program、compiler/exporter 或 QA gate 后重跑同一命令。
- 渲染图显示重叠、截断、字体异常、图表过小或页脚拥挤：先定位到 IR/renderer/export/QA 哪一层，再补可复用门禁，不只改当前坐标。
- PPTX 在 Office/WPS 与截图同时异常：默认视为生成/布局 bug，直到证据证明是软件差异。
- 克隆 fidelity 受不支持对象限制：查阅对应 `references/pptx-cloner-c3-*.md`，把修复沉淀为 object coverage、materialization policy 或 component contract。
- 技能文档、参考文档或脚本契约发生变化：运行 `python3 scripts/validate_skill.py`，并只提交本轮修改。

## 参考文件索引

| 需要处理 | 参考文件 |
|---|---|
| IR、编译边界、对象策略 | `references/architecture.md`, `references/slide-ir-schema.md`, `references/conversion-rules.md` |
| 可编辑性与 Office 实用性 | `references/editability-policy.md`, `references/pptx-capability-matrix.md` |
| 样式系统与视觉 DNA | `references/style-program.md`, `references/style-glass-fintech-pptx.md`, `references/visual-dna-model.md` |
| 布局、文本、组件门禁 | `references/layout-text-safety.md`, `references/text-spacing-and-alignment-qa.md`, `references/component-layout-contract-gate.md` |
| Cloner / 逆向编译 | `references/pptx-cloner.md`, `references/pptx-cloner-c3-object-coverage-roadmap.md`, `references/pptx-cloner-c3-materialization-policy.md` |
| 评估与发布 | `references/qa-loop.md`, `references/acceptance-matrix.md`, `references/ooxml-and-rendered-perceptual-qa.md` |

## 技能维护规则

- `SKILL.md` 保持为当前执行手册，不放历史迭代、方案解释、长 checklist 或旧版本对比。
- 可机器判断的规则放入 `scripts/`、schema、示例 fixture 或 validator；正文只保留命令入口和失败处理。
- 复杂背景、研究、学习笔记放入 `docs/learning/` 或 `research/`，不作为运行时必读文件。
- 每轮语义修改先保留 checkpoint，结束时精确 staging、验证、提交并推送。
