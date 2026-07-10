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

## Problem 2: Passing geometry while failing Atlas layout grammar

### Symptom

A Market Atlas deck could pass layout safety, visual fidelity, and editability gates while a reviewer still saw institution-level layout problems:

- Title/subtitle band felt too heavy and visually pushed the map grammar downward.
- Large content masks intruded into the title area, making the header read like a heavy container.
- Right signal/decision panels drifted between x positions and sometimes felt like floating cards.
- Footer rail was visually too dominant for a finance review page.
- Dense decision semantics were hidden as 6–7px microtext instead of being handled by layout grammar.
- Slide 05 process page had a low visual center of gravity.

### Root Cause

The existing gates checked local overlap, safe zones, object editability, and render fidelity. They did not encode the Atlas visual grammar itself:

```text
light header band ≤ y214
stable left analysis field starts around y222
right decision rail anchored around x724–748
weak compliance footer h≤44 and opacity≤0.90
business semantic text should not rely on <8px microtype
```

Without those rules, the compiler could generate a technically valid but visually unstable map deck.

### Fix

- Added executable Atlas layout grammar checks in `scripts/check_visual_layout_architecture.py`:
  - `ATLAS_TITLE_ZONE_OVERWEIGHT`
  - `ATLAS_TITLE_ZONE_MASK_INTRUSION`
  - `ATLAS_RIGHT_PANEL_FLOATING`
  - `ATLAS_FOOTER_DOMINANCE`
  - `ATLAS_DENSITY_PARITY_FAILURE`
- Reworked `market-atlas-infographic` compiler grammar in `scripts/compile_spec_to_ir.py`:
  - introduced a light header band and moved content masks below it;
  - aligned right panels to a stable right-column grid;
  - weakened the footer mask/source band;
  - raised Atlas semantic business text out of 6–7px microtype;
  - expanded macro decision matrix capacity instead of shrinking text;
  - moved the process state-machine page upward to improve slide-05 visual balance.

### Verification Commands

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/check_visual_layout_architecture.py
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

Manual rendered review artifact:

```text
build/visual-system-market-atlas-infographic/market-atlas-infographic-actual-contact-sheet-grammar-final.png
```

### Files Affected

- `scripts/compile_spec_to_ir.py`
- `scripts/check_visual_layout_architecture.py`
- `docs/learning/market-atlas-visual-layering.md`

### Future Prevention Rule

Do not call an Atlas deck accepted just because overlap/fidelity/editability gates pass. Atlas needs its own layout grammar gate: light header, stable grid, anchored right rail, weak footer, and no business-critical microtext. Rendered contact-sheet review remains mandatory after changing this visual system.

## Problem 3: Passing overlap checks while failing text spacing/alignment mechanics

### Symptom

A deck can pass collision checks and visual fidelity while still looking unprofessional because:

- priority text blocks are not overlapping but are only a few pixels apart;
- objects are visually near-aligned but not actually aligned;
- repeated rows/cards drift in gutter or width;
- child text leaves its semantic parent container.

### Root Cause

Previous gates treated layout mostly as independent boxes. That misses the professional layout layer: relationships between boxes. The missing mechanisms were:

- a role-aware text distance field that scans text block pairs;
- an alignment graph that validates declared left/top/row/equal-gutter/parent-padding relations;
- a requirement that generated slides carry non-empty `layout_relations`.

### Fix

Added:

- `scripts/check_text_spacing.py`
- `scripts/check_alignment_graph.py`
- `tests/test_text_spacing_and_alignment_gates.py`
- `references/text-spacing-and-alignment-qa.md`

Integrated both gates into `scripts/validate_visual_systems.py` and `scripts/validate_skill.py`.

### Future Prevention Rule

Do not describe layout acceptance as “no obvious overlap.” Release QA must state which text-distance and alignment relationships were traversed and validated.

## Problem 4: Atlas process signal rail can pass gates but still read as floating

**Context:** Rebuilding the Market Atlas validation deck with the new text-spacing and alignment-graph gates.

