# PPTX QA Gap Analysis: Text Spacing and Alignment Mechanisms

## Context

A reviewer pointed out that the current QA language is too coarse. Saying “no obvious overlap” is not a mechanism. A finance-grade PPTX skill must traverse every text block, measure spacing relationships, and verify intended alignment relationships between containers, text, charts, tables, and repeated components.

This analysis inspects the current `ultimate-pptx-builder` skill after the Market Atlas layout-grammar pass.

## Summary Judgment

The current skill has improved from pure visual scoring to structural gates, but it is still not rigorous enough for institutional PPT quality. Its biggest weakness is that it checks many defects as **local named patterns**, not as a general **layout relation system**.

Current strengths:

- CJK-aware text capacity estimation exists.
- Pairwise text collision exists.
- Metric-card label/value/delta stacking exists.
- Some title/content gaps exist.
- Some container overlap/gap checks exist.
- Some hard-coded alignment checks exist for chart-focus and metric-card rows.
- Atlas has coarse grammar gates for title band, footer, right rail, and microtext.

Current gaps:

1. It does not measure minimum spacing between every relevant text block pair.
2. It treats overlap as the main text-pair failure and misses near-crowding.
3. It does not classify spacing by semantic relationship: same paragraph stack, card internal stack, unrelated neighboring modules, footer, title/subtitle, chart label, etc.
4. It does not infer or require alignment groups across arbitrary objects.
5. It does not verify equal gutters, equal column widths, equal row heights, baseline alignment, optical alignment, or container-to-child padding as general rules.
6. It does not build a page-level layout graph from IR objects.
7. It does not cross-check IR-estimated text boxes against actual rendered text extents from PPTX screenshots/OCR.
8. `SKILL.md` references `references/atlas-layout-grammar-gates.md`, but that file is missing in the workspace, so Atlas grammar is not fully documented as a reusable rule source.

## Evidence from Current IR Diagnostics

A quick diagnostic scanned the current visual-system IR outputs that already pass the official validators.

IRs inspected:

- `build/visual-system-glass-fintech-pptx/glass-fintech-pptx.ir.json`
- `build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json`
- `build/visual-system-paper-analyst-report/paper-analyst-report.ir.json`

### Text proximity findings

Even after official PASS, the diagnostic found many priority text pairs with less than 10px separation:

| Visual system | Close text pairs `<10px` | Example |
|---|---:|---|
| glass-fintech-pptx | 36 | metric label/value/delta stacks at 5px gaps |
| market-atlas-infographic | 50 | metric value/delta at 2px; body paragraph stacks at 8px; decision rule rows at 6px |
| paper-analyst-report | 38 | metric value/delta at 1px; body paragraph stacks at 6px |

Not every close pair is automatically wrong. Some metric stacks intentionally have tighter rhythm. But the current gate does not distinguish intentional compact stacks from accidental near-collisions. That is the real weakness.

### Alignment near-miss findings

The same diagnostic found many objects sitting 8–24px away from strong repeated anchors. The raw count includes false positives because it has no semantic grouping yet, but that is exactly the point: the current skill has no general alignment graph to decide which near-misses are acceptable and which are professional layout defects.

Examples:

- Paper pages repeatedly show text/content left edges at 96/98/104 around stronger anchors near 82.
- Atlas pages show right-column objects and labels near, but not always on, repeated right/left anchors.
- Glass pages show title/subtitle/risk objects near decorative/page anchors without an explicit alignment contract.

### Container row raggedness findings

The diagnostic found multiple rows where shapes start on a similar y-band but have inconsistent tops, bottoms, or heights. Some are legitimate because left/right zones intentionally differ; others require explicit relation metadata to decide.

This exposes a missing concept: **the IR lacks alignment intent**. Without intent, a checker must guess from geometry and IDs.

## Root Cause

The skill currently validates objects mostly as isolated boxes or named component patterns:

```text
object fits safe zone
text fits box
two text hitboxes do not overlap
metric-card known stack has enough gap
some known rows align
Atlas right panel x is within a range
```

That is not enough. Professional PPT layout is relational:

```text
this title aligns to this content column
these cards share a row baseline
these containers share equal gutters
these paragraphs are a vertical stack with rhythm N
this chart and note panel share top/bottom alignment
this right rail is optically aligned to, but not identical with, its parent panel padding
this footer is separated from all non-footer content by N
```

The current IR does not encode those relationships, and the validators do not infer them robustly.

## Missing Mechanism 1: Text Distance Field

### What is missing

The current `check_pairwise_text_collisions()` only blocks overlap-like collisions. It should instead build a complete text distance field:

```text
for every priority text block A/B:
  compute estimated rendered hitboxes
  compute horizontal gap, vertical gap, diagonal gap
  compute overlap on perpendicular axis
  classify relationship
  compare against role-aware minimum gap
```

### Required relationship classes

