# Market Atlas Visual Layering Learnings

## Context

`market-atlas-infographic` is meant to use map/grid/route motifs without letting those motifs compete with investment-committee content. The visual language only works when decorative atlas infrastructure stays behind content isolation masks, and business objects sit above both.

## Rule

Before changing Atlas grid, route, mask, footer, or Signal Field rendering, read this note and `docs/learning/glass-fintech-showcase.md`.

## Problem 1: Content masks below route/grid motifs only tint the page; they do not isolate content

### Symptom

A Market Atlas deck passed automated gates but looked visually chaotic in real PPTX screenshots:

- The whole page appeared as if background transparency had changed.
- Grid and route lines bled through left narrative, Signal Field, process area, and footer regions.
- Layout felt more crowded even where text boxes did not geometrically overlap.
- Slide 01 and slide 05 were especially affected.

### Root Cause

There were two interacting failures:

1. **Opacity regression:** a previous Atlas “de-noising” pass treated content-zone masks as decorative noise and lowered `zone_left` / `zone_bottom` opacity too far.
2. **Layering architecture regression:** the Atlas content masks were below decorative `atlas-gridline`, `route-line`, and `map-node` motifs in z-order. Even after increasing opacity, those masks could not actually block motif bleed-through because the motifs were painted above them.

The correct Atlas hierarchy is:

```text
atlas canvas
  < decorative grid / route / map-node motifs
  < content isolation masks: zone_left / zone_right / zone_bottom / footer-mask
  < business surfaces: cards / charts / Signal Field / process tiles
  < business text / metrics / risk note
```

### Why this was not an exporter bug

The IR already contained weak or incorrectly layered masks before PPTX export. The HTML/PNG reference and LibreOffice-rendered PPTX actual both showed the same visual hierarchy problem. That rules out PowerPoint/PPTX transparency conversion as the primary cause.

### Why the previous gate missed it

The previous visual-layout gate checked some local symptoms, such as overly prominent grid or route opacity. It did **not** require:

- content-zone masks to have minimum opacity;
- content masks to sit above decorative motifs;
- risk/footer text to have a strong footer mask;
- semantic separation between decorative background routes and content-bearing regions.

So a deck could pass while still feeling chaotic to a human reviewer.

### Fix

- Keep Atlas decorative grid/route opacities atmospheric.
- Raise `zone_left`, `zone_right`, and `zone_bottom` opacity so they become real content-isolation surfaces.
- Put content masks above decorative grid/route/map-node motifs but below business cards/text.
- Add a dedicated `footer-mask` behind risk notes.
- Add hard gates:
  - `ATLAS_CONTENT_ZONE_UNDERMASKED`
  - `ATLAS_CONTENT_MASK_BELOW_MOTIF`
  - `ATLAS_FOOTER_UNMASKED`
  - existing grid/route prominence checks remain active.

### Verification Commands

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/check_visual_layout_architecture.py scripts/validate_visual_systems.py scripts/validate_skill.py
python3 scripts/validate_visual_systems.py
python3 scripts/check_visual_layout_architecture.py build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json --report build/visual-system-market-atlas-infographic/market-atlas-infographic-visual-layout-architecture-report.json
python3 scripts/check_layout_safety.py build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json --report build/visual-system-market-atlas-infographic/market-atlas-infographic-layout-safety-report.json
python3 scripts/check_pptx_package.py build/visual-system-market-atlas-infographic/market-atlas-infographic.pptx
python3 scripts/validate_skill.py
```

Then manually inspect:

- `build/visual-system-market-atlas-infographic/visual-fidelity/actual/slide-01.png`
- `build/visual-system-market-atlas-infographic/visual-fidelity/actual/slide-05.png`

### Files Affected

- `scripts/compile_spec_to_ir.py`
- `scripts/check_visual_layout_architecture.py`
- `docs/learning/market-atlas-visual-layering.md`

### Future Prevention Rule

Do not solve Atlas visual noise by fading content masks. Fade or clip decorative motifs instead. Content masks are semantic isolation surfaces, not ornament.

A visual gate is incomplete if it checks only object opacity and not the z-order relationship between decorative motifs, isolation masks, and business content.
