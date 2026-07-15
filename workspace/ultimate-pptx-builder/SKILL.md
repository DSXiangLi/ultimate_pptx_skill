---
name: ultimate-pptx-builder
description: Use when creating high-end editable PowerPoint decks from rich visual concepts, HTML-like previews, financial narratives, programmable design systems, or existing PPTX files/templates that need cloning into reusable editable visual systems. Builds PPTX via IR-first authoring and a dual forward/reverse compiler with explicit fidelity, editability, design, practicality, and clone-learning QA gates.
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

This skill builds **editable, finance-grade PPTX decks** from rich visual concepts and learns from excellent existing PPTX decks without pretending that arbitrary HTML or arbitrary PPTX can be magically converted into perfect editable PowerPoint. The core architecture is **IR-first** and now supports a dual compiler:

```text
Forward Compiler:
  Content Contract → Narrative Topology → Style Program → Slide IR
         ↓                  ↓                  ↓             ↓
  Compliance          Layout Grammar      Visual DNA     HTML Preview + PPTX Export
                                                          ↓
                                        Fidelity / Editability / Design / Practicality QA

Reverse Compiler / PPTX Cloner:
  Existing PPTX → OOXML/theme/master/object inventory → Decompiled IR
        ↓                 ↓                                  ↓
  1:1 rebuild fidelity → archetype mining → visual DNA/component contracts
        ↓
  reusable generator + benchmark/gate/learning promotion
```

HTML is allowed as a preview and layout engine, but it is not the source of truth. The source of truth is a typed **Slide IR** containing native PowerPoint objects, vector islands, raster islands, and explicit editability budgets. For clone work, the original PPTX is evidence; the decompiled/rebuilt IR is the test harness; the reusable style program and component contracts are the product.

## Learning Notes Rule

Before modifying an area with prior discoveries, read `docs/learning/` first. When development reveals and solves a new issue, add a learning note with context, symptom, root cause, fix, verification command, affected files, and prevention rule. Current visual-rendering learnings live in `docs/learning/phase4b-visual-rendering.md`; glass showcase learnings live in `docs/learning/glass-fintech-showcase.md`; Atlas/Glass aesthetic regression learnings live in `docs/learning/atlas-glass-aesthetic-regression.md`; PPTX reverse-compiler roadmap notes live in `docs/learning/pptx-template-decompiler-roadmap.md`.

## When to Use

Use this skill when the user asks for:

- HTML-like visual effects delivered as `.pptx`.
- Editable PPTX rather than screenshots.
- Financial institution decks with strong visual design.
- A reusable PPTX generation workflow or skill.
- Converting an existing HTML/visual concept into an editable PowerPoint architecture.
- Building deck style systems that should not collapse into one-off templates.
- Cloning an existing `.pptx` into a reusable editable visual system, not just duplicating the file. For this workflow, follow `references/pptx-cloner.md`.
- Collecting, selecting, or learning from high-quality PPTX template/reference libraries. For this workflow, follow `references/pptx-template-research-library.md`.

Do **not** use this skill for:

- Simple one-off slides where standard `powerpoint` skill is sufficient.
- Pure image posters where editability is irrelevant.
- Promising arbitrary DOM/CSS perfect native PowerPoint conversion.
- Promising arbitrary PPTX → perfect reusable template conversion without staged specimen analysis, rebuild fidelity testing, and explicit fallbacks.

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


### Step 2F — PPTX Cloner / Reverse Compiler

When the user provides an existing PPTX, or when improving this skill from the curated template library, run the reverse-compiler workflow in `references/pptx-cloner.md` before trying to create a new forward style.

```text
source.pptx
→ specimen analysis pack
→ OOXML/theme/master/layout/object inventory
→ decompiled raw Slide IR
→ 1:1 rebuilt PPTX + visual/text/editability fidelity report
→ layout archetypes + visual DNA + component contracts
→ reusable generator
→ benchmark/gate/learning promotion
```

Start with the executable acceptance loop, then use the report's `optimization_queue` as the implementation backlog:

```bash
python3 scripts/run_pptx_cloner_loop.py \
  research/pptx-template-library/files/<template-id>.pptx \
  --deck-id <template-id> \
  --out specimens/<template-id> \
  --require-render \
  --max-iterations 3
```

If `specimens/<template-id>/cloner-loop-report.json` has `release_decision: fail`, fix the named blocker and rerun the same loop. Do not proceed to C3 rebuild, visual DNA extraction, component contracts, or reusable generator work until the current phase passes. Use `--skip-render` only for tests or render-unavailable environments; skipped renders are not valid evidence for visual abstraction quality.

