# Visual DNA Realization Gate

## Purpose

A visual system is not accepted merely because it declares `visual_system_grammar` or changes palette/background decoration. The gate checks whether visual DNA is realized through information-bearing PPTX objects: metric cards, charts/tables, route maps, signal fields, risk/source rails, guardrails, and component grammar.

This responds to the learning that good PPTX style cannot be a shallow recolor or decorative overlay. If chart grammar, card geometry, typography-bearing components, tables, route maps, and footer/source treatment remain generic, the style is not a real visual system.

## Script

```bash
python3 scripts/check_visual_dna_realization.py <deck.ir.json> --report <visual-dna-realization-report.json>
```

The gate is called by:

```bash
python3 scripts/validate_visual_systems.py
```

## Blocking codes

- `VISUAL_DNA_GRAMMAR_MISSING` — deck has no visual grammar declaration.
- `VISUAL_DNA_INFORMATION_COMPONENT_MISSING` — required style-specific information-bearing components are absent.
- `DECORATION_ONLY_VISUAL_DNA` — decoration outnumbers semantic components so heavily that the style is likely background/orb/line dressing.
- `VISUAL_DNA_NARRATIVE_ROLES_MISSING` — title/body/risk narrative roles are absent.
- `VISUAL_DNA_PRIORITY_COMPONENT_TOO_WEAK` — semantic visual components are present but not editable/intentional enough.
- `VISUAL_DNA_COMPONENT_CONTRACT_EVIDENCE_MISSING` — Atlas route-map DNA lacks component contract refs or authored layout graph evidence.

## Style-specific realization requirements

### Glass fintech

Must realize information through roles such as:

- `glass-panel`
- `metric-card` / `metric`
- `chart`
- `risk-rail`

Decorative roles such as `spotlight-orb` and `luminous-ribbon` are allowed, but they cannot be the main evidence of the style.

### Paper analyst report

Must realize information through roles such as:

- `paper-sheet`
- `ledger-metric`
- `chart` / `table`
- `research-folio` / `analyst-note`

Editorial rules are useful, but they are not enough by themselves.

### Market Atlas infographic

Must realize information through roles such as:

- `route-map`
- `signal-field`
- `scenario-map`
- `process-state-map`
- `map-node` / `signal-node`
- `guardrail`

Atlas also requires `component_contract_refs` and authored `layout_graph.components` evidence, because map-like visual systems otherwise risk passing as decorative route lines without component semantics.

## Acceptance

```bash
python3 -m unittest tests/test_visual_dna_realization.py -v
python3 scripts/validate_visual_systems.py
python3 scripts/validate_skill.py
```

Expected:

- shallow decoration-only fixture fails;
- Glass/Paper/Atlas realization fixtures pass;
- all three real visual systems pass with zero blockers;
- `validate_skill.py` runs the visual DNA realization regression test.
