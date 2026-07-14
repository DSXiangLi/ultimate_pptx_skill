# PPTX Cloner / Template Abstraction Reverse Compiler

## Purpose

Use this sub-skill when the user provides one or more `.pptx` files and wants to learn from the deck's **core visual effect**, extract a reusable visual/layout/component system, or improve `ultimate-pptx-builder` by learning from high-quality real PowerPoint templates.

The product goal is **not** to reproduce or copy the original PPTX as the user-facing deliverable. The source deck is evidence. The deliverable is a reusable, editable template system that lets the user build **new PPTX decks with new content** while preserving the source deck's recognizable visual DNA, layout grammar, component vocabulary, information hierarchy, and PPTX material behavior.

The cloner is a reverse compiler:

```text
existing PPTX specimen
→ OOXML/theme/master/layout/object inventory
→ decompiled Slide IR
→ 1:1 rebuild fidelity loop
→ layout/component archetype mining
→ visual DNA extraction
→ component contract extraction
→ generalized editable generator
→ benchmark/gate/learning promotion
```

A 1:1 rebuild is a **diagnostic fidelity test**, not the end product. Direct duplication is easier if the user only wants a copy. The real product is a reusable, editable PPTX generator/template family that preserves the specimen's visual language with new content.

## Non-Negotiables

1. **Do not promise arbitrary PPTX → perfect reusable template.** Promise staged extraction of the core visual system, with explicit fidelity/editability budgets and documented fallbacks.
2. **Separate visual fidelity from reusable abstraction.** The rebuild can be near 1:1 while the reusable generator intentionally abstracts photos, icons, or brand-specific assets.
3. **Extract evidence before naming semantics.** Do not call something a `risk-rail`, `fund-comparison-card`, or `roadmap-node` until object geometry, text, style, and repeated placement support that interpretation.
4. **Keep critical text native.** Title/body/data/source/risk text must remain editable unless the user explicitly accepts an image-only artifact.
5. **Do not promote one-off decoration.** A motif becomes skill DNA only if it affects layout rhythm, component grammar, information hierarchy, chart/table treatment, or source/risk/footer treatment.
6. **Preserve provenance.** Keep source URL, license, SHA256, original filename, and embedded-media caveats with every specimen.
7. **Checkpoint before each semantic change set.** The user expects rollback points before modifying the skill, visual systems, runtime contracts, or gates.
8. **Never optimize for source duplication over future usability.** If a decorative source feature blocks robust new-content generation, classify it as optional/fallback material rather than forcing brittle imitation.

## Inputs

Accept:

```text
single deck: path/to/reference.pptx
collection:  samples/<collection>/*.pptx
library:     research/pptx-template-library/files/<template-id>.pptx
notes:       purpose, required pages, must-remain-editable fields, must-match pages
```

Prefer same-family collections when extracting reusable systems. A mixed template pile is useful for inspiration but weak evidence for a generator.

## Output Pack

For each specimen, create or update:

```text
specimens/<deck_id>/
  original.pptx
  provenance.json
  unpacked/
  rendered/slide-01.png
  rendered/contact-sheet.png
  extracted-text.md
  object-inventory.json
  theme-inventory.json
  master-layout-inventory.json
  asset-inventory.json
  decompiled.raw.ir.json
  rebuilt.pptx                 # internal fidelity/diagnostic artifact, not final product
  rebuilt-rendered/
  rebuild-fidelity-report.json
  clone-notes.md
```

For each promoted template system:

```text
templates/<template_id>/
  template.schema.json
  style_program.json
  visual-dna-program.json
  layout_archetypes.json
  component_archetypes.json
  component-contracts/*.contract.json
  layout-constraints.json
  generator.py
  validation.md
```

## Workflow

### Acceptance Loop Principle — Fail → Diagnose → Optimize → Re-run

Cloner work must run as an acceptance loop, not a one-pass analysis. Every phase emits a machine-readable report with:

```yaml
release_decision: pass | fail
blocking_count: integer
gates: list of gate results
optimization_queue: concrete failures mapped to owner/action
next_phase_allowed: boolean
next_phase: named phase if allowed
```

If `release_decision != pass`, do not advance to the next semantic phase. Fix the highest-leverage blocker, rerun the same command, and repeat until the gate passes or the loop declares the failure stalled because the same blockers repeat without an engineering change.

Executable C1/C2 loop:

```bash
python3 scripts/run_pptx_cloner_loop.py \
  research/pptx-template-library/files/<template-id>.pptx \
  --deck-id <template-id> \
  --out specimens/<template-id> \
  --require-render \
  --max-iterations 3
```

For unit tests or environments without LibreOffice rendering, use `--skip-render`; do not use skipped renders as evidence for visual/template abstraction quality.

Current C1/C2 passing condition:

