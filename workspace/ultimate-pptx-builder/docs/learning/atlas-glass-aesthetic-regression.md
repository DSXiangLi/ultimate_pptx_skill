# Atlas / Glass Aesthetic Regression Lessons

Use this note when PPTX exports pass package, fidelity, editability, and layout gates but rendered PNGs still look visually weak.

## Failure Pattern

### Glass

A Glass deck can technically pass while losing its visual DNA when the representative visual language drifts from `luminous-glass` to a sober/matte variant.

Rendered symptoms:

- Luminous orb becomes too small or too transparent.
- Background grid/ruler lines visually dominate the glass material.
- The page reads as a dark dashboard/table instead of glass-fintech.

Root cause found in this iteration:

- Cross-system representative used `matte-institutional` instead of the flagship `luminous-glass` language.
- Orb/glow geometry and opacity were reduced enough that the signature glass material disappeared.
- Automatic PPTX package/fidelity checks did not catch the aesthetic regression.

Repair rule:

- Glass representative must preserve visible `spotlight-orb`, `luminous-ribbon`, `glass-panel`, and `risk-rail` roles.
- Keep the orb visible, but use layout gates to prevent it from intruding into title safe zones.

### Market Atlas

Atlas can pass technical gates while still looking like dashboard cards or ordinary charts on a map background.

Rendered symptoms:

- `SIGNAL FIELD` is only KPI cards.
- `ALLOCATION ROUTE MAP` is a chart/time axis with route labels.
- Right-side decision panels are empty, wireframe-like, or duplicate metrics.
- `LIMIT` and `DD GUARDRAIL` appear as labels without auditable thresholds.

Root cause found in this iteration:

- The compiler emitted dashboard/chart/card skeletons and attached Atlas terminology.
- Gates checked roles, package validity, editability, and fidelity, but did not require decision semantics.

## Required Atlas Semantics

A Market Atlas slide is not acceptable unless the map grammar answers:

1. What signal moved?
2. How does the signal score or veto affect regime/stage?
3. What is the current stage/state?
4. What action follows?
5. What limit or guardrail stops the action?
6. What rollback path applies if the thesis fails?

## Gate Requirements Added

- Slide 02 macro route must expose a native decision matrix with `SCORE`, `STAGE`, `ACTION`, `ROLLBACK`, `政策VETO`, and `CONFIRM EARLY`.
- Slide 03 allocation bridge must expose `Trigger`, `Action`, `Funding`, `Limit`, `Guardrail`, `DD>5%`, and `另类现金≥8`.
- Semantic Atlas route IDs such as `_macro_route_`, `_bridge_route_`, `_decision_route_`, `_state_route_`, and `_scenario_branch_` must be treated as business routes, not decorative background motifs.
- Business nodes such as `_bridge_node_`, `_state_node_`, `_budget_station_`, `_macro_station_`, `_scenario_zone_`, and `_decision_node_` must not be treated as background motif nodes.

## Human Review Rule

A green automated run remains necessary but insufficient.

After changing a visual system:

1. Export real `.pptx`.
2. Render with LibreOffice / actual PPTX renderer.
3. Build a contact sheet.
4. Review full-size slides, especially the previously failing style.
5. Do not call the result complete if the first impression is still “dashboard/chart with map labels.”

Current accepted state from this iteration:

- Glass: no blocker/major; minor decorative density only.
- Atlas slide02: no blocker/major after adding policy VETO and Score → Stage → Action → Rollback matrix.
- Atlas slide03: no blocker/major after adding Trigger → Action → Funding → Limit → Guardrail chain, `DD>5%`, weekly drawdown threshold, and `另类现金≥8`.
