# Visual DNA Model

## Purpose

A visual anchor is not validated by first-glance difference alone. A deck can look different at thumbnail level while sharing the same chart colors, fonts, cards, spacing, and component grammar. That is a shallow skin, not a visual system.

This model defines the minimum DNA layers required for a programmable PPTX visual anchor.

```text
Visual Anchor = Palette Logic + Typography System + Surface/Texture + Light Physics
              + Layout Archetypes + Container Grammar + Component Grammar
              + Data-Viz Grammar + Ornament/Motif System + Motion/Flow Metaphor
              + Density Rhythm + Office/PPTX Material Translation
```

## Core DNA Layers

| Layer | What It Controls | Shallow Failure |
|---|---|---|
| Palette logic | hue families, semantic colors, neutral scale, contrast policy, chart series mapping | same chart colors with different background |
| Typography system | font pairing, title/body/numeral treatment, weight rhythm, tabular numerals, CJK fallback | every system uses the same sans stack and sizes |
| Surface / texture | paper, glass, map canvas, metal, ink, gradient, image-generated background policy | flat recolor or decorative rectangle |
| Light physics | glow direction, shadow softness, highlight placement, vignette, spotlight, print-flat lighting | arbitrary glow or no coherent lighting model |
| Layout archetypes | cover/data/table/process/closing page spatial templates and asymmetry rules | same title-left/cards-right skeleton everywhere |
| Container grammar | card shape, radius, stroke, inset, cut corners, tabs, ledgers, capsules, map tiles | same rounded cards with different fill |
| Component grammar | KPI, quote, callout, table, process step, source rail, footer, page number treatment | components are mechanically reused across systems |
| Data-viz grammar | chart palette, axis treatment, grid style, labels, legends, annotation style, series geometry | chart colors and axes remain identical |
| Ornament / motif | rules, nodes, coordinates, marginalia, HUD marks, seals, glyphs, page numerals | superficial background decorations only |
| Flow metaphor | dashboard monitoring, editorial reading, map navigation, storyboard sequence, cockpit control | no system-specific reading path |
| Density rhythm | how low/medium/high density pages compress without losing identity | same spacing and card counts in every system |
| PPTX material translation | native/vector/raster policy, editable degradation, theme mapping | beautiful preview cannot become editable PPTX |

## Effective Anchor Test

Remove any one layer below. If the style still looks essentially the same, that layer is not carrying real DNA:

1. Palette and semantic chart mapping.
2. Typography and numeral voice.
3. Main container family.
4. Data visualization treatment.
5. Page-role layout archetypes.
6. Motif / ornament system.
7. Surface and light model.
8. Footer / source / pagination system.

An effective anchor should survive content changes but not survive DNA removal. In other words:

```text
same content + different DNA => visibly different system
same DNA + different content => recognizably same system
```

## Minimum Acceptance Criteria

A visual anchor is accepted only when:

- It declares all twelve DNA layers above, not only palette/background/container.
- At least six layers are materialized into actual PPTX objects or theme tokens.
- `data_viz_grammar`, `typography_system`, `container_grammar`, and `layout_archetypes` are mandatory; missing any of these is blocking.
- Chart series colors, axis/grid styling, label treatment, and annotation style differ across full visual systems unless the same corporate chart standard is explicitly required.
- Font families may share Office-safe fallbacks, but font pairing, scale, weight rhythm, and numeral treatment must differ by system.
- Metric/card/process/table components must not reuse the same geometry, radius, stroke, padding, and hierarchy across systems.
- Layout difference must alter page-role composition, not just object coordinates inside the same skeleton.
- Rendered contact sheets and full-size pages must be reviewed for component-level sameness, not only first-glance difference.

## Release Criteria

Release is blocked if a new visual system differs mainly by:

- background color or texture;
- accent palette while charts and components remain the same;
- decorative motifs that do not change information-bearing components;
- unchanged font scale/weight/numeral voice;
- unchanged card/component geometry;
- unchanged chart grammar;
- unchanged title/body/cards/footer composition skeleton.

## Practical PPTX Translation

Not every DNA layer must be fully native. Acceptable translations:

- Palette, typography, containers, charts, tables, cards, page numbers, footers: native/editable.
- Complex surface texture or AI-generated background: raster background is allowed only when it carries no critical text and has a native fallback.
- Motifs and route lines: native shapes or vector islands.
- Lighting: native gradients/shadows where possible; raster only for non-critical atmosphere.

## Reviewer Checklist

Ask these questions before accepting a visual anchor:

1. Do charts look designed for this system, or copied from another system?
2. Would the deck still feel like this system if the background was removed?
3. Are typography, numerals, and information hierarchy system-specific?
4. Are cards/containers structurally different, or just differently colored?
5. Does each page role use a different composition grammar appropriate to the system?
6. Do footer, source, and page-number systems reinforce the visual identity?
7. Are motifs connected to reading flow, not just decoration?
8. Can the system scale to dense finance slides without losing its identity?