- specimen evidence pack exists;
- source slide XML unpacks and is traceable;
- full-size renders/contact sheet exist when required;
- raw IR exists;
- slide recall is 100%;
- object recall is 100%;
- source text recall is 100%;
- every IR object carries source/editability/render-policy fields;
- text-bearing objects are native/editable priority >= 4.

Loop output:

```text
specimens/<template-id>/cloner-loop-report.json
```

Use the `optimization_queue` in that report as the next implementation backlog. Do not replace it with vague prose such as “improve fidelity”; every item must name the failed gate, owner, concrete action, and evidence.

Future phases must plug into the same loop contract:

| Phase | Loop gate | Blocking failure example | Optimization response |
|---|---|---|---|
| C3 diagnostic rebuild | source IR → rebuilt PPTX → strict package/text/object/render report | rebuilt package fails strict Office gate | fix exporter/package relationships, rerun C3 |
| C4 archetype mining | repeated layout/component evidence report | claimed component appears on only one slide | demote to specimen note or compare more slides |
| C5 visual DNA | DNA claim → object evidence → PPTX translation rule | palette/background changes but card/chart grammar unchanged | extract deeper grammar or reject promotion |
| C6 component contracts | contract schema + slot/regression examples | slot overlap or unsupported density | tighten contract/validator and rerun examples |
| C7 generator | new-content deck through forward QA | source family not recognizable or critical text rasterized | update generator/style program/contracts and rerun |
| C8 learning promotion | tests/schemas/gates/docs updated | discovery only exists in notes | convert learning to executable gate or contract |

This loop is intentionally stricter than “looks close.” SOTA cloner quality comes from repeated gate failures being converted into compiler improvements, not from manually polishing one template.

### Phase C0 — Select Specimens Intentionally

Before implementation, choose a small batch with distinct grammar families. For the current curated library, use `references/pptx-template-research-library.md` and start with:

1. `dark-minimalist-business`
2. `it-software-sales-proposal-slides`
3. `data-privacy-training-gradient`
4. `digital-transformation-journey-infographic`
5. `data-strategy-roadmap-infographic`
6. `difference-between-saving-and-investment-slides`
7. `dark-modern-tech-startup-brand`
8. `business-scorecard-infographic` after abstracting photo residue

Do not clone all 19 templates at once. First establish the decompiler/rebuild loop on 2–3 representative templates, then expand.

### Phase C1 — Specimen Analyzer

Goal: produce a complete evidence pack without changing the source deck.

Extract:

- slide size and count;
- theme colors and theme fonts;
- masters, layouts, placeholders;
- shape/text/image/chart/table inventory;
- object coordinates, z-order, fills, strokes, shadows, transparency, text styles;
- embedded assets and relationship targets;
- rendered PNGs;
- extracted text.

Acceptance:

- every slide renders;
- package unpacks cleanly;
- text extraction exists;
- inventory references raw XML paths and shape IDs;
- provenance is recorded;
- no private metadata is copied into durable learning docs.

### Phase C2 — OOXML → Raw Slide IR

Convert native PowerPoint objects into the skill's Slide IR. Preserve source references so every IR object can be traced back.

Minimum raw object fields:

```yaml
id: stable clone object id
type: text | shape | image | chart | table | group | vectorIsland | rasterIsland
role_guess: conservative semantic role
box: {x, y, w, h}
z: object order
text: extracted text if any
style: fill/stroke/shadow/effect summary
font: family/size/weight/color/paragraph rules
image_ref: media relationship if any
chart_ref: chart XML relationship if any
group_id: source group if any
source_xml_path: ppt/slides/slideN.xml
source_shape_id: original cNvPr id/name
editability: guessed priority
render_policy: native | vector | raster | hybrid
```

Acceptance targets:

- slide count recall = 100%;
- critical text recall = 100%;
- shape/text/image inventory recall ≥ 95% for normal editable decks;
- coordinates and z-order are within defined tolerance;
- unsupported effects are classified, not silently dropped.

### Phase C3 — 1:1 Rebuild Fidelity Gate

Rebuild the source deck from decompiled IR, render original and rebuilt, then compare.

This phase exists to prove the extractor/compiler understands PPTX mechanics. Passing C3 does **not** mean the template system is done; it only authorizes C4–C7 abstraction work. Do not ship `rebuilt.pptx` as the final cloner output unless the user explicitly asked for a copy.

```text
original.pptx → decompiled.raw.ir.json → rebuilt.pptx
original render + rebuilt render → visual diff + text recall + editability audit
```

Current executable baseline:

```bash
python3 scripts/run_pptx_cloner_loop.py \
  research/pptx-template-library/files/<template-id>.pptx \
  --deck-id <template-id> \
  --out specimens/<template-id> \
  --require-render \
  --max-iterations 3
```

The loop runs `scripts/rebuild_decompiled_ir_pptx.py` after C1/C2 pass and writes:

