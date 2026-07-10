# Atlas Layout Grammar Gates

## Purpose

Market Atlas decks are finance map/route pages. They can pass generic overlap, editability, and visual-fidelity checks while still failing institutional layout quality. This reference defines the reusable Atlas-specific grammar that must be encoded in executable gates.

## Why Generic Gates Are Insufficient

Generic gates usually answer:

- Do text boxes overlap?
- Does text fit its box?
- Are objects inside safe zones?
- Does PPTX render similarly to the reference?

Atlas also needs to answer:

- Is the title band light enough to leave the map grammar dominant?
- Are content masks below the title band, not behind it?
- Is the right rail anchored to a stable column grid?
- Is the footer a weak compliance rail rather than a visual container?
- Is dense business logic expressed with readable components rather than 6–7px microtext?
- Do semantic map routes remain subordinate to the narrative hierarchy?

## Blocking Gate Codes

### `ATLAS_TITLE_ZONE_OVERWEIGHT`

Block when the union of title and subtitle extends too low, typically beyond `y≈214` on a 1280×720 canvas.

Prevention:

- keep title/subtitle in a light header band;
- reduce title size/weight before pushing content downward;
- move main map/content grammar to a stable body grid.

### `ATLAS_TITLE_ZONE_MASK_INTRUSION`

Block when large content masks overlap the title/subtitle band enough that the header reads like a heavy container.

Prevention:

- content masks should start below the title band;
- do not place large translucent panels behind title/subtitle copy;
- separate header caption layer from map/content layer.

### `ATLAS_RIGHT_PANEL_FLOATING`

Block when the right signal/decision panel drifts away from the intended right-column grid.

Typical anchors:

```text
right rail x ≈ 724–748
left map x ≈ 80–88
main body y ≈ 222+
```

Prevention:

- align right rail surfaces, cards, maps, and internal child labels to a declared right-column grid;
- use consistent gutter from the left analysis/map column;
- avoid per-slide ad hoc x offsets.

### `ATLAS_FOOTER_DOMINANCE`

Block when the footer mask is visually too large/opaque for a finance review deck.

Suggested threshold:

```text
footer mask h <= 44
footer opacity <= 0.90
```

Prevention:

- make source/risk rail thin and low-emphasis;
- keep compliance text readable but visually subordinate;
- never let footer masks become a second content container.

### `ATLAS_DENSITY_PARITY_FAILURE`

Block when a slide hides business semantics as microtext rather than using a proper density layout.

Current baseline:

```text
more than 4 business text objects below 8px => blocking
```

Prevention:

- increase component size or spacing;
- split dense logic across map + right rail;
- create decision strips/matrices with enough row height;
- do not delete same-content evidence to make the slide look cleaner.

### `ATLAS_CONTENT_MASK_BELOW_MOTIF`

Block when content masks sit below decorative grids/routes in z-order and therefore cannot protect readability.

Prevention:

- decorative grid/route layer below content masks;
- content masks above decoration and below business text/cards;
- semantic routes are allowed only when they support the narrative.

### `ATLAS_CONTENT_ZONE_OVERLAP`

Block when translucent content zones overlap and create muddy opacity or fake container collisions.

Prevention:

- use non-overlapping functional islands;
- maintain visible gutters between left map, right rail, and bottom/footer bands.

### `ATLAS_RIGHT_PANEL_BOTTOM_BAND_COLLISION`

Block when the right rail intersects the bottom allocation/status band.

Prevention:

- right rail and bottom band must have a visible gutter;
- do not run background masks behind semantic cards.

### `ATLAS_GRID_TOO_PROMINENT` / `ATLAS_ROUTE_TOO_PROMINENT`

Block when decorative grids/routes compete with business content.

Prevention:

- keep decorative grid atmospheric;
- semantic routes can be stronger, but decorative infrastructure lines must remain subordinate.

## Required Future Mechanisms

The current Atlas gates are still coarse. Future versions should add:

1. **Text distance field** — every priority text block pair gets a role-aware minimum spacing check.
2. **Alignment graph** — declared and inferred left/right/top/bottom/centerline/gutter relationships are validated.
3. **Component grammar contracts** — right rail, metric cards, decision matrices, scenario maps, and process state machines declare child padding, equal widths/heights, row gaps, and baseline alignment.
4. **Rendered geometry check** — compare actual PPTX-rendered PNG text/container extents against IR predictions, especially for Chinese native text.

## Acceptance Rule

Do not accept an Atlas-style deck because generic validators pass. Acceptance requires:

```text
layout_safety = pass
visual_layout_architecture = pass
atlas_layout_grammar = pass
rendered_contact_sheet_review = no blocker/major
same_content_evidence = preserved
```

If a human reviewer sees title dominance, footer dominance, right-rail drift, microtext density, ghost containers, or weak grid discipline after a PASS, treat that as a gate coverage bug first.