**Symptom:** The process slide (`ls05`) originally placed a three-card `SIGNAL FIELD` outside the execution state-machine panel. Automated gates passed, but full-size rendered review judged the rail as floating because the slide had four process steps and only three signal cards.

**Root cause:** The signal evidence was positioned as a separate right/top module instead of being integrated into the process grammar. The visual mapping was semantic but not spatially auditable.

**Fix:** Embed `STEP SIGNAL WINDOWS` inside the `process-state-map` panel, render four native signal chips, keep metric labels as exact same-content text, and map each chip to the corresponding 01-04 process node by position and connector lines. Move the feedback loop above the nodes and move the legend into the right governance area so step explanations have breathing room.

**Prevention rule:** Process-style Atlas pages must use a 1:1 `signal window -> process node` grammar. Do not use a detached signal rail when the main narrative is a state machine.

## Problem 5: Atlas header repair can create title-zone overweight

**Context:** Full-size review found the kicker line visually too close to the Chinese title.

**Symptom:** Moving the title down fixed kicker/title crowding but triggered `ATLAS_TITLE_ZONE_OVERWEIGHT` on long-title slides because the subtitle band extended to the body start.

**Root cause:** A global hard title offset ignored long-title height and subtitle budget.

**Fix:** Keep the kicker at `y=78`, move the title only to `y=98`, and reduce the Atlas title/subtitle gap to 8px. This preserves separation without pushing the title band into the map grammar.

**Prevention rule:** Header fixes must satisfy both local text spacing and global Atlas title-zone weight. Never solve kicker/title collision by simply pushing all title content downward.

## Problem 6: Route-map children can be legally contained but semantically overlapping

**Context:** User review found serious container overlap on Market Atlas page2/page3 even after generic overlap, text spacing, alignment graph, visual fidelity, and editability gates passed.

**Symptom:**

- Slide `ls02` macro route map placed the bottom SCORE/STAGE/ACTION/ROLLBACK rule matrix inside the same parent panel as WATCH/CONFIRM/DEPLOY cards, but the matrix band intruded into the card/node region.
- The `NOW: CONFIRM EARLY` marker read as a floating panel covering the CONFIRM card body.
- Slide `ls03` allocation bridge placed the DD drawdown rule outside the route-map component and too close to the footer/risk rail, creating an orphaned guardrail/footer collision.

**Root cause:** Generic bbox checks treated these objects as valid children inside the parent route-map panel. The missing rule was not geometric containment; it was component grammar: route-map cards, floating status badges, bottom bands, guardrail notes, and footer rails need explicit slots and semantic overlap policy.

**Fix:**

- Added `scripts/check_component_layout_contract.py` and regression tests for Atlas route-map bottom-band intrusion, floating badge coverage, orphaned guardrails, and footer/guardrail collision.
- Reworked `add_atlas_budget_route_map(...)` so `ls02` uses separate upper card/node slots and a true bottom rule-matrix slot; the status marker is a small chrome badge rather than a body-covering card.
- Reworked `ls03` allocation bridge so limit/DD rules stay inside the route-map panel with sufficient text box height and spacing from asset rows/footer.
- Integrated `check_component_layout_contract.py` into `scripts/validate_visual_systems.py` as a formal release gate.

**Verification:**

```bash
python3 -m py_compile scripts/compile_spec_to_ir.py scripts/check_component_layout_contract.py scripts/validate_visual_systems.py
python3 scripts/validate_visual_systems.py
python3 scripts/check_component_layout_contract.py build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json --report verification/atlas-component-layout-contract-fixed-report.json
python3 scripts/validate_skill.py
```

Expected result:

```text
PASS visual systems ... market-atlas-infographic score>=95 edit=100
PASS component layout contract
ALL CHECKS PASSED
```

**Prevention rule:** Do not rely on parent-child containment to accept Atlas route-map layouts. Complex components need slot-level contract checks: card body, status badge, bottom band, guardrail note, and footer must occupy declared regions with explicit semantic-overlap policy.

