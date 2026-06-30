# QA Loop

## Four Gates

### Gate 1 — Fidelity

Compare HTML preview render with PPTX render.

Checks:

- object missing
- object shifted
- text wraps differently
- overflow/cropping
- font/color/weight drift
- z-order drift

Release threshold: score ≥90 or documented accepted exceptions.

### Gate 2 — Editability

Inspect PPTX object model or export report.

Checks:

- priority ≥4 text is native text
- finance chart/table is editable
- risk/source is editable and readable
- raster islands have source metadata

Release threshold: no critical editability failure.

### Gate 3 — Layout and Text Safety

Run `scripts/check_layout_safety.py` against the Slide IR before export acceptance.

Checks:

- priority>=4 objects inside safe zones
- bottom cards/footnotes/metrics outside the unsafe projection/export area
- CJK-aware text-box capacity for title/body/metric/risk/table text
- title/page-number decorative collisions
- dense finance-table row/cell readability
- oversized repeated page-number motifs that create AI-template smell

Release threshold: zero blocking layout/text issues, or explicit user-accepted exceptions in the validation record.

### Gate 4 — Design Quality

Critique using a design rubric:

- narrative clarity
- first/second/third read hierarchy
- spacing and alignment
- motif consistency
- deck rhythm
- density control
- professional finance tone

Release threshold: no blocking visual hierarchy or readability issue.

### Gate 5 — Practicality

Checks:

- 16:9 slide size
- Office-safe fonts or bundled fallback
- min font size policy
- file size / object count
- source/risk text present
- PDF export sanity

Release threshold: no finance practicality blocker.

## Required Fix-and-Reverify Loop

For real deck output, one pass is not enough:

1. Generate PPTX.
2. Render and audit.
3. Run layout/text safety.
4. List issues.
5. Fix at least one issue or explicitly document why no issue exists.
6. Re-render affected slides.
7. Accept only after no new blocking issues appear.

## Acceptance Mechanism

Every run should write `qa-report.json` matching `schemas/qa-report.schema.json` and, for long-form decks, a layout safety report from `scripts/check_layout_safety.py`.
