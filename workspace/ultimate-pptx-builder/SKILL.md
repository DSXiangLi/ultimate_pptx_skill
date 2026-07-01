---
name: ultimate-pptx-builder
description: Use when creating high-end editable PowerPoint decks from rich visual concepts, HTML-like previews, financial narratives, or programmable design systems. Builds PPTX via IR-first authoring, explicit editability budgets, native/vector/raster conversion policy, and mandatory QA gates.
version: 0.1.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [pptx, powerpoint, editable-decks, html-to-pptx, design-systems, qa]
    related_skills: [powerpoint, hermes-agent-skill-authoring, writing-plans]
---

# Ultimate PPTX Builder

## Overview

This skill builds **editable, finance-grade PPTX decks** from rich visual concepts without pretending that arbitrary HTML can be perfectly converted to editable PowerPoint. The core architecture is **IR-first**:

```text
Content Contract → Narrative Topology → Style Program → Slide IR
       ↓                  ↓                  ↓             ↓
Compliance          Layout Grammar      Visual DNA     HTML Preview + PPTX Export
                                                        ↓
                                      Fidelity / Editability / Design / Practicality QA
```

HTML is allowed as a preview and layout engine, but it is not the source of truth. The source of truth is a typed **Slide IR** containing native PowerPoint objects, vector islands, raster islands, and explicit editability budgets.

## Learning Notes Rule

Before modifying an area with prior discoveries, read `docs/learning/` first. When development reveals and solves a new issue, add a learning note with context, symptom, root cause, fix, verification command, affected files, and prevention rule. Current visual-rendering learnings live in `docs/learning/phase4b-visual-rendering.md`; glass showcase learnings live in `docs/learning/glass-fintech-showcase.md`; Atlas/Glass aesthetic regression learnings live in `docs/learning/atlas-glass-aesthetic-regression.md`.

## When to Use

Use this skill when the user asks for:

- HTML-like visual effects delivered as `.pptx`.
- Editable PPTX rather than screenshots.
- Financial institution decks with strong visual design.
- A reusable PPTX generation workflow or skill.
- Converting an existing HTML/visual concept into an editable PowerPoint architecture.
- Building deck style systems that should not collapse into one-off templates.

Do **not** use this skill for:

- Simple one-off slides where standard `powerpoint` skill is sufficient.
- Pure image posters where editability is irrelevant.
- Promising arbitrary DOM/CSS perfect native PowerPoint conversion.

## Core Contract

Every generated deck must carry four explicit budgets:

| Budget | Required Question | Blocking Failure |
|---|---|---|
| Fidelity | Does PPTX visually match the preview? | Critical layout/text drift |
| Editability | Are business-critical objects native/editable? | Title/body/data/risk text rasterized |
| Design | Is the page visually strong and narratively clear? | No hierarchy, weak motif, broken rhythm |
| Practicality | Will it work in a finance/Office workflow? | Missing source/risk note, tiny fonts, huge file |

## Workflow

### Step 1 — Content Contract

Create a content contract before visual design:

- audience and scenario
- business goal
- narrative topology
- required data/source fields
- compliance/risk text
- editability priorities

**Acceptance Gate 1: Content Contract**

- [ ] No invented numbers, sources, or quotes.
- [ ] Risk / disclaimer / source slots are present when finance content is involved.
- [ ] Each slide has one primary narrative job.
- [ ] Business-critical fields have editability priority `4` or `5`.

### Step 2 — Style Program

Choose or define a style program using:

- visual tension
- layout grammar
- token pack
- Base DNA
- SOTA DNA
- PPTX material strategy
- degradation rules
- density modes

**Acceptance Gate 2: Style Program**

- [ ] The style has Base DNA: remove it and the style no longer exists.
- [ ] The style has at least two SOTA DNA moves that a generic model would not reliably apply by default.
- [ ] The style declares which objects must remain native and which may become raster/vector islands.
- [ ] The style supports the required information density.

