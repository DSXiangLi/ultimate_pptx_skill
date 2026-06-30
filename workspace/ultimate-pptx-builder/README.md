# Ultimate PPTX Builder

Workspace-local skill prototype for IR-first, editable, high-fidelity PPTX generation.

## Core Pipeline

```text
Content Contract → Slide IR → HTML Preview → PPTX Export → Visual Fidelity → QA Report
```

## Primary Showcase

The first deep style anchor is `glass-fintech-pptx`:

```bash
python3 scripts/validate_glass_showcase.py
```

Current acceptance target:

- at least 3 slides
- no `rasterIsland` in the MVP glass showcase
- all critical title/body/metric/risk text native and editable
- at least one priority-5 financial chart exported as editable vector chart, not raster
- visual fidelity score >= 88
- editability score >= 95

## 15-Slide Narrative Benchmark

The same style anchor now has a realistic investment-committee benchmark deck:

```bash
python3 scripts/validate_glass_benchmark.py
```

Current benchmark target:

- exactly 15 slides from simulated finance-user input
- multiple presentation modes: cover, summary, dashboard, chart focus, table, matrix, scenario, process, timeline, quote, compliance, action plan
- at least 4 editable vector charts
- at least 2 editable vector tables
- no raster fallback in the benchmark MVP path
- visual fidelity score >= 88
- editability score >= 95

## Validate Everything

```bash
python3 scripts/validate_skill.py
```

The validator checks:

- required files
- skill frontmatter
- acceptance criteria presence
- JSON parseability
- minimal IR editability policy
- style program policy, including `glass-fintech-pptx`
- Phase 1 content contract → IR compiler
- Phase 2 IR → HTML preview traceability
- Phase 3 IR → editable PPTX export audit
- Phase 4B visual fidelity loop
- Phase 4 QA report using measured visual fidelity
- glass-fintech end-to-end showcase
- glass-fintech 15-slide benchmark deck

## Learning Notes

Before changing an area with prior discoveries, read `docs/learning/` first. Add a new note whenever development reveals and resolves an issue.

Current notes:

- `docs/learning/phase4b-visual-rendering.md`
- `docs/learning/glass-fintech-showcase.md`

## Status

Phase 0-4B plus the first deep style showcase and 15-slide benchmark are complete when `python3 scripts/validate_skill.py` passes.