```text
specimens/<template-id>/rebuilt.pptx
specimens/<template-id>/rebuild-report.json
specimens/<template-id>/rebuilt-rendered/slide-*.png
specimens/<template-id>/rebuild-visual-fidelity-report.json
```

First C3 baseline blocking criteria:

- rebuilt PPTX exists;
- rebuilt PPTX passes `scripts/check_pptx_package.py`;
- rebuilt slide count equals source slide count;
- rebuilt native text recall is 100%;
- rebuilt PPTX renders when `--require-render` is used;
- source-vs-rebuilt visual diff report is produced.

Current C3 baseline non-blocking but required evidence:

- `rebuild-report.json` classifies unsupported groups/charts/tables/background/material classes instead of silently dropping them;
- C3.1 image objects with source media relationships are reconstructed as native PPTX picture objects;
- C3.2 solid slide-level backgrounds from `p:cSld/p:bg/p:bgPr` are reconstructed as native PPTX slide backgrounds;
- C3.3 picture-fill shapes encoded as `<p:sp>` with `<a:blip>` are reconstructed as native PPTX picture material;
- C3.4 group recursion emits group children with `group_id` traceability and records child-bearing containers as structural `expanded-group-container` entries instead of opaque placeholders;
- visual fidelity score is recorded but not yet threshold-blocking, because remaining gaps still include empty text containers, tables/charts, crop/mask/effects, and advanced shape styling.

Acceptance targets for normal editable decks:

- current baseline: strict package pass, slide recall = 100%, critical text recall = 100%, render baseline exists, image relationships and solid slide backgrounds are reconstructed, and every unsupported object class is classified;
- mature clone mode: visual fidelity ≥ 97, or every miss is classified and accepted as a deliberate fallback;
- critical text recall = 100%;
- editability score ≥ 95%;
- theme/master/layout/package relationship checks pass;
- rendered perceptual QA reports no blocking drift.

Treat failure as decompiler/compiler evidence, not as a reason to hand-wave. If the rebuild cannot match because of unsupported effects, add explicit degradation rules.

### Phase C4 — Template Archetype Mining

Only after C1–C3 work reliably, mine repeatable patterns:

- cover and section page structures;
- dashboard/scorecard structures;
- chart-heavy layouts;
- table/comparison pages;
- metric card groups;
- roadmap/timeline/process pages;
- source/risk/footer/page-number systems;
- typography scale and spacing rhythm;
- repeated component geometry.

Cluster by page role and component role. Keep evidence counts and sample slide references. Do not overfit to a single cover.

### Phase C5 — Visual DNA Extraction

Extract the full DNA layers required by `references/visual-dna-model.md`:

- palette logic and semantic chart mapping;
- typography/numeral voice;
- surface/material/texture policy;
- light physics;
- layout archetypes;
- container grammar;
- component grammar;
- chart/table grammar;
- motif/ornament system;
- reading-flow metaphor;
- density rhythm;
- PPTX material translation.

For each DNA claim, include object evidence:

```text
claim → specimen slides → source object IDs/XML paths → extracted values → PPTX translation rule
```

### Phase C6 — Component Contract Extraction

Promote repeated components into Component Contract DSL only when supported by evidence.

Likely extractable contracts:

- title block / section header;
- metric card group;
- KPI scorecard grid;
- chart panel;
- comparison table;
- source/risk rail;
- footnote/footer band;
- process/timeline/roadmap;
- matrix;
- dashboard card grid.

Every contract must include slot geometry, spacing policy, semantic overlap rules, density limits, native/editable requirements, and at least one regression example.

### Phase C7 — Generalized Template Generator

Build a generator that accepts new content and keeps the cloned visual language recognizable.

The generator is the actual user-facing cloner product. It should expose content slots, page-role choices, component variants, density modes, and fallbacks so users can create new decks, not merely re-render the old one.

Acceptance:

- original-content rebuild remains high fidelity;
- new-content generated deck keeps the same visual DNA;
- critical title/body/data/source/risk/chart/table content remains editable;
- generated deck passes current gates or template-specific equivalents;
- visual reviewer can recognize the source family without seeing the original.

### Phase C8 — Learn Back Into the Skill

After a clone succeeds, promote durable findings into the forward compiler:

- update `style_program` or add a new visual system only if it has deep DNA;
- add component contracts and validators for learned component classes;
- extend benchmark corpus for new scenario × density × style coverage;
- add learning notes for root causes and prevention rules;
- add tests for extracted contracts/gates;
- document fallback rules for Office-incompatible effects.

Do not leave discoveries only in prose. If a repeated PPTX pattern matters, convert it into schema, script, component contract, benchmark case, or QA gate.

## Template-Specific Clone Strategy

### Dark executive systems

Use for `dark-minimalist-business`, `software-company-consulting`, and related dark templates.