### Step 2B — Deep Style Showcase

For the first production-grade style anchor, run `glass-fintech-pptx` end-to-end before adding more style presets:

```bash
python3 scripts/validate_glass_showcase.py
```

**Acceptance Gate 2B: Glass Fintech Showcase**

- [ ] At least three slides compile from `examples/glass-fintech-showcase.contract.json`.
- [ ] The showcase uses no `rasterIsland` objects in the MVP path.
- [ ] Title/body/metric/risk text remains native with priority >= 4.
- [ ] At least one priority-5 financial chart exports as `editable-vector-chart`, not raster.
- [ ] Visual fidelity score is >= 88.
- [ ] QA editability score is >= 95.
- [ ] A visual QA fix-and-reverify cycle is recorded in `verification/glass-fintech-showcase-validation.md`.

### Step 2C — 15-Slide Narrative Benchmark

After the 3-slide showcase passes, run a longer deck to test narrative quality and content variety in the same style anchor:

```bash
python3 scripts/validate_glass_benchmark.py
```

**Acceptance Gate 2C: Glass Fintech Benchmark**

- [ ] Exactly 15 slides compile from `examples/glass-fintech-benchmark.contract.json`.
- [ ] The contract includes simulated realistic finance-user input, audience, scenario, and data assumptions.
- [ ] Each slide has one `narrative_job` and a finance risk/source rail.
- [ ] The benchmark covers cover, summary, dashboard, chart focus, table, matrix, scenario, process, timeline, quote, compliance, and action plan pages.
- [ ] At least four charts export as `editable-vector-chart`.
- [ ] At least two tables export as `editable-vector-table`.
- [ ] The benchmark uses no `rasterIsland` objects in the MVP path.
- [ ] `scripts/check_layout_safety.py` passes with zero blocking layout/text issues.
- [ ] No bottom-safe-zone, footer-separation, text-overflow, line-leading, title/content gap, title/decor collision, container-overlap/double-panel, oversized page-number, table-density, or compliance-density blocker remains.
- [ ] Visual fidelity score is >= 88 and QA editability score is >= 95.
- [ ] A visual QA fix-and-reverify cycle is recorded in `verification/glass-fintech-benchmark-validation.md`.


### Step 2C-V — Controlled Visual-Language Variants

Before declaring a visual anchor extensible, prove it with controlled visual languages that are visibly different **at grammar level**, not merely by decoration tuning or business-scenario changes. Read `references/visual-anchor-system.md` and `references/visual-variant-distinctiveness.md`, then run:

```bash
python3 scripts/check_narrative_visual_orthogonality.py
python3 scripts/validate_glass_variants.py
```

**Acceptance Gate 2C-V: Visual-Language Distinctiveness**

- [ ] `visual_language` and `narrative_intent` are separate fields; legacy `visual_variant` is not used for controlled visual-language validation.
- [ ] Controlled visual-language validation uses `examples/variants/glass-fintech-visual-language-base.contract.json` as the same-content base.
- [ ] The same slides and same `narrative_intent` compile under at least three visual languages.
- [ ] Only visual coordinates change across the controlled visual-language runs.
- [ ] Coordinate changes materialize into PPTX object evidence, not just JSON declarations.
- [ ] Pairwise visual languages differ in motif roles, panel material, metric grammar, footer/source-band treatment, layout rhythm, or chart/table treatment.
- [ ] The gate blocks weak variants with `WEAK_COORDINATE_REALIZATION`, `COMPONENT_GRAMMAR_UNCHANGED`, `VISUAL_VARIANT_DISTANCE_TOO_LOW`, `VISUAL_NARRATIVE_COUPLING`, or `LEGACY_VISUAL_VARIANT`.
- [ ] Rendered contact sheets are reviewed; if they look nearly identical, treat it as a generation bug even if schema/fidelity/editability scores pass.

