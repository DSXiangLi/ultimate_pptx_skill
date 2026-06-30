# Glass Fintech 15-Slide Benchmark Validation

## Scope

Validate the `glass-fintech-pptx` long-form benchmark as a realistic finance deck, not only a showcase. The benchmark now includes executable layout/text safety gates in addition to fidelity and editability checks.

## Benchmark Input

`examples/glass-fintech-benchmark.contract.json`

The contract simulates a realistic investment/strategy user request with:

- audience and scenario
- macro assumptions
- asset-allocation views
- sector/style exposure
- risk budget and stress scenarios
- execution path
- compliance/risk notes
- one `narrative_job` per slide

## Deck Output

`build/glass-fintech-benchmark/glass-fintech-benchmark.pptx`

## Mandatory Gates

```bash
python3 scripts/check_layout_safety.py build/glass-fintech-benchmark/glass-fintech-benchmark.ir.json \
  --report build/glass-fintech-benchmark/glass-fintech-benchmark-layout-safety-report.json
python3 scripts/validate_glass_benchmark.py
python3 scripts/validate_skill.py
```

## Current Result

```text
PASS glass benchmark slides=15 score=96.01 editability=100.00 layout=pass
PASS required files: 44 present
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
PASS glass-fintech benchmark
ALL CHECKS PASSED
```

## Metrics

| Metric | Result |
|---|---:|
| slides | 15 |
| visual fidelity | 96.01 |
| editability | 100.00 |
| practicality | 100.00 |
| layout safety | pass |
| layout blocking issues | 0 |
| editable vector charts | 4 |
| editable vector tables | 2 |

## Layout/Text Safety Rules Now Enforced

`check_layout_safety.py` blocks long-form benchmark release if any of these fail:

- 64px bottom safe zone for critical text/chart/table/metric/card objects
- 16px footer separation band above risk/source rail
- CJK-aware Office-like text capacity for priority >=4 text
- protected-term wrap risk checks for Chinese short terms such as 风险预算/评审版本/现金流/触发器/出海链条
- title orphan-wrap checks and title-to-text gap checks
- alignment grid checks for chart-focus rows, metric-card rows, and action-page card/body spans
- max 5 core columns for finance PPT tables
- compliance/suitability page max 4 body paragraphs
- table row/cell readability checks
- explicit native text leading / line-height safety
- visual container overlap and unapproved nested double-panel checks
- title-to-first-content gap checks
- title/page-number collision checks
- oversized/repeated page-number motif checks

## Issues Found and Mechanized

Earlier visual review found that fidelity/editability could pass while the deck still had:

- bottom cards and footers visually too close
- over-prominent repeated page-number motif
- dense table/compliance pages
- potential text overflow under PowerPoint font metrics
- CJK short terms split across lines even when the box-level capacity check passed
- title orphan wraps and card/body edge misalignment
- AI-template repetition from excessive card/glow/page-number grammar

These are now partly enforced by executable gates, not only written as guidance. Remaining design taste issues still require rendered-page review, but layout and text capacity have blocking system checks.

## Representative Artifacts

- PPTX: `build/glass-fintech-benchmark/glass-fintech-benchmark.pptx`
- Layout report: `build/glass-fintech-benchmark/glass-fintech-benchmark-layout-safety-report.json`
- QA report: `build/glass-fintech-benchmark/glass-fintech-benchmark-qa-report.json`
- Contact sheet: `build/glass-fintech-benchmark/visual-fidelity/actual/contact-sheet-final-alignment-cjk.png`

## Current Limitations

- Layout safety is IR-based, not a full PowerPoint textbox overflow detector.
- LibreOffice rendering may differ from user-local PowerPoint rendering.
- AI-template smell is partially encoded through repeated large page-number checks, but true design taste still needs visual QA/rubric review.
- Full Office-native chart/table XML is still future work; current benchmark uses editable vector chart/table groups.
