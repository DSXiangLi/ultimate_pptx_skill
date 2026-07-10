# Component Contract DSL + Authored Layout Graph Validation

Date: 2026-07-10

## Scope

This validation records Phase A of the PPTX deep-optimization roadmap:

1. Component Contract DSL schema/engine/tests.
2. Atlas route-map contract migration from hard-coded component checks to declarative DSL.
3. Authored layout graph evidence in generated Atlas IR.
4. Formal validation through `validate_visual_systems.py` and `validate_skill.py`.

## Files added or changed

- `schemas/component-contract.schema.json`
- `examples/component-contracts/atlas-route-map.contract.json`
- `scripts/check_component_contracts.py`
- `scripts/check_component_layout_contract.py`
- `scripts/compile_spec_to_ir.py`
- `scripts/validate_skill.py`
- `tests/test_component_contract_dsl.py`
- `tests/test_authored_layout_graph.py`
- `references/component-contract-dsl.md`
- `references/authored-layout-graph.md`
- `research/2026-07-10-pptx-deep-optimization-roadmap.md`

## Acceptance results

### A1 — Component Contract DSL

Command:

```bash
python3 -m unittest tests/test_component_contract_dsl.py -v
python3 scripts/check_component_contracts.py \
  build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json \
  --contracts examples/component-contracts \
  --report verification/atlas-component-contract-dsl-report.json
```

Result:

```text
OK
PASS component contract DSL
```

The bad fixture blocks:

- `ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION`
- `ATLAS_FLOATING_BADGE_COVERS_CARD`
- `ATLAS_GUARDRAIL_TEXT_ORPHANED`
- `ATLAS_FOOTER_GUARDRAIL_COLLISION`

The good fixture passes with `blocking_count=0`.

### A2 — Atlas component gate migration

Command:

```bash
python3 -m unittest tests/test_component_layout_contract.py tests/test_component_contract_dsl.py -v
python3 scripts/validate_visual_systems.py
```

Result:

```text
OK
PASS visual systems same_content=1 count=3 glass-fintech-pptx score=94.95 edit=100.00; paper-analyst-report score=95.46 edit=100.00; market-atlas-infographic score=95.65 edit=100.00
```

`check_component_layout_contract.py` keeps the public gate name `component_layout_contract`, but now reports:

```json
{
  "engine": "component_contract_dsl",
  "contracts": ["atlas-route-map"]
}
```

### A3 — Authored layout graph evidence

Command:

```bash
python3 -m unittest tests/test_authored_layout_graph.py -v
```

Result:

```text
OK
```

Current Atlas IR now declares:

```json
"component_contract_refs": ["atlas-route-map"]
```

And slides `ls02`/`ls03` carry `layout_graph.components`:

- `ls02`: `macro-budget-route-map`, contract `atlas-route-map`
- `ls03`: `allocation-bridge-route-map`, contract `atlas-route-map`

The graph only keeps actual generated object IDs; it is evidence, not wishful declaration.

### A4 — Formal skill validation

Command:

```bash
python3 scripts/validate_skill.py
```

Result:

```text
ALL CHECKS PASSED
```

`validate_skill.py` now requires the new schema/example/reference/script/test files and runs:

- `tests/test_component_contract_dsl.py`
- `tests/test_authored_layout_graph.py`

## Release decision

Phase A is accepted for workspace after the following gates passed:

- Component DSL unit tests
- Existing component layout regression tests
- Authored layout graph tests
- `validate_visual_systems.py`
- `validate_skill.py`

Remaining future phases:

- Phase B: Visual DNA realization gate
- Phase C: OOXML property audit + rendered perceptual QA
- Phase D: Finance PPTX benchmark corpus
