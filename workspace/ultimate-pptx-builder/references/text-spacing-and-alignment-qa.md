# Text Spacing and Alignment Graph QA

## Purpose

PPTX release QA must not stop at “no obvious overlap.” A deck can have no collisions and still look unprofessional if text blocks are too close, columns are near-aligned rather than aligned, card gutters drift, or children violate container padding.

This reference defines two deterministic geometry gates:

1. `check_text_spacing.py` — role-aware text distance field.
2. `check_alignment_graph.py` — declared alignment relations plus inferred near-miss warnings.

## Text Distance Field

`check_text_spacing.py` traverses priority native text objects pairwise after estimating rendered ink extents. It classifies each pair before applying thresholds.

### Relation classes

- `metric-stack`: label/value/delta inside the same metric or signal component.
- `component-row`: text inside the same component that sits side-by-side.
- `component-stack`: text inside the same component that stacks vertically.
- `paragraph-stack`: narrative body paragraphs in the same column.
- `vertical-stack`: non-body stacked text.
- `footer`: risk/source/footnote separation.
- `unrelated`: projected side-by-side text that should have clear breathing room.

### Blocking codes

- `TEXT_COLLISION`
- `METRIC_STACK_GAP_TOO_SMALL`
- `COMPONENT_ROW_GAP_TOO_SMALL`
- `COMPONENT_STACK_GAP_TOO_SMALL`
- `PARAGRAPH_RHYTHM_TOO_TIGHT`
- `TEXT_STACK_GAP_TOO_SMALL`
- `FOOTER_TEXT_SEPARATION_TOO_SMALL`
- `UNRELATED_TEXT_GAP_TOO_SMALL`

## Alignment Graph

`check_alignment_graph.py` validates explicit `layout_relations` in each slide IR. A slide with no relations fails with `LAYOUT_RELATIONS_MISSING`.

### Supported relation types

- `align-left`, `align-right`, `align-top`, `align-bottom`, `align-center-x`, `align-center-y`
- `row` with optional `align`, `equal`, and `gutter`
- `parent-padding`
- `vertical-stack` as an accepted declaration; rhythm is enforced by text spacing

### Blocking codes

- `LAYOUT_RELATIONS_MISSING`
- `RELATION_OBJECT_MISSING`
- `DECLARED_ALIGN_*_BROKEN`
- `EQUAL_WIDTH_BROKEN`
- `EQUAL_HEIGHT_BROKEN`
- `EQUAL_GUTTER_BROKEN`
- `PARENT_PADDING_BROKEN`
- `UNKNOWN_LAYOUT_RELATION`

### Warning codes

- `INFERRED_ALIGNMENT_NEAR_MISS`

Warnings do not block release yet, but they are important review signals. Near-miss warnings mean objects are 8–16px away from a strong left anchor: often a sign of accidental visual drift.

## IR contract

Compiler outputs should include `layout_relations` on every generated slide. The current compiler uses conservative relation inference for:

- body text columns;
- metric/signal/scenario/process component rows;
- table-like scenario/process columns;
- component parent-padding for cards/chips/zones.

Future style-specific compilers may replace inference with authored semantic relations, but they must not remove the relation layer.

## Acceptance

Release validators must run both scripts after layout safety and before visual-layout/aesthetic gates:

```bash
python3 scripts/check_layout_safety.py deck.ir.json --report layout.json
python3 scripts/check_text_spacing.py deck.ir.json --report text-spacing.json
python3 scripts/check_alignment_graph.py deck.ir.json --report alignment-graph.json
python3 scripts/check_visual_layout_architecture.py deck.ir.json --report visual-layout.json
```

A release passes only if both new reports have:

```json
{"release_decision": "pass", "blocking_count": 0}
```

## Design principle

Layout is not boxes. Layout is relationships between boxes.

The QA system must therefore check both:

- absolute geometry: capacity, overflow, collision;
- relational geometry: spacing, alignment, equal gutters, parent padding.