Use `references/pptx-template-research-library.md` when selecting templates from `research/pptx-template-library/`. Do not clone every template equally. Start with a small P0 batch that covers distinct grammar families: dark executive, enterprise proposal, compliance tech, roadmap/journey infographic, finance explainer, tech brand system, and KPI scorecard.

**Acceptance Gate 2F: Clone Learning**

- [ ] A checkpoint exists before modifying this skill, visual systems, runtime contracts, validators, or benchmark boundaries.
- [ ] The cloner acceptance loop has run and the current phase report has `release_decision: pass` before advancing.
- [ ] The source PPTX provenance is recorded: original path, source URL/license if known, SHA256, slide count, theme/master/layout counts, and embedded-media caveats.
- [ ] Original slides render to full-size PNGs/contact sheets before abstraction begins.
- [ ] Decompiled IR preserves slide count, critical text, coordinates, z-order, object class, and source XML/object references.
- [ ] 1:1 rebuild fidelity is measured before claiming reusable abstraction quality.
- [ ] Critical title/body/data/source/risk text remains native/editable in clone and generator modes.
- [ ] Every promoted visual DNA or component contract has specimen evidence, not just aesthetic impression.
- [ ] New learnings are promoted into scripts, schemas, component contracts, benchmark cases, gates, or learning notes; do not leave important clone discoveries as prose only.


### Step 2D — Layout and Text Safety Gate

Before calling any long-form PPTX deck accepted, run the executable layout/typesetting gate:

```bash
python3 scripts/check_layout_safety.py <deck.ir.json> --report <layout-safety-report.json>
```

This gate is blocking because knowledge-only standards are insufficient. It checks safe zones, bottom overflow risk, title/page-number collisions, priority text capacity, dense table readability, and repeated oversized page-number motifs.

For complex component pages, also run the component layout contract gate:

```bash
python3 scripts/check_component_layout_contract.py <deck.ir.json> --report <component-layout-contract-report.json>
```

This gate catches container-grammar failures that can pass plain bbox/text checks: bottom bands intruding into cards, floating badges covering card bodies, orphaned guardrails, and footer/annotation collisions.

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

After HTML preview generation and before PPTX export, run the design/aesthetic contract gate:

```bash
python3 scripts/check_visual_aesthetic_contract.py <deck.ir.json> --report <visual-aesthetic-contract-report.json>
```

This is a taste gate, not a geometry gate. It catches defects that layout/fidelity/editability can miss: decorative glow/orb noise, weak visual restraint, style DNA collapse, motif overload, and effects that already look unattractive in the HTML preview.

**Acceptance Gate 4: Preview Traceability**

- [ ] Every exportable DOM node maps back to an IR object.
- [ ] DOM-only decoration is not allowed to carry critical content.
- [ ] Computed layout can be written back to IR or sidecar layout data.
- [ ] HTML-stage visual aesthetic contract passes with zero blockers before PPTX export.
- [ ] Large lower-edge glow/orb decoration remains atmospheric and does not compete with content, footer/source rails, or page hierarchy.

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

The visual/design critique starts at HTML preview time. If the HTML already shows poor hierarchy, noisy decoration, insufficient visual restraint, or weak aesthetic quality, fix the style program/compiler before exporting PPTX.

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
7. **Optimizing a single clone instead of the PPTX system.** For cloner work, source/rebuilt decks are diagnostic evidence, not the product. Every fix should become a reusable reverse-compiler capability, template-system rule, component contract, benchmark, or gate before being considered complete.

## Verification Checklist

