# Visual Anchor System

## Purpose

A visual anchor is not a one-off template, not a business-scenario preset, and not a background/palette skin. It is a bounded generative **visual region**: one recognizable style family that can produce many decks without collapsing into sameness or drifting into another style.

```text
Immutable DNA + Mutable Coordinates + Mutation Operators + PPTX Material Policy + Anti-Drift Rules
```

A mature deck compiler keeps these axes separate:

```text
Narrative Intent × Visual Language → Deck
```

- `narrative_intent` answers: what communication/business job does the deck serve?
- `visual_language` answers: what does the deck look and feel like?

## Anchor Fields

For the full DNA layer model, read `references/visual-dna-model.md`. A mature anchor must define more than surface and color: palette logic, typography system, surface/texture, light physics, layout archetypes, container grammar, component grammar, data-viz grammar, ornament/motif system, flow metaphor, density rhythm, and PPTX material translation.

| Field | Purpose |
|---|---|
| `immutable_dna` | Non-negotiable features; without them the anchor is lost |
| `mutable_coordinates` | Tunable visual axes that create variation inside the same style family |
| `controlled_visual_languages` | Named visual-language points inside the anchor; names must be visual, not narrative |
| `mutation_operators` | Allowed transformations for visual rhythm, component grammar, light, material, and density |
| `page_role_variants` | How cover, data, table, appendix, and closing pages adapt visually |
| `density_modes` | Low/medium/high/appendix density behavior |
| `pptx_material_policy` | Native/vector/raster policy under Office constraints |
| `anti_drift` | What would make the style generic or off-brand |
| `qa_rubric` | Scoring rules for DNA, distinctiveness, editability, and template smell |

## Acceptance

A visual anchor is acceptable when:

- it declares immutable DNA and at least three mutable visual coordinates;
- it supports multiple page roles and density modes;
- it forbids rasterizing critical finance content;
- its generated IR contains recognizable DNA evidence;
- multiple visual languages from the same anchor are distinct but still recognizable;
- visual-language checks do not depend on business/narrative names;
- `scripts/check_visual_anchor.py` returns `release_decision=pass`;
- `scripts/check_narrative_visual_orthogonality.py` returns PASS.

## Controlled Visual Languages, Not Scenario Variants

Do not prove an anchor by adding a business template name such as “committee deck” or “risk review deck”. Prove it by generating decks from the same anchor with different **visual language** coordinates:

```text
glass-fintech-pptx
  ├─ matte-institutional
  ├─ luminous-glass
  └─ terminal-cockpit
```

These are visual languages:

| Visual Language | Visual Meaning | Must Not Mean |
|---|---|---|
| `matte-institutional` | restrained luminosity, matte glass, precision rules, formal spacing, compact ledger metrics | investment committee only |
| `luminous-glass` | high light energy, spotlight orbs, luminous panels, hero KPI emphasis, presentation rhythm | strategy meeting only |
| `terminal-cockpit` | terminal grid, dense cockpit panels, status chips, monitoring source band, signal-coded accents | risk review only |

Business use belongs in `narrative_intent`, for example:

```text
investment_committee_decision
strategy_update
risk_review
```

Any combination should be possible when the content supports it:

```text
risk_review × matte-institutional
risk_review × luminous-glass
risk_review × terminal-cockpit
```

## Grammar-Level Distinctiveness

Coordinate variation is not accepted unless it is realized in visible PPTX grammar. A controlled visual language must change more than decorative glow parameters. At minimum, the compiler should materialize differences in several of these dimensions:

- motif roles, e.g. `institutional-gridline`, `spotlight-orb`, `terminal-gridline`;
- panel material, e.g. matte glass vs luminous glass vs dense cockpit panels;
- metric grammar, e.g. formal compact KPI vs hero KPI vs status chip;
- chart/table treatment, e.g. subdued grid vs spotlight chart vs monitoring grid;
- footer/source-band treatment, e.g. formal source band vs presentation source band vs monitoring status bar;
- layout rhythm and density.

Executable gates should block:

```text
WEAK_COORDINATE_REALIZATION
COMPONENT_GRAMMAR_UNCHANGED
VISUAL_VARIANT_DISTANCE_TOO_LOW
VISUAL_NARRATIVE_COUPLING
LEGACY_VISUAL_VARIANT
```

A visual language is only accepted when rendered PPTX contact sheets are visually distinguishable while still preserving immutable anchor DNA.

## Prevention Rule

If a visual-language name answers “what is this meeting/deck about?” it is not a visual-language name. Move it to `narrative_intent` and rename the visual language using visual vocabulary: material, light, typography, container grammar, motif, palette, density, or atmosphere.