### Step 2E — Multi-Visual-System Generalization

After one visual anchor proves internal visual-language extensibility, prove the architecture is not trapped in a single local optimum. Compile the same content contract and same `narrative_intent` through multiple full visual systems:

```bash
python3 scripts/validate_visual_systems.py
```

**Acceptance Gate 2E: Cross-Visual-System Generalization**

- [ ] Validation uses one same-content base contract and keeps `narrative_intent` fixed.
- [ ] At least three full style anchors compile through the same IR → PPTX → render → QA pipeline.
- [ ] The baseline dark glass anchor remains valid, but at least two additional anchors are visually distant from it.
- [ ] Each style anchor declares `visual_system_grammar` including surface, composition, material, chromatic mode, and container grammar.
- [ ] Each style system preserves critical business text as native editable text; missing native content is blocking.
- [ ] Pairwise visual-system grammar distance is checked so a new anchor cannot be a shallow recolor.
- [ ] Real `.pptx` files are exported and rendered; layout safety, editability, and visual fidelity must pass for every system.


### Step 2D — Layout and Text Safety Gate

Before calling any long-form PPTX deck accepted, run the executable layout/typesetting gate:

```bash
python3 scripts/check_layout_safety.py <deck.ir.json> --report <layout-safety-report.json>
```

This gate is blocking because knowledge-only standards are insufficient. It checks safe zones, bottom overflow risk, title/page-number collisions, priority text capacity, dense table readability, and repeated oversized page-number motifs.

**Acceptance Gate 2D: Layout/Text Safety**

- [ ] `release_decision` is `pass`.
- [ ] `blocking_count` is `0`.
- [ ] Priority >=4 text has enough estimated box capacity under the CJK-aware heuristic.
- [ ] Critical objects stay inside the slide safe zone and bottom projection/export safe area.
- [ ] Decorative page-number systems do not dominate content-heavy long decks.
- [ ] Any accepted exception is documented in the deck validation record.

### Step 3 — Slide IR

Generate Slide IR, not raw HTML. Each object must have:

- stable `id`
- `type`
- `role`
- `box`
- `editability`
- `render_policy`
- source metadata when rasterized

**Acceptance Gate 3: IR Integrity**

- [ ] Every object has `id`, `type`, `box`, and `editability`.
- [ ] Text with priority ≥4 uses `render_policy: native`.
- [ ] Raster islands never contain critical title/body/risk text.
- [ ] Z-order is deterministic.
- [ ] IDs are unique within a slide.

### Step 4 — HTML Preview

Render the IR to HTML preview. Browser layout may be used to compute bounding boxes, but the browser DOM must map back to IR IDs via `data-ir-id`.

**Acceptance Gate 4: Preview Traceability**

- [ ] Every exportable DOM node maps back to an IR object.
- [ ] DOM-only decoration is not allowed to carry critical content.
- [ ] Computed layout can be written back to IR or sidecar layout data.

### Step 5 — PPTX Export

Export using the object conversion policy:

| IR Type | Preferred PPTX Output | Fallback |
|---|---|---|
| `text` | native text box | never raster for priority ≥4 |
| `shape` | native shape | raster only for complex effect priority ≤2 |
| `chart` | native chart or editable vector group | raster + data sidecar only if low priority |
| `table` | native table or grouped text/shapes | raster forbidden for finance tables |
| `icon` | SVG path → freeform | raster if purely decorative |
| `rasterIsland` | picture with metadata | n/a |
| `vectorIsland` | freeform group | raster if unsupported |

**Acceptance Gate 5: PPTX Object Audit**

- [ ] Native text boxes exist for all priority ≥4 text.
- [ ] Charts/tables marked priority ≥4 are not flat screenshots.
- [ ] Raster objects contain source metadata for regeneration.
- [ ] Object count and file size are within practical limits.

### Step 6 — QA Loop

