# Finance Benchmark Decks for Ultimate PPTX Builder

Use this reference when testing whether a PPTX-building workflow works as a real finance-deck system rather than a pretty slide generator.

## Why this exists

A short showcase can pass visual/editability checks while still failing from a user perspective. Longer finance decks expose problems that pixel fidelity does not catch:

- summary cards that disagree with table rows
- matrix counts that do not support the stated conclusion
- process titles that promise three stages while the slide shows four steps
- risk notes that use internal/test wording instead of formal finance-material language
- subtitles, footers, source notes, and metric cards colliding under dense layouts
- bottom cards or notes overflowing or nearly overflowing the slide safe area
- giant repeated page-number motifs that create obvious AI-generated template smell
- dense tables/matrices whose text technically exists but cannot be read comfortably

## Benchmark pattern

For a production-grade style anchor, create a realistic long-form benchmark before expanding into more style presets.

Minimum recommended benchmark:

1. 12-15 slides from a simulated or real user input contract.
2. Explicit audience, scenario, data assumptions, and business goal.
3. One `narrative_job` per slide.
4. Finance source/risk rail on every slide that needs it.
5. At least these content modes:
   - cover / hero thesis
   - executive summary
   - dashboard metrics
   - editable vector chart page
   - editable vector table page
   - matrix / heatmap-like grid
   - scenario stress cards
   - process / execution path
   - timeline / observation calendar
   - quote / decision principle
   - compliance / suitability page
   - action plan
6. At least one fix-and-reverify pass using visual/narrative QA, not only automated JSON scores.
7. A passing layout/text safety report from `scripts/check_layout_safety.py`.

## Acceptance gates

A benchmark deck should fail if any of these are true:

- less than the target slide count
- missing narrative jobs
- missing risk/source rail where finance content requires it
- chart or table falls back to raster when priority >= 4
- visual fidelity below the configured threshold
- QA editability below the configured threshold
- export audit contains unsupported critical objects
- layout/text safety gate fails
- user-facing financial wording reads like internal test scaffolding
- slide summaries contradict table/chart data
- bottom cards, risk notes, metrics, or tables violate the slide safe zone
- decorative page-number or repeated glass-card motif dominates content-heavy pages
- title/page-number or title/content collision risk remains
- priority>=4 text likely overflows its box by CJK-aware capacity estimate

## Editable vector chart/table MVP

Until full Office chart XML and native table XML are implemented, editable vector groups are an acceptable MVP path if the audit is explicit:

- chart objects: `actual=editable-vector-chart`
- table objects: `actual=editable-vector-table`
- components must be native text/shapes, not flattened screenshots
- the contract/IR should retain the semantic data so future exporters can upgrade to Office-native structures

## Narrative + Layout QA checklist

Run this on dense pages after automated validation:

- Does the page answer one clear business question?
- Do summary cards match the underlying table/chart values?
- Are labels, units, source, and risk text visible without zooming?
- Does the slide title match the number of steps/stages/cards shown?
- Would the wording be acceptable in an investment-committee or institutional-client deck?
- Are all business-critical numbers editable in PowerPoint?
- Are all priority>=4 objects inside the safe zone?
- Does each text box have enough capacity for its actual copy?
- Does the page rhythm vary across the deck, or is it just the same AI-looking glass template repeated?

## Proven glass-fintech benchmark

The `glass-fintech-pptx` benchmark pattern used this 15-slide structure:

1. cover / thesis
2. executive summary
3. macro dashboard with risk-budget chart
4. asset allocation chart focus
5. allocation recommendation table
6. style exposure matrix
7. sector exposure chart
8. scenario stress cards
9. execution path process
10. risk-control table
11. observation calendar timeline
12. performance attribution chart
13. decision principle quote
14. compliance / suitability
15. action plan

The key lesson: a benchmark that passes `fidelity=94+` and `editability=100` can still fail user review. Treat automated scores as necessary but insufficient; user-perspective narrative QA and executable layout/text safety are part of the skill, not polish.