| Relationship | Example | Minimum mechanism |
|---|---|---|
| title → subtitle | headline above supporting copy | gap based on title font and slide density |
| title → first content | title above card/chart/body | larger breathing room, e.g. 24–40px |
| paragraph stack | body_1 → body_2 | vertical rhythm, e.g. 8–14px depending font |
| metric internal stack | label → value → delta | compact but explicit, e.g. 3–6px, never accidental |
| neighboring text modules | left body vs right labels | horizontal gutter threshold with projection overlap |
| text → footer | body/chart text above risk/source | footer separation threshold |
| chart label/legend text | labels around chart | chart-specific min gap and non-overlap |
| decorative folio text | small labels/page tags | may be exempt or warning only |

### Why this matters

A layout can have no overlap but still look broken if text blocks have 1–3px gaps, inconsistent paragraph rhythm, or accidental crowding between unrelated modules.

### Current deficiency in code

`check_layout_safety.py` has:

- `check_pairwise_text_collisions()` — collision only, not spacing.
- `metric_group_issues()` — only regex-based metric groups.
- `check_title_text_gap_and_wrap()` — only title versus body/quote near title area.

It does not have a general `check_pairwise_text_spacing()`.

## Missing Mechanism 2: Alignment Graph

### What is missing

The checker needs to build an alignment graph from objects, not rely on a few hard-coded patterns.

A proper alignment graph should identify:

- left-edge groups
- right-edge groups
- top-edge rows
- bottom-edge rows
- centerline groups
- baseline groups for text stacks
- equal-width groups
- equal-height groups
- equal-gutter sequences
- parent-child padding relationships

Then it should compare actual geometry against declared or inferred layout intent.

### Alignment types that should be explicit

| Alignment type | Examples |
|---|---|
| left edge | title, subtitle, body column, chart caption |
| right edge | right rail cards, footer, source note |
| top edge | same-row cards, chart + note panel |
| bottom edge | KPI card row, footer-aligned modules |
| centerline | process nodes, scenario branches |
| baseline | metric values in same row |
| equal width | cards in a metric row |
| equal height | peer cards or row modules |
| equal gutter | repeated columns/cards |
| optical alignment | small labels aligned inside padded containers, not same absolute x |
| parent padding | child text inside card/container follows declared inset |

### Current deficiency in code

`check_alignment_grid()` currently checks only a few cases:

- note panel top versus chart top
- metric card row span versus body panel span
- same-row metric cards share tops/bottoms

This is useful but not general. It misses arbitrary visual systems and non-metric components.

## Missing Mechanism 3: Declarative Layout Intent in IR

The IR needs explicit relation metadata. Geometry alone cannot tell whether two boxes should align or merely sit near each other.

Recommended IR extension:

```json
{
  "layout_relations": [
    {
      "id": "title-column-left",
      "type": "align-left",
      "objects": ["s01_title", "s01_subtitle", "s01_body_1"],
      "tolerance": 4
    },
    {
      "id": "metric-row-1",
      "type": "row",
      "objects": ["s01_metric_1_card", "s01_metric_2_card", "s01_metric_3_card"],
      "align": ["top", "bottom"],
      "equal": ["height"],
      "gutter": {"mode": "equal", "tolerance": 3}
    },
    {
      "id": "card-padding",
      "type": "parent-padding",
      "parent": "s01_metric_1_card",
      "children": ["s01_metric_1_label", "s01_metric_1_value", "s01_metric_1_delta"],
      "padding": {"x": 12, "y": 8}
    },
    {
      "id": "body-stack",
      "type": "vertical-stack",
      "objects": ["s01_body_1", "s01_body_2", "s01_body_3"],
      "min_gap": 8,
      "max_gap": 18
    }
  ]
}
```

This would convert visual intent from “implicit coordinates” into a testable contract.

## Missing Mechanism 4: Rendered Text Geometry Verification

IR estimates are necessary but not sufficient. Native PPT text metrics can differ after LibreOffice/PowerPoint rendering.

The robust path is two-stage:

1. **IR geometry gate**: fast deterministic estimate from boxes, roles, fonts, and layout relations.
2. **Rendered geometry gate**: detect text block extents from actual PPTX-rendered PNG and compare them to IR expectations.

Possible implementation options:

- Use OCR/text detection boxes for rendered PNGs, then map approximate boxes back to IR IDs using text strings and positions.
- Use LibreOffice/PPTX XML text boxes plus conservative metrics for deterministic gate, then sample rendered OCR only for suspicious pages.
- Use image segmentation to detect visual card/container edges and verify alignment independent of text recognition.

This is especially important for Chinese text because rendered line breaks and actual ink extents differ from IR estimates.

## Missing Mechanism 5: Component Grammar Contracts

Each reusable component should declare its internal layout contract:

```text
MetricCard:
  children: label, value, delta
  padding: 12/8
  label→value gap: 3–8
  value→delta gap: 3–8
  value baseline aligns across row
  cards in same row: equal height, equal width, equal gutter

DecisionRuleList:
  rows: key/value pairs
  key column fixed width
  values share x-left
  row gap 8–12
  no value text below 8px

AtlasRightRail:
  parent x anchor: 724/748 family
  child cards share left/right inset
  signal bars share width
  footer excluded from rail
```

