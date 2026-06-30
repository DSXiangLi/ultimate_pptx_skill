# Authoring Contract

## Principle

Authors may use HTML-like layout freedom, but exportable meaning must be declared in IR. If HTML is used, every exportable DOM node must map to exactly one IR object via `data-ir-id`.

## Object Authoring Rules

| Rule | Reason | Acceptance |
|---|---|---|
| Critical text is IR `text` | preserves editability | priority ≥4 text cannot render as raster |
| Decoration may be DOM-only | visual freedom | decoration cannot contain words/numbers |
| Complex visual effects become `rasterIsland` | preserve fidelity | must include source metadata |
| Charts/tables declare data | finance editability | priority ≥4 chart/table cannot be image-only |
| IDs are stable | QA and patchability | duplicate IDs fail validation |

## HTML Preview Contract

If HTML is generated from IR:

```html
<div class="slide" data-slide-id="s1">
  <h1 data-ir-id="title">...</h1>
  <div data-ir-id="chart_1"></div>
</div>
```

- `data-ir-id` must match an object ID in the IR.
- Pseudo-elements cannot contain meaningful text.
- Browser-computed layout may be stored as `computed_box` sidecar data.

## Acceptance Mechanism

Run `scripts/validate_skill.py`. For a real renderer, add a preview traceability test:

- Parse HTML.
- Extract every `[data-ir-id]`.
- Confirm it exists in IR.
- Confirm every exportable IR object has either a preview node or is explicitly hidden.