Run all five QA gates:

1. visual fidelity comparison
2. editability audit
3. layout/text safety gate
4. visual/design critique
5. finance practicality check

**Acceptance Gate 6: Release Criteria**

- [ ] Fidelity score ≥ 90, or all deviations are documented and accepted.
- [ ] Editability score ≥ 90 for business-critical objects.
- [ ] No blocking compliance/practicality issue.
- [ ] At least one fix-and-reverify cycle has been completed for real deck output.

## Common Pitfalls

1. **Treating arbitrary HTML as the source of truth.** Use IR as source; HTML is a renderer.
2. **Rasterizing text to preserve beauty.** Business-critical text must remain native.
3. **Adding more style names instead of stronger style DNA.** Each style must be a generative program.
4. **Ignoring Office reality.** Fonts, charts, file size, print/PDF behavior, and corporate editing matter.
5. **Skipping QA because the preview looks good.** PowerPoint text metrics and rendering differ from Chromium.
6. **Trusting fidelity/editability scores as design acceptance.** Add layout/text safety and rendered-page review; a faithful PPTX can faithfully render a bad layout.

## Verification Checklist

- [ ] `references/architecture.md` explains the IR-first architecture.
- [ ] `references/acceptance-matrix.md` defines phase gates and blocking failures.
- [ ] `references/slide-ir-schema.md` defines all core object types.
- [ ] `references/editability-policy.md` defines priority and fallback rules.
- [ ] `references/style-program.md` defines Base/SOTA DNA and PPTX material strategy.
- [ ] `references/qa-loop.md` defines the five gates and release criteria.
- [ ] `references/layout-text-safety.md` defines the executable safe-zone and text-capacity gate.
- [ ] `references/layout-root-cause-and-exhaustive-qa.md` and `references/layout-defect-taxonomy.md` are consulted when a rendered deck passes automated gates but a reviewer still sees overlap, crowding, title/card collisions, line-leading defects, container-level layout defects, or style-DNA/page-role layout mismatch.
- [ ] `references/finance-benchmark-decks.md` is used when creating or evaluating long-form finance benchmarks; do not rely on pixel/editability scores alone.
- [ ] `references/phase4b-visual-fidelity.md` defines the render/diff loop.
- [ ] `references/style-glass-fintech-pptx.md` defines the first deep style anchor and acceptance target.
- [ ] `references/visual-dna-model.md` is consulted before accepting a visual anchor; first-glance difference is insufficient if chart grammar, typography, card/component geometry, and page-role layout skeleton remain the same.
- [ ] `scripts/check_visual_layout_architecture.py` classifies visible layout defects as local slide bugs, style-DNA adaptation bugs, or systemic skill/gate gaps, and blocks route/title intrusion, microtext, chart undersizing, process-page density overload, and page-role hierarchy mismatch.
- [ ] `scripts/check_pptx_package.py` validates Office-compatible PPTX package structure including slide master/layout/theme relationships; LibreOffice-openable minimal ZIPs are not enough.
- [ ] `scripts/check_layout_safety.py` enforces 64px bottom safe zone, 16px footer separation, CJK-aware text capacity, explicit multi-line leading budget, pairwise text collision checks, metric-card internal stack gaps/padding, visual container overlap/nesting rules, title-to-content gaps, table density/readability limits, compliance density rules, and anti-template page-number checks.
- [ ] `scripts/validate_glass_showcase.py` passes before adding another style preset.
- [ ] `scripts/validate_glass_benchmark.py` passes for the 15-slide narrative benchmark before expanding style presets.
- [ ] `docs/learning/README.md` and relevant learning notes were checked before modifying known problem areas.
- [ ] `schemas/*.json` are valid JSON.
- [ ] `examples/minimal-deck.ir.json` passes `scripts/validate_skill.py`.
- [ ] No document promises arbitrary HTML → perfectly editable PPTX.
