# Style Program

## Purpose

A style is not a template name. A style is a programmable visual system that can generate many slides without becoming repetitive.

## Required Fields

```yaml
style_program:
  id: swiss-grid-pptx
  tension:
    order_emergence: order
    surface_structure: structure
    authority_access: authority
  grammar:
    line: mechanical
    color_application: flat
    space: grid
    information_encoding: typography_chart
    depth: flat_layered
  tokens:
    palette: institutional-cool
    typography: office-cn-sans
  base_dna:
    - strict grid alignment
  sota_dna:
    - giant thin numeral as structure
    - controlled grid break
  pptx_material_strategy:
    native: [text, shape, chart, table]
    vector: [icon, simple diagram]
    raster: [texture, complex background]
  degradation_rules:
    - never rasterize priority >=4 text
    - replace complex texture with flat fill in editable mode
```

## SOTA Gate

Every style must pass:

- Base DNA ≥ 1.
- SOTA DNA ≥ 2.
- Each SOTA DNA answers: “Would a generic model reliably do this without the skill?” If yes, it is not SOTA enough.
- Every SOTA DNA has PPTX translation or degradation instructions.

## PPTX-Specific Dimensions

| Dimension | Why It Matters |
|---|---|
| Deck rhythm role | cover/body/data/appendix have different visual needs |
| Density support | finance decks often need medium/high density |
| Office font support | corporate decks must open predictably |
| Theme mapping | colors should map to PowerPoint theme slots |
| Compliance visibility | risk/source text must remain readable |

## Acceptance Mechanism

A style cannot be used unless:

- it declares `pptx_material_strategy`,
- it defines at least two SOTA moves,
- it lists forbidden degradations,
- it declares supported density modes,
- it maps tokens to Office-safe outputs.