Extract:

- deep neutral palette and contrast ladder;
- title-scale rhythm;
- minimal page-role skeletons;
- gradient/vignette/light model;
- section divider grammar;
- low-noise executive spacing.

Risk: shallow black-background clones. Block promotion unless typography, layout skeleton, chart grammar, and footer/page-number treatment are system-specific.

### Enterprise proposal systems

Use for `it-software-sales-proposal-slides`.

Extract:

- proposal narrative topology;
- value proposition cards;
- problem/solution/comparison rhythm;
- CTA/closing pages;
- geometric gradient motif;
- enterprise-safe source/footnote handling.

Risk: SaaS marketing language leaking into finance decks. Abstract the structure, not the business wording.

### Risk/compliance tech systems

Use for `data-privacy-training-gradient` and AI/risk-adjacent templates.

Extract:

- compliance/training page roles;
- security motif and circuit/line grammar;
- risk/source visibility;
- explainer density modes;
- warning/caution components.

Risk: decorative cyber background overpowering compliance text. Critical risk/source text must stay native and readable.

### Roadmap / journey systems

Use for `digital-transformation-journey-infographic` and `data-strategy-roadmap-infographic`.

Extract:

- path geometry;
- milestone nodes;
- stage labels;
- sequence arrows/connector grammar;
- icon/card role mapping;
- compression strategy for 3/5/7 stages.

Risk: infographics that look good only for exact item counts. Generator must declare supported counts and fallback layouts.

### Finance explainer systems

Use for `difference-between-saving-and-investment-slides`.

Extract:

- comparison grammar;
- definition/example/risk page roles;
- concept cards;
- finance-safe illustration abstraction;
- source/risk/footer requirements.

Risk: cute illustration style weakening institutional tone. Keep the information structure; abstract illustration into optional vector/shape motifs.

### KPI / scorecard systems

Use for `business-scorecard-infographic`.

Extract:

- dashboard grid;
- metric hierarchy;
- progress/meter components;
- label/value/annotation typography;
- high-density safe zones.

Risk: building/photo residue and tiny labels. Replace photography with abstract surface if not core; enforce CJK-aware text capacity.

## QA Gates for Cloner Work

Run the existing forward-compiler gates plus clone-specific gates:

1. **Package/OOXML audit** — masters, layouts, themes, relationships, media, charts.
2. **Text recall** — original vs decompiled vs rebuilt critical text.
3. **Object inventory recall** — expected vs rebuilt object classes and counts.
4. **Visual fidelity** — original render vs rebuilt render, full-size not just thumbnails.
5. **Editability audit** — business-critical text/chart/table native or editable-vector.
6. **Visual DNA realization** — new-content generator materializes DNA beyond palette/background.
7. **Layout/text safety** — CJK-safe spacing, no overlaps, source/risk/footer readable.
8. **Practicality** — file size, Office/WPS rendering, font fallback, attribution/license notes.

## Template Abstraction Report Template

Every cloner iteration should end with:

```markdown
# Template Abstraction Report: <template/deck id>

## Source
- file:
- source URL/license:
- SHA256:
- slide count:

## Goal
- intended new-deck use cases:
- diagnostic rebuild pages:
- abstractable page roles:
- critical editable fields:

## Fidelity Result
- purpose: internal diagnostic, not final deliverable
- visual fidelity:
- text recall:
- object recall:
- editability:
- known unsupported effects:

## Extracted DNA
- palette:
- typography:
- layout archetypes:
- component grammar:
- chart/table grammar:
- footer/source/risk grammar:

## Promotion Decisions
- promote to style program:
- promote to component contracts:
- add benchmark/gate:
- learning note:

## Next Iteration
- fixes:
- tests:
- templates to compare next:
```

## Implementation Order

For the current skill, implement in this order:

1. Build/validate C1 specimen analyzer on two P0 templates: `dark-minimalist-business` and `it-software-sales-proposal-slides`.
2. Add C2 raw IR decompiler for text/shape/image first; charts/tables can be classified before full native reconstruction.
3. Add C3 rebuild fidelity gate and visual diff reports. C3 baseline is implemented as strict package/text/render validation with unsupported object classification.
4. Continue C3 optimization: C3.1 image relationship reconstruction, C3.2 solid slide background reconstruction, C3.3 picture-fill shape reconstruction, and C3.4 group recursion are implemented; next reduce empty text placeholders, shape styling gaps, chart, and table placeholders before making visual score threshold-blocking.
5. Only then start C4–C6 mining on the first 4–6 selected templates, with C3 unsupported/visual-score evidence attached to every promoted claim.
6. Promote one template family end-to-end before expanding to many families.
7. For each promotion, add benchmark evidence and update skill gates so the learning improves future generation.

This avoids the trap of collecting many pretty templates without proving that the system can understand and regenerate them.