Current validators encode some of this in ad hoc regexes. The skill needs reusable component schemas.

## Missing Mechanism 6: Better Severity Model

Not all close spacing is equal. The checker needs severity based on role and intent:

| Case | Severity |
|---|---|
| unrelated priority text gap < 6px | blocking |
| paragraph stack gap < 6px | blocking/warning depending density |
| metric internal value/delta gap < 2px | blocking |
| metric internal 3–5px | allowed if declared compact |
| decorative folio close to background labels | ignore/warning |
| near-miss from inferred anchor but no declared relation | warning requiring relation metadata |
| declared relation violated | blocking |

## Missing Mechanism 7: QA Report Integration

`run_qa.py` currently gives a shallow design score based on role presence:

```python
if "title" in roles: score += 10
if "body" in roles: score += 10
```

This does not reflect real design quality. The QA report should ingest:

- layout safety report
- visual layout architecture report
- text spacing report
- alignment graph report
- rendered geometry/OCR report
- visual aesthetic report

Release should fail if any of these has blocking issues.

## Concrete Proposed New Scripts

### 1. `scripts/check_text_spacing.py`

Purpose: traverse all text blocks and validate role-aware spacing.

Outputs:

- `TEXT_GAP_TOO_SMALL`
- `PARAGRAPH_RHYTHM_TOO_TIGHT`
- `UNRELATED_TEXT_NEAR_COLLISION`
- `FOOTER_TEXT_SEPARATION_TOO_SMALL`
- `METRIC_STACK_GAP_TOO_SMALL`
- `CHART_LABEL_GAP_TOO_SMALL`

### 2. `scripts/check_alignment_graph.py`

Purpose: validate declared and inferred alignment groups.

Outputs:

- `DECLARED_ALIGN_LEFT_BROKEN`
- `DECLARED_ROW_TOP_BROKEN`
- `EQUAL_GUTTER_BROKEN`
- `EQUAL_WIDTH_BROKEN`
- `PARENT_PADDING_BROKEN`
- `INFERRED_ALIGNMENT_NEAR_MISS`
- `UNDECLARED_STRONG_ALIGNMENT_CLUSTER`

### 3. `scripts/check_component_grammar.py`

Purpose: validate component-level contracts for metric cards, right rails, tables, process nodes, scenario maps, footer rails.

Outputs:

- `METRIC_CARD_CONTRACT_BROKEN`
- `RIGHT_RAIL_CHILD_ALIGNMENT_BROKEN`
- `DECISION_LIST_COLUMN_ALIGNMENT_BROKEN`
- `PROCESS_NODE_BASELINE_BROKEN`
- `SCENARIO_BRANCH_ALIGNMENT_BROKEN`

### 4. `scripts/check_rendered_geometry.py`

Purpose: compare actual rendered PNG text/container geometry against IR estimates and layout relations.

Outputs:

- `RENDERED_TEXT_EXTENT_EXCEEDS_IR`
- `RENDERED_TEXT_NEAR_COLLISION`
- `RENDERED_CONTAINER_EDGE_MISALIGNMENT`
- `RENDERED_GRID_DRIFT`

## Recommended Next Implementation Order

1. Add IR-level `check_text_spacing.py` first. It is deterministic and directly addresses the reviewer’s first criticism.
2. Add `layout_relations` to generated IR for at least `glass-fintech-pptx` and `market-atlas-infographic`.
3. Add `check_alignment_graph.py` that validates declared relations and emits warnings for inferred near-misses.
4. Refactor existing ad hoc alignment checks from `check_layout_safety.py` into the new graph checker.
5. Add component grammar contracts for MetricCard, AtlasRightRail, PaperAnalystSidebar, GlassChartPanel.
6. Integrate all new reports into `validate_visual_systems.py`, `validate_glass_showcase.py`, `validate_glass_benchmark.py`, and `run_qa.py`.
7. Only after IR gates stabilize, add rendered OCR/geometry verification.

## Acceptance Criteria for the New Mechanism

A deck should not be accepted unless:

- Every priority text block pair is classified as overlap, stack, neighbor, unrelated, footer, decorative, or exempt.
- No unclassified priority text pair is closer than the global minimum threshold.
- Every repeated component row declares and passes alignment/gutter rules.
- Every visual system has declared layout anchors, not just hard-coded coordinates.
- Strong inferred alignment clusters either become declared relations or are explicitly ignored.
- Rendered contact-sheet review confirms the reports did not miss obvious spacing/alignment defects.

## Bottom Line

The current skill is moving in the right direction, but it still behaves like a rule collection rather than a layout engine. The next architectural upgrade should be:

```text
Box checks → Text distance field + Alignment graph + Component grammar contracts + Rendered geometry verification
```

That is the mechanism needed to make PPTX QA specific enough for institutional finance decks.
