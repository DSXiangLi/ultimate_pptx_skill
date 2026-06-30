# Skill Installation Validation Record

## Scope

Install and update the workspace-local `ultimate-pptx-builder` prototype as a reusable Hermes user skill in the default profile.

## Source

`/home/lixiang/workspace/ultimate-pptx-builder`

## Destination

`/home/lixiang/.hermes/skills/productivity/ultimate-pptx-builder`

## Sync Command

```bash
rsync -a --delete /home/lixiang/workspace/ultimate-pptx-builder/ \
  /home/lixiang/.hermes/skills/productivity/ultimate-pptx-builder/
```

## Installed Validation Command

```bash
cd /home/lixiang/.hermes/skills/productivity/ultimate-pptx-builder
python3 scripts/validate_skill.py
```

## Current Installed Result

```text
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

## Key Installed Capabilities

- IR-first PPTX generation pipeline
- HTML preview traceability
- editable PPTX export audit
- LibreOffice-rendered PPTX visual-fidelity loop
- `glass-fintech-pptx` 3-slide showcase
- 15-slide finance benchmark
- editable vector chart groups
- editable vector table groups
- layout/text safety gate

## Layout/Text Safety Gate

Installed skill now includes and validates:

```bash
python3 scripts/check_layout_safety.py <deck.ir.json> --report <layout-safety-report.json>
```

Current enforced rules include:

- 64px bottom safe zone
- 16px footer separation band
- CJK-aware priority text capacity
- max 5 core table columns for finance PPT pages
- compliance/suitability density cap
- table row/cell readability
- title/page-number collision
- oversized/repeated page-number motif detection

## Benchmark Metrics at Sync Time

```text
benchmark_visual_score=95.46
benchmark_editability=100.00
benchmark_practicality=100.00
benchmark_layout=pass
benchmark_layout_blocking=0
editable_vector_charts=4
editable_vector_tables=2
```

## Notes

This record confirms that the reusable installed skill, not only the workspace prototype, contains the updated acceptance standards and executable layout/text safety mechanism.
