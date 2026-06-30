# Editability Policy

## Priority Scale

| Priority | Meaning | Default Policy |
|---:|---|---|
| 5 | must be editable | native only |
| 4 | should be editable | native; exception requires justification |
| 3 | useful to edit | native/vector preferred |
| 2 | nice to edit | raster allowed |
| 1 | no edit need | raster/locked allowed |

## Critical Roles

These roles are critical by default and must not be rasterized:

- `title`
- `body`
- `risk`
- `source`
- `footnote`
- `chart` with finance data
- `table` with finance data

## Native / Vector / Raster Decision

```text
Can PowerPoint represent it natively with acceptable fidelity?
  yes → native
  no  → can SVG/freeform preserve partial editability?
          yes → vectorIsland
          no  → rasterIsland with source metadata
```

## Raster Island Rules

A raster island is acceptable only if:

- it does not contain critical text/data,
- it has source metadata,
- it has regeneration instructions,
- it is marked replaceable or locked,
- the QA report lists it as intentionally rasterized.

## Acceptance Mechanism

For every deck, produce an editability audit table:

| Object ID | Role | Priority | Expected | Actual | Pass |
|---|---|---:|---|---|---|

Blocking failures:

- priority 5 object not native/data-editable
- risk/source text rasterized
- chart/table data flattened without explicit approval
