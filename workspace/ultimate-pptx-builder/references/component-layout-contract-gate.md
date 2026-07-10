# Component Layout Contract Gate

## When to use

Use this reference when a PPTX deck passes generic layout, text spacing, alignment, fidelity, or editability gates but a reviewer still sees container-level defects such as:

- bottom bands intruding into cards;
- floating badges covering card bodies;
- guardrail notes orphaned between a component panel and footer;
- footer/risk rails colliding with business annotations;
- nested panels or ghost containers that are legal parent/child containment but visually broken.

This is especially relevant for Market Atlas route-map, allocation-map, signal-field, process-state-machine, and decision-console components.

## Core lesson

Do **not** claim that PPTX layout quality can be fully determined by a single geometric gate. The correct framing is:

```text
Deterministic gates catch formalizable structural defects.
Vision model / human review catches remaining semantic and aesthetic defects.
Every recurring visual-review defect should be converted into a deterministic regression when possible.
```

For generated decks where IR carries roles, boxes, z-order, components, parents, slots, and layout relations, many severe issues can be deterministic blockers. For arbitrary external PPTX without semantic metadata, detection is necessarily weaker.

## Gate shape

A component layout contract gate should validate component grammar, not just bbox overlap:

```text
component
  ├── slots: header, card-row, badge, bottom-band, legend, guardrail, footer-gap
  ├── allowed overlaps: text inside card, icon inside badge, child inside parent
  ├── conditional overlaps: small corner badge with bounded overlap ratio
  └── forbidden overlaps: bottom band over card body, floating badge over semantic card, guardrail/footer collision
```

Recommended report fields:

```json
{
  "gate": "component_layout_contract",
  "release_decision": "fail",
  "blocking_count": 4,
  "issues": [
    {
      "code": "ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION",
      "severity": "blocking",
      "slide_id": "ls02",
      "object_ids": ["band", "card1", "card2"],
      "evidence": {"overlap_h": 16, "required_gap": 12}
    }
  ]
}
```

## Market Atlas blocker codes

Use these as durable regression targets:

```text
ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION
ATLAS_FLOATING_BADGE_COVERS_CARD
ATLAS_GUARDRAIL_TEXT_ORPHANED
ATLAS_FOOTER_GUARDRAIL_COLLISION
ATLAS_ROUTE_MAP_DOUBLE_PANEL_STACKING
ATLAS_PANEL_BOTTOM_GHOST_LINE
```

## TDD workflow

When a user reports a container-level defect:

1. Treat it as a gate-coverage bug, not as subjective feedback to hand-wave away.
2. Create a minimal failing IR fixture/test that captures the defect class.
3. Run the test first and confirm RED.
4. Implement the smallest deterministic component rule to make it GREEN.
5. Add a positive fixture so the rule does not ban legitimate component composition.
6. Run the rule against other visual systems to check false positives.
7. Only after the current bad output is fixed should the new gate be promoted into the formal release validator.

## Promotion rule

Do not wire a new component gate into the main release validator while the current known-bad deck still fails it, unless the intent is to block release immediately. Safer sequence:

```text
1. Add regression tests and standalone gate.
2. Prove current bad deck fails and unrelated systems pass.
3. Fix generator/layout.
4. Verify the deck passes the new gate.
5. Promote the gate into validate_visual_systems.py.
```

This prevents weakening the gate just to keep a legacy failing validation green.
