# Layout Root-Cause and Exhaustive QA Lessons

Use this reference when building or reviewing long-form editable PPTX decks, especially finance decks with repeated components such as metric cards, tables, process bands, timeline rows, compliance text, and footers.

## Session Signal

A generated 15-slide finance benchmark passed visual fidelity and editability gates, but manual review found obvious layout defects: metric-card text overlap, title/metric-band crowding, container/text collisions, and compliance wording that still felt like a generation/test artifact.

The user correction was explicit: do not wait for the user to enumerate every visible defect. The workflow must proactively locate layout classes of failure and make them impossible or blocking.

## Root Cause Pattern

High visual-fidelity scores can mask bad layouts when both renderers consume the same flawed IR:

```text
Bad IR -> Pillow reference PNG
Bad IR -> PPTX -> LibreOffice PNG
```

The similarity score answers whether PPTX preserved the IR, not whether the IR is sane.

Similarly, editability audit answers whether content is native/editable, not whether those native text boxes collide.

## Concrete Failure Class

The defective deck used fixed y-offsets inside a shared `add_metric()` helper:

```text
metric label
metric value
metric delta
```

A typical bad IR shape looked like:

```text
value: y=178 h=38 -> 178..216
delta: y=192 h=24 -> 192..216
```

The objects were native and editable, and reference/PPTX rendering matched, but the slide was still visibly wrong.

## Required Prevention

Treat layout as a compiler safety problem, not post-hoc polish.

Long-form PPTX generation needs four independent gates:

1. **IR structural gate** — ids, roles, z-order, render policy, editability budgets.
2. **Layout/text safety gate** — text capacity, pairwise collisions, intrinsic component stacking, table density, footer separation.
3. **Renderer fidelity gate** — preview/reference versus exported PPTX render similarity.
4. **Semantic/visual review gate** — narrative coherence, finance professionalism, compliance wording, visual hierarchy.

Do not substitute any one gate for the others.

## Layout Safety Checks to Include

At minimum, block on:

- pairwise estimated text-box collisions;
- metric-card label/value/delta stack gap;
- child text padding inside card containers;
- title band versus metric/content band collisions;
- bottom safe-zone and footer-separation violations;
- table row height, visible cell count, and long-cell overflow risk;
- compliance/body density and test/generation-chain wording;
- oversized repeated page-number motifs on long decks.

## Preferred Fix Strategy

Avoid per-slide coordinate patching. Fix the shared grammar or component:

- replace fixed offsets with intrinsic layout functions;
- allocate vertical slots by component type and density mode;
- increase container height before shrinking text below readable thresholds;
- split or reduce dense tables instead of forcing all rows into one page;
- make content-heavy topology titles smaller or reserve a shorter title band;
- rerun full-deck gates and spot-check representative rendered slides.

## Acceptance Language

A deck is not accepted because it is visually similar to its reference. It is accepted only when:

```text
layout=pass
visual fidelity >= threshold
editability >= threshold
semantic/visual review has no blockers
```

If a user points out visible defects after a pass, treat that as a validation-system bug first, not merely a slide-design bug.


## Additional Failure Class: Text Leading and Container Stacking

A later review found two more classes that object-overlap checks alone did not catch:

- wrapped native text can look nearly overlapped when PPTX export relies on renderer-default Chinese line spacing;
- visual containers can overlap or double-frame each other even when text boxes do not collide, e.g. a self-paneled table inside an outer glass panel or metric cards pressing into another panel.

Prevention additions:

- the exporter should write explicit paragraph line spacing (`a:lnSpc`) for native text, with looser leading for small wrapped labels;
- the layout gate should block non-decorative container overlap and unapproved nested double panels;
- title-to-first-content spacing should be a blocking rule, not a subjective visual note;
- table/chart objects that already render an editable vector panel should not be wrapped in a second glass panel unless the nesting is explicitly allowed.
