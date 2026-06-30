# Visual-System Generalization

A visual-language gate inside one anchor is not enough. It can still overfit to one local optimum, such as dark glass finance dashboards.

## Rule

To prove generality, validation must compile the same content and same narrative intent through multiple full style anchors.

Current required anchors:

- `glass-fintech-pptx` — dark translucent finance dashboard grammar.
- `paper-analyst-report` — light editorial research memo grammar.
- `market-atlas-infographic` — modular map/tile infographic grammar.

## Acceptance Criteria

A multi-visual-system validation run is accepted only when all of the following hold:

- At least three full style anchors compile from the same content contract and the same `narrative_intent`.
- At least two style anchors are visually distant from the original dark-glass finance anchor.
- Each style anchor declares a distinct `visual_system_grammar` with surface, composition, material, chromatic mode, and container grammar.
- Pairwise visual-system grammar distance is high enough that a new system cannot be a shallow recolor.
- Critical business text from the source contract is preserved as native editable PPTX text in every generated system.
- Every system exports a real `.pptx` and passes layout safety, PPTX export audit, visual fidelity, and QA editability gates.
- Rendered contact sheets are reviewed, and at least the densest page of each new visual system receives full-size visual review.

## Release Criteria

Release is blocked unless:

- `python3 scripts/validate_visual_systems.py` reports `PASS visual systems`.
- `python3 scripts/validate_skill.py` reports `ALL CHECKS PASSED`.
- No full-size rendered-page review finds blocking overlap, unreadable priority text, hidden critical content, or misleading validation-artifact truncation.

## Blocking Failures

- A new style anchor changes slide content to pass layout.
- Critical business text is missing from native editable PPTX objects.
- The style anchor only recolors an existing visual system.
- The style cannot export real `.pptx` and pass layout/render/QA gates.
- Contact-sheet review or full-size review finds a blocking visual issue after automated gates pass.

## Verification

Run:

```bash
python3 scripts/validate_visual_systems.py
```

The validator builds temporary contracts under `build/visual-system-*` from the same base contract and checks `visual_system_grammar`, native text coverage, layout safety, PPTX export audit, visual fidelity, QA editability, and pairwise system distance.