- [ ] `references/architecture.md` explains the IR-first architecture and dual forward/reverse compiler boundary.
- [ ] `references/pptx-cloner.md` defines the PPTX Cloner / Reverse Compiler workflow, clone-specific QA gates, and learning promotion rules.
- [ ] `references/pptx-cloner-c3-object-coverage-roadmap.md` is consulted when C3 passes package/text/render gates but visual fidelity is still limited by unsupported object/material classes.
- [ ] `references/pptx-cloner-c3-image-reconstruction.md` is consulted when C3 rebuilds show image placeholders; it records the OOXML slide relationship → media package path → native `add_picture` reconstruction pattern.
- [ ] `references/pptx-cloner-c3-background-reconstruction.md` is consulted when rebuilt slides collapse to white or lose dark/colored template material; it records slide-level `p:bg` extraction and native background rebuild.
- [ ] `references/pptx-cloner-c3-picture-fill-shapes.md` is consulted when image-like visuals are encoded as `<p:sp>` picture fills rather than `<p:pic>` objects.
- [ ] `references/pptx-cloner-c3-group-recursion.md` is consulted when grouped icons/cards/decorative systems remain opaque placeholders; group containers should become traceable child objects before component mining.
- [ ] `references/pptx-cloner-c3-empty-text-containers.md` is consulted when C3 reports unsupported `text` objects after group recursion; empty/decorative text containers should be classified or skipped rather than drawn as placeholders.
- [ ] `references/pptx-cloner-c3-native-table-reconstruction.md` is consulted when C3 reports `table` placeholders; simple native tables should be extracted as structured `table_ref` IR and rebuilt with native editable PowerPoint tables before table styling is optimized.
- [ ] `references/pptx-cloner-c3-table-styling.md` is consulted after native table reconstruction when editable tables lose font, fill, margin, alignment, border, or theme fidelity.
- [ ] `references/pptx-cloner-acceptance-loop.md` is consulted for the phase-gated fail → diagnose → optimize → rerun contract; do not advance cloner phases unless the current loop report has `release_decision: pass`.
- [ ] `references/pptx-template-research-library.md` defines the curated template library policy and first-batch clone candidates.
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
- [ ] `scripts/check_visual_aesthetic_contract.py` runs after HTML preview and before PPTX export for glass showcase/benchmark decks; lower-edge decorative glow/orb noise is a blocking design failure.
- [ ] `scripts/check_visual_dna_realization.py` runs inside multi-system validation and blocks shallow style anchors that are realized mainly through decoration instead of information-bearing chart/table/card/route-map/source-risk grammar.
- [ ] `scripts/check_ooxml_visual_properties.py` audits exported PPTX XML so native alpha/critical text evidence survives materialization instead of existing only in IR/HTML previews.
- [ ] `scripts/check_rendered_perceptual_layout.py` runs on rendered slide PNGs and blocks meaningful bottom-edge pressure that object-level IR gates may miss.
- [ ] `examples/benchmarks/finance-pptx-benchmark-corpus.json` and `scripts/check_finance_benchmark_corpus.py` validate scenario × density × style coverage and require all formal gate reports before accepting multi-system regression.
- [ ] `scripts/check_alignment_graph.py` validates declared `layout_relations` so PPTX QA can check alignment intent rather than relying only on overlap or a few hard-coded component names.
- [ ] `scripts/check_component_layout_contract.py` validates complex component slots and semantic overlap policy so route-map bands, floating badges, guardrails, and footer annotations cannot pass as legal parent/child containment.
- [ ] `scripts/check_component_contracts.py`, `schemas/component-contract.schema.json`, and `examples/component-contracts/*.contract.json` keep component contracts declarative instead of one-off hard-coded Python rules.
- [ ] Atlas route-map slides declare `component_contract_refs` and authored `layout_graph.components` evidence so QA can distinguish intended component slots from geometry inferred after the fact.
- [ ] `scripts/check_visual_layout_architecture.py` classifies visible layout defects as local slide bugs, style-DNA adaptation bugs, or systemic skill/gate gaps, and blocks route/title intrusion, microtext, chart undersizing, process-page density overload, and page-role hierarchy mismatch.
- [ ] `scripts/check_pptx_package.py` validates Office-compatible PPTX package structure including slide master/layout/theme relationships; LibreOffice-openable minimal ZIPs are not enough.
- [ ] `scripts/check_layout_safety.py` enforces 64px bottom safe zone, 16px footer separation, CJK-aware text capacity, explicit multi-line leading budget, pairwise text collision checks, metric-card internal stack gaps/padding, visual container overlap/nesting rules, title-to-content gaps, table density/readability limits, compliance density rules, and anti-template page-number checks.
- [ ] `scripts/validate_glass_showcase.py` passes before adding another style preset.
- [ ] `scripts/validate_glass_benchmark.py` passes for the 15-slide narrative benchmark before expanding style presets.
- [ ] `docs/learning/README.md` and relevant learning notes were checked before modifying known problem areas.
- [ ] `schemas/*.json` are valid JSON.
- [ ] `examples/minimal-deck.ir.json` passes `scripts/validate_skill.py`.
- [ ] No document promises arbitrary HTML → perfectly editable PPTX.
- [ ] No document promises arbitrary PPTX → perfect reusable template conversion without staged clone fidelity testing and explicit fallback policy.
