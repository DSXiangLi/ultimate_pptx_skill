# Authored Layout Graph

## Purpose

`layout_relations` are useful, but inferred relations alone are not enough for finance-grade PPTX QA. Complex components need authored evidence that says which component grammar the compiler intended, which slots exist, and which relationships are semantic rather than accidental geometry.

The authored layout graph records this intent in Slide IR:

```json
{
  "layout_graph": {
    "source": "authored",
    "components": [
      {
        "id": "ls02_budget_map_panel",
        "type": "macro-budget-route-map",
        "contract_ref": "atlas-route-map",
        "root": "ls02_budget_map_panel",
        "slots": {
          "card_lane": ["ls02_macro_zone_1", "ls02_macro_zone_2", "ls02_macro_zone_3"],
          "status_badge": ["ls02_macro_now_card", "ls02_macro_now_text"],
          "bottom_matrix": ["ls02_macro_rule_matrix", "ls02_macro_matrix_1_body"]
        },
        "relations": [
          {"type": "row", "source": "authored"},
          {"type": "semantic-child", "allowed_overlap": "corner-badge", "source": "authored"},
          {"type": "separate-band", "min_gap": 8, "source": "authored"}
        ]
      }
    ]
  }
}
```

## Why this exists

The Atlas page2/page3 incident showed that:

- objects can be inside the same parent and still violate component semantics;
- a bottom matrix can be geometrically contained but visually intrude into route cards;
- a `NOW` status marker can be legal overlap only if it is a corner badge, not a body-covering panel;
- a guardrail note can be present but semantically orphaned if it sits between the route map and footer.

`layout_graph` prevents QA from guessing those intentions after the fact.

## Current scope

Current authored graph support covers Market Atlas route-map components:

- `macro-budget-route-map` for slide2-style staged risk-budget routes;
- `allocation-bridge-route-map` for slide3-style current/proposed/limit bridges.

The deck also declares:

```json
"component_contract_refs": ["atlas-route-map"]
```

## Acceptance

```bash
python3 -m unittest tests/test_authored_layout_graph.py -v
python3 scripts/validate_visual_systems.py
```

Expected:

- `market-atlas-infographic` deck declares `atlas-route-map` in `component_contract_refs`.
- `ls02` and `ls03` carry `layout_graph.components` with `contract_ref=atlas-route-map`.
- The graph only keeps object IDs that actually exist in the generated slide.
- Existing `layout_relations` still exist; authored graph does not replace alignment graph validation yet.

## Boundary

This is evidence, not a layout solver. It records what the compiler authored. Future work can make the solver consume the same component contracts before object generation.
