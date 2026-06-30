# Layout and Text Safety Gate

This reference converts the PowerPoint overflow and text-typesetting lessons into an executable acceptance mechanism. It exists because pixel fidelity can faithfully reproduce a bad layout.

## Purpose

The gate validates the **layout IR itself** before export/rendering:

```text
Content Contract → Slide IR → layout/text safety gate → HTML/PPTX renderers
```

It catches design-system failures that normal fidelity/editability checks miss:

- critical objects too close to slide edges
- bottom cards or notes entering the unsafe slide edge area
- non-footer content entering the footer separation band
- finance tables with too many core columns for a readable PPT page
- compliance/suitability pages that become dense document pages
- title and decorative page-number collisions
- priority text that is likely to overflow its text box
- wrapped native text whose estimated line leading is unsafe
- dense finance tables with rows/cells too small to read
- non-decorative containers that overlap or create unapproved nested double panels
- title-to-first-content gaps that are too tight for finance PPT breathing room
- title orphan wraps and title-to-text gaps that visually crowd subtitles/body copy
- protected Chinese terms split across PowerPoint line breaks
- chart-focus/action-page/card-row alignment-grid defects
- repeated oversized page-number motifs that create obvious AI-template smell

## Executable Mechanism

Run:

```bash
python3 scripts/check_layout_safety.py build/glass-fintech-benchmark/glass-fintech-benchmark.ir.json \
  --report build/glass-fintech-benchmark/glass-fintech-benchmark-layout-safety-report.json
```

The script exits non-zero on blocking issues and writes a JSON report:

```json
{
  "issue_count": 0,
  "blocking_count": 0,
  "release_decision": "pass",
  "issues": []
}
```

## Default Blocking Rules

| Rule | Default | Blocks When |
|---|---:|---|
| side/top safe zone | 48 px | priority>=4 or critical object violates side/top margin |
| bottom safe zone | 64 px | critical text/chart/table/metric/card enters bottom unsafe area |
| footer separation | 16 px above footer rail | non-footer content enters the footer separation band |
| table columns | 5 core fields | finance table has too many core fields for a readable PPT page |
| compliance body paragraphs | 4 max | compliance/suitability page becomes a dense document page |
| title length | 34 chars | title is too long for a single finance-deck headline |
| text capacity | CJK-aware heuristic | priority>=4 text likely needs more height than its box |
| table row height | 38 px | finance table row is too short for readability |
| container gap | 14 px | visual containers are too close, warning |
| container overlap | 2% / 4 px | non-decorative containers overlap, blocking |
| title/content gap | 34 px | title band is too close to the first content container |
| title/text gap | 12 px | title estimated hitbox is too close to priority text |
| title orphan line | 4 weighted chars | final title line would contain too little content |
| alignment tolerance | 8 px | same-row/paired containers break the intended grid |
| protected-term wrap | term-specific | estimated break falls inside a protected Chinese term |
| page-number area | 1.2% of slide | decorative page number becomes a dominant motif |
| long-deck page-number repetition | 35% slides | oversized page-number motif repeats across too many slides |
| title/decor gap | 56 px | title expanded hitbox intersects page-number decoration |

## Critical Roles

The gate treats these roles as business-critical for layout safety:

```text
title, body, risk, source, footnote, metric, metric-note, table, chart
```

Decorative backgrounds and glow orbs may bleed by design, but decorative page numbers are checked because they can collide with titles and create template smell.

## Text Capacity Heuristic

PowerPoint, LibreOffice, and Windows/macOS font metrics differ, so the checker does not pretend to be exact. It uses a conservative CJK-aware estimate:

- CJK character width ≈ 1em before renderer scaling
- ASCII character width ≈ 0.55em before renderer scaling
- Office/LibreOffice CJK render scale ≈ 1.30x, used conservatively for line-capacity estimates
- available line width = 88% of text box width
- multi-line native text line height budget = 1.38x font size plus padding
- single-line text uses a lighter baseline check to avoid false positives on KPI values
- PPTX export writes explicit OOXML paragraph spacing so rendered native text does not depend on Office/LibreOffice defaults

This heuristic is intentionally stricter than pixel fidelity. If it fails, either shorten copy, reduce font size, enlarge the box, or redesign the slide.

## Acceptance Gate

A long-form benchmark deck is not accepted unless all are true:

- `scripts/check_layout_safety.py` exits 0.
- The layout safety report has `release_decision: pass`.
- No blocking `BOTTOM_SAFE_ZONE`, `FOOTER_SEPARATION`, `TEXT_OVERFLOW_RISK`, `PROTECTED_TERM_WRAP_RISK`, `TITLE_ORPHAN_WRAP`, `TITLE_TEXT_GAP_TOO_SMALL`, `CONTENT_ROW_TOP_MISALIGNMENT`, `CARD_ROW_EDGE_MISALIGNMENT`, `TITLE_DECOR_COLLISION`, `OVERSIZED_PAGE_NUMBER`, `TABLE_TOO_MANY_COLUMNS`, `COMPLIANCE_TEXT_DENSITY`, or `TABLE_CELL_OVERFLOW_RISK` remains.
- Any accepted exception is documented in the validation record with a user-facing reason.

## Why This Is a System Mechanism, Not a Knowledge Note

Knowledge notes tell the agent what to remember. This gate makes the pipeline fail before bad output is called complete. It moves layout discipline from “design advice” into a runnable contract that every future deck can enforce.
