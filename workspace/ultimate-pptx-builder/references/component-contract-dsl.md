# Component Contract DSL

## Purpose

The Component Contract DSL turns recurring rendered-review defects into executable component grammar. It sits above generic bbox overlap checks and below human/vision aesthetic review.

It exists because `market-atlas-infographic` proved that objects can be legally contained inside one parent panel while still being semantically broken: bottom bands can intrude into route cards, status badges can cover card bodies, and guardrail notes can become orphaned between the map panel and footer.

## Contract shape

A contract is JSON and contains:

```json
{
  "id": "atlas-route-map",
  "version": 1,
  "component_selector": {"role": "route-map", "id_contains": "panel"},
  "slots": [
    {"id": "card_lane", "members": {"id_contains_any": ["_zone_"], "role_any": ["route-map", "map-node"]}},
    {"id": "bottom_band", "members": {"id_contains_any": ["rule_matrix"]}},
    {"id": "status_badge", "members": {"id_contains_any": ["now_card"]}}
  ],
  "rules": [
    {"type": "forbid_slot_overlap", "code": "ATLAS_ROUTE_MAP_BOTTOM_BAND_INTRUSION", "slot_a": "bottom_band", "slot_b": "card_lane"}
  ]
}
```

## Selectors

Selectors intentionally stay small and auditable:

- `id`
- `id_contains`
- `id_contains_any`
- `role`
- `role_any`
- `type`
- `type_any`
- `component`

Slots are scoped to the component root by default. Mark a slot as `external: true` when the contract must inspect related objects outside the component, such as footer/risk rails or orphanable guardrail notes.

## Rule types

### `forbid_slot_overlap`

Blocks substantial overlap between two semantic slots.

Use for:

- bottom rule matrix intruding into cards;
- ghost/double panels covering a content lane;
- legends covering data marks.

### `conditional_badge_overlap`

Allows a small status badge to overlap card chrome, but blocks deep body intrusion.

Use for:

- `NOW: CONFIRM EARLY` style state badges;
- small approval/check badges;
- status chips anchored to a component corner.

### `must_be_inside_component`

Blocks objects that should belong to the component but drift outside the component panel.

Use for:

- guardrail notes;
- route annotations;
- panel-owned source tags.

### `min_gap_between_slots`

Requires minimum vertical/horizontal separation between slots.

Use for:

- guardrail/footer gap;
- table/source-note gap;
- card row/legend gap.

## Current contract files

```text
schemas/component-contract.schema.json
examples/component-contracts/atlas-route-map.contract.json
scripts/check_component_contracts.py
```

## Acceptance commands

```bash
python3 -m unittest tests/test_component_contract_dsl.py -v
python3 scripts/check_component_contracts.py \
  build/visual-system-market-atlas-infographic/market-atlas-infographic.ir.json \
  --contracts examples/component-contracts \
  --report /tmp/atlas-component-dsl.json
```

Expected:

```text
PASS component contract DSL
release_decision=pass
blocking_count=0
```

## Design boundary

This DSL is not a full layout solver yet. It validates whether generated component geometry obeys declared component grammar. Future phases may add authored layout graph evidence and constraint solving.

## Prevention rule

When full-size rendered review finds a repeated component defect, do not add another one-off hard-coded Python branch first. Add or extend a component contract fixture, watch it fail, then implement the smallest DSL/gate behavior needed to make it pass.
