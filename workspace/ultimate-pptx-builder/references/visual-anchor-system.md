# Visual Anchor System

## Purpose

A visual anchor is not a one-off template. It is a bounded generative visual region: one recognizable style family that can produce many decks without collapsing into sameness or drifting into another style.

```text
Immutable DNA + Mutable Coordinates + Mutation Operators + PPTX Material Policy + Anti-Drift Rules
```

## Anchor Fields

| Field | Purpose |
|---|---|
| `immutable_dna` | Non-negotiable features; without them the anchor is lost |
| `mutable_coordinates` | Tunable axes that create variation inside the same style family |
| `mutation_operators` | Allowed transformations for layout rhythm and visual energy |
| `page_role_variants` | How cover, data, table, compliance, and closing pages adapt |
| `density_modes` | Low/medium/high/appendix density behavior |
| `pptx_material_policy` | Native/vector/raster policy under Office constraints |
| `anti_drift` | What would make the style generic or off-brand |
| `qa_rubric` | Scoring rules for DNA, distinctiveness, editability, and template smell |

## Acceptance

A visual anchor is acceptable when:

- it declares immutable DNA and at least three mutable coordinates;
- it supports multiple page roles and density modes;
- it forbids rasterizing critical finance content;
- its generated IR contains recognizable DNA evidence;
- multiple variants from the same anchor are distinct but still recognizable;
- `scripts/check_visual_anchor.py` returns `release_decision=pass`.

## Controlled Variation Principle

Do not prove an anchor by adding another style name. Prove it by generating several decks from the same anchor with different coordinate values:

```text
glass-fintech-pptx
  ├─ sober-committee
  ├─ luminous-strategy
  └─ dense-risk-review
```

The family should remain recognizable while avoiding repeated template smell.
