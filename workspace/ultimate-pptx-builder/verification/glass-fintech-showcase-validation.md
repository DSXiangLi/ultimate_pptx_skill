# Glass Fintech Showcase Validation Record

## Scope

Validate the first deep style anchor: `glass-fintech-pptx`.

The goal is not to add many style presets. The goal is to prove one style can run end-to-end with strong native editability, visual fidelity artifacts, and a fix-and-reverify loop.

## Deliverables

- `examples/glass-fintech-pptx.style.json`
- `examples/glass-fintech-showcase.contract.json`
- `references/style-glass-fintech-pptx.md`
- `scripts/validate_glass_showcase.py`
- enhanced native glass simulation in:
  - `scripts/compile_spec_to_ir.py`
  - `scripts/render_ir_html.py`
  - `scripts/render_ir_png.py`
  - `scripts/export_ir_pptx.py`
- `docs/learning/glass-fintech-showcase.md`

## RED Gate

`validate_skill.py` was first updated to require glass-fintech files before they existed.

Result:

```text
FAIL: missing required files: references/style-glass-fintech-pptx.md, docs/learning/glass-fintech-showcase.md, examples/glass-fintech-pptx.style.json, examples/glass-fintech-showcase.contract.json, scripts/validate_glass_showcase.py
```

This confirmed the new acceptance gate detects missing showcase implementation.

## GREEN Gate

Command:

```bash
python3 scripts/validate_glass_showcase.py
```

Initial pass:

```text
PASS glass-fintech showcase score=95.24 editability=100.00
```

## Visual QA Fix Loop

A separate visual QA pass inspected actual LibreOffice-rendered PNGs and found:

- ghost page numbers were too strong and interfered with metric cards;
- metric delta text sat too close to card bottoms;
- footer risk text was too small, dark, and low;
- slide 3 title wrapping was unbalanced.

Fixes applied:

- reduced and moved ghost page numbers;
- increased muted text brightness to `B6C7D8`;
- increased metric card height and moved delta text upward;
- moved risk rail upward, increased height, and increased risk text size;
- widened/reduced action-slide title sizing.

Reverification:

```bash
python3 scripts/validate_glass_showcase.py
```

Result:

```text
PASS glass-fintech showcase score=95.63 editability=100.00
```

## Native Chart Upgrade

A second RED→GREEN loop added a priority-5 financial chart to the same `glass-fintech-pptx` style line instead of adding more style presets.

### RED

`validate_glass_showcase.py` was tightened to require:

- at least one chart in `examples/glass-fintech-showcase.contract.json`;
- at least one compiled IR object with `type: chart`;
- chart `render_policy: native-vector-group` and editability priority 5;
- export audit `actual: editable-vector-chart`.

Observed failures moved through the expected stack:

```text
FAIL glass showcase: glass showcase must include at least one financial chart contract
FAIL glass showcase: glass showcase needs at least one editable chart object
FAIL glass showcase: PPTX export audit failed
```

### GREEN

Implemented:

- chart data semantics in the glass content contract;
- compiler output for `type: chart` with categories, series, unit and source;
- HTML chart preview with `data-ir-id` traceability;
- Pillow reference chart rendering;
- PPTX export as editable vector group of native shapes/text, not raster;
- chart audit in export report.

Result:

```text
PASS glass-fintech showcase score=95.61 editability=100.00
chart actual=editable-vector-chart
```

Visual QA found the first chart version looked too much like a small decorative widget. Fixes applied:

- removed internal production wording from slide copy;
- enlarged chart area from 448×150 to 448×208;
- added 0/50/100% axis labels;
- added horizontal legend;
- added last-period data labels;
- added formal source note;
- localized the chart title to a finance presentation style.

## Unified Validation

Command:

```bash
python3 scripts/validate_skill.py
```

Result:

```text
PASS required files: 39 present
PASS skill frontmatter
PASS acceptance criteria present
PASS JSON parseability
PASS minimal IR policy
PASS style policy
PASS Phase 1 compiler output
PASS Phase 2 HTML traceability
PASS Phase 3 PPTX export audit
PASS Phase 4B visual fidelity
PASS Phase 4 QA report
PASS glass-fintech showcase
ALL CHECKS PASSED
```

## Decision

Status: **PASS**

Current glass showcase metrics:

```text
glass_visual_score=95.61
glass_editability=100.00
glass_qa_fidelity=95.61
chart_actual=editable-vector-chart
slides=3
```

## Remaining Known Limits

- Glass blur is simulated with native translucent shapes, strokes, glow orbs, and shadows; true blur is not yet promised.
- Reference rendering remains IR/Pillow, not browser screenshot, because the environment lacks Chromium/Playwright.
- Chart objects are currently editable vector groups of native shapes/text, not full Office chart XML with embedded workbook data.
