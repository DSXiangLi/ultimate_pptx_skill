# Ultimate PPTX Builder 深度优化路线图与验收矩阵

> 日期：2026-07-10
> 目标：把当前 `ultimate-pptx-builder` 从“多风格 PPTX 生成 + 一组 gate”升级为 finance-grade PPTX visual compiler：组件语法、布局图、视觉 DNA、OOXML 转换证据、真实渲染感知 QA、benchmark corpus 全部可执行。

## 设计原则

1. **不再只靠局部坐标修复。** 任何重复出现的视觉缺陷都要抽象为 contract/gate。
2. **不把 HTML 当 source of truth。** Source of truth 是 Content Contract + Visual DNA + Component Contract + Slide IR。
3. **不接受浅层换皮。** 风格差异必须落到 chart/table/card/process/footer/typography 等信息承载组件。
4. **不相信单层验证。** IR 几何、PPTX OOXML、真实渲染 PNG、人工/视觉审查各有职责。
5. **不通过删除业务信息或压缩业务字号过 gate。** `政策VETO`、风险/来源、限制/回撤、结论/动作必须保留。

---

## Phase A — Component Contract DSL + Authored Layout Graph

### A1. Component Contract DSL validator

**目标**：把 `check_component_layout_contract.py` 中硬编码的 Atlas route-map 经验，抽象为可声明、可测试的 DSL。

**产物**：

- `schemas/component-contract.schema.json`
- `examples/component-contracts/atlas-route-map.contract.json`
- `scripts/check_component_contracts.py`
- `tests/test_component_contract_dsl.py`
- `references/component-contract-dsl.md`

**最小 DSL 能力**：

- component root / selector
- slots with relative box ratios or named anchors
- slot membership by object id pattern / role / component tag
- forbidden overlap between slots
- conditional overlap for small status badge
- min gap to footer / external rail
- report fields compatible with existing component layout contract gate

**验收**：

```bash
python3 -m unittest tests/test_component_contract_dsl.py -v
python3 scripts/check_component_contracts.py tests/fixtures/component_contract_bad.ir.json --contracts examples/component-contracts --report /tmp/component-contract-bad.json
python3 scripts/check_component_contracts.py tests/fixtures/component_contract_good.ir.json --contracts examples/component-contracts --report /tmp/component-contract-good.json
```

要求：

- bad fixture 必须 fail，并命中 bottom-band / badge / footer gap 类 blocker。
- good fixture 必须 pass。
- 不依赖视觉模型，不依赖 PPTX render。

### A2. Atlas route-map contract migration

**目标**：将 Atlas route-map 的 slot/overlap 规则迁移到 DSL，同时保留现有 regression codes。

**产物**：

- `examples/component-contracts/atlas-route-map.contract.json`
- `scripts/check_component_layout_contract.py` 变为调用 DSL engine 或共享 engine
- `verification/component-contract-dsl-validation.md`

**验收**：

```bash
python3 scripts/check_component_layout_contract.py build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json --report /tmp/atlas-component-layout.json
python3 scripts/check_component_contracts.py build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json --contracts examples/component-contracts --report /tmp/atlas-component-dsl.json
python3 scripts/validate_visual_systems.py
```

要求：

- Atlas 当前 build：两个 gate 都 pass / blocking_count=0。
- 历史 bad fixture：DSL gate fail。
- Glass/Paper 不被 Atlas contract 误伤。

### A3. Authored Layout Graph evidence

**目标**：让 compiler 生成关系证据，而不是完全靠 `check_alignment_graph.py` 后验推断。

**产物**：

- IR metadata 增加 `layout_graph` 或 `component_contract_refs`
- Atlas route-map / signal-field / process-state-map 至少有 authored graph evidence
- `references/authored-layout-graph.md`

**验收**：

```bash
python3 scripts/compile_spec_to_ir.py ...
python3 scripts/check_alignment_graph.py build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json --report /tmp/alignment.json
python3 scripts/validate_visual_systems.py
```

要求：

- 每页 `layout_relations` 非空。
- Atlas 复杂组件有 authored relation / contract ref evidence。
- checker 报告能说明哪些关系是 authored，哪些是 inferred。

### A4. Formal release integration + installed skill sync

**目标**：workspace 与 installed skill 均可执行 Phase A。

**验收**：

```bash
cd /home/lixiang/workspace/ultimate-pptx-builder && python3 scripts/validate_visual_systems.py && python3 scripts/validate_skill.py
cd /home/lixiang/.hermes/skills/productivity/ultimate-pptx-builder && python3 scripts/validate_visual_systems.py && python3 scripts/validate_skill.py
```

要求：

- 两边均 `ALL CHECKS PASSED`。
- `validate_skill.py` 检查新文件、测试、reference。

---

## Phase B — Visual DNA Realization Gate

**目标**：防止风格退化为背景/配色/装饰枚举。

**产物**：

- `scripts/check_visual_dna_realization.py`
- `references/visual-dna-realization-gate.md`
- IR metadata 中的 `visual_dna_evidence`

**验收**：

```bash
python3 scripts/check_visual_dna_realization.py build/visual-system-same-content.json --report /tmp/visual-dna.json
python3 scripts/validate_visual_systems.py
```

要求：

- 至少检查 typography、container、component、data-viz、footer/source、layout archetype 六层 evidence。
- 能阻断 `DECORATION_ONLY_VARIANT`、`DATA_VIZ_GRAMMAR_SHARED`、`COMPONENT_GRAMMAR_SHARED`。

---

## Phase C — OOXML Property Audit + Rendered Perceptual QA

**目标**：解决“IR/HTML 正确但 PPTX XML 或实际渲染丢失效果”的转换可信度问题。

**产物**：

- `scripts/check_ooxml_visual_properties.py`
- `scripts/check_rendered_perceptual_layout.py`
- `references/ooxml-property-audit.md`
- `references/rendered-perceptual-qa.md`

**验收**：

```bash
python3 scripts/check_ooxml_visual_properties.py build/.../*.pptx --ir build/.../*.ir.json --report /tmp/ooxml.json
python3 scripts/check_rendered_perceptual_layout.py build/.../visual-fidelity/actual --ir build/.../*.ir.json --report /tmp/rendered-layout.json
```

要求：

- alpha/line-spacing/font fallback/stroke alpha 等关键属性有 XML-level assertion。
- rendered QA 至少输出 edge pressure、density map、footer pressure、title pressure。

---

## Phase D — Finance PPTX Benchmark Corpus

**目标**：防止当前 compiler 对 3 个 demo 过拟合。

**产物**：

- `examples/benchmarks/*.contract.json`
- `scripts/validate_finance_benchmark_corpus.py`
- `references/finance-benchmark-corpus.md`

**验收**：

```bash
python3 scripts/validate_finance_benchmark_corpus.py
python3 scripts/validate_skill.py
```

要求：

- 覆盖投委会、基金对比、宏观月报、风险归因、回撤复盘、客户路演、合规披露等场景。
- 覆盖 cover/summary/chart/table/matrix/scenario/process/risk/action/compliance 拓扑。
- 至少跑 same-content cross-style 与 same-style cross-content 两类验证。

---

## 当前执行批次

本批次只执行 **Phase A1 → A4**。Phase B/C/D 先保留为后续验收路线，避免一次变更跨越过大导致不可回滚。
