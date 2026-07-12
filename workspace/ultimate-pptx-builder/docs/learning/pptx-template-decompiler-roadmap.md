# PPTX Template Decompiler / Clone-PPTX Roadmap

Date: 2026-07-10

## Context

The current `ultimate-pptx-builder` has evolved into a finance-grade PPTX visual compiler:

```text
Narrative Contract
→ Visual DNA Program
→ Component Contract DSL
→ Authored Layout Graph
→ IR Compiler
→ Editable PPTX Materialization
→ OOXML Audit
→ Rendered Perceptual QA
→ Visual DNA Realization Gate
→ Finance Benchmark Corpus
```

The next high-leverage evolution path is not only to generate decks from scratch, but to learn from existing high-quality PPTX decks:

```text
Existing excellent PPTX samples
→ decompile structure and style
→ rebuild 1:1 as a fidelity test
→ abstract reusable templates / visual DNA / layout grammar
→ feed those patterns back into the forward compiler
```

This is the **PPTX Template Decompiler** or **Clone-PPTX** direction.

## Core Thesis

The best PPTX skill should not rely only on hand-designed styles or HTML-like imagination. It should learn directly from real PPTX decks that already work in finance/Office workflows.

The loop should be:

```text
Real PPTX specimen
→ raw OOXML/theme/master/layout/object inventory
→ decompiled Slide IR
→ 1:1 rebuild fidelity loop
→ template archetype mining
→ visual DNA extraction
→ component contract extraction
→ generalized template generator
→ benchmark case / gate / learning note
```

This makes skill evolution grounded in real PowerPoint capabilities:

- which effects are native PowerPoint shapes/text/charts/tables;
- which effects require vector approximations;
- which effects should be raster fallback;
- how professional decks actually handle source/risk/footer, charts, tables, typography, spacing, and hierarchy.

## Important Distinction

### 1:1 Clone

A 1:1 clone is not the end goal. Directly copying the original PPTX is always simpler if only duplication is needed.

Its purpose is to test whether the decompiler/template abstraction is faithful:

```text
original.pptx
→ decompiled IR
→ rebuilt.pptx
→ render original/rebuilt
→ visual diff + text recall + editability audit
```

If the rebuilt PPTX is far from the original, the abstraction is not good enough.

### Reusable Template

The real goal is reusable template grammar:

```text
same design system + new content
→ generated editable PPTX
→ same visual language, layout rhythm, component grammar, and compliance treatment
```

Therefore every cloned deck should be promoted into reusable assets where possible:

- style tokens;
- visual DNA program;
- layout archetypes;
- component archetypes;
- component contracts;
- constraint layout rules;
- benchmark cases.

## Recommended Sample Input

Best input is not a random pile of unrelated PPTX files. The strongest results come from same-family decks:

```text
samples/<collection_name>/
  deck_01.pptx
  deck_02.pptx
  deck_03.pptx
  ...
```

Preferably 5–20 decks from:

- same institution;
- same presentation purpose;
- same or adjacent visual system;
- similar finance/business context.

Useful user notes:

```text
collection purpose: fund roadshow / investment research / weekly report / product explainer
most important pages: cover, fund comparison, allocation, chart-heavy, risk page
must be 1:1: yes/no per page
must remain editable: title/body/data/source/risk/chart/table
```

## Phase K1 — PPTX Specimen Analyzer

### Goal

Ingest one or more PPTX specimens and produce a complete analysis pack.

### Inputs

```text
samples/<collection>/*.pptx
```

### Outputs

```text
specimens/<deck_id>/
  original.pptx
  unpacked/
  rendered/slide-01.png
  rendered/slide-02.png
  extracted-text.md
  object-inventory.json
  theme-inventory.json
  master-layout-inventory.json
  asset-inventory.json
```

### Extract

- slide size;
- slide count;
- theme colors;
- theme fonts;
- masters and layouts;
- placeholders;
- shape/text/image/chart/table inventory;
- object z-order;
- raw XML references;
- rendered PNGs;
- extracted text.

### Candidate Files

```text
scripts/analyze_pptx_specimen.py
scripts/unpack_pptx_ooxml.py
scripts/render_pptx_specimen.py
schemas/pptx-specimen.schema.json
tests/test_pptx_specimen_analyzer.py
references/pptx-template-decompiler.md
```

### Acceptance

```bash
python3 -m unittest tests/test_pptx_specimen_analyzer.py -v
python3 scripts/analyze_pptx_specimen.py samples/foo.pptx --out specimens/foo
```

Required:

- all slides rendered;
- PPTX package unpacked;
- object inventory exists;
- theme/master/layout inventory exists;
- extracted text exists;
- no credential/private metadata is copied into durable learning docs.

### Commit

```text
ultimate-pptx phase K1 pptx specimen analyzer
```

## Phase K2 — PPTX OOXML → Raw IR Decompiler

### Goal

Convert PPTX native objects into the skill's Slide IR.

### Raw IR Object Fields

Each object should carry:

```text
id
type
role_guess
box
z
text
style
fill
stroke
font
paragraph
image_ref
chart_ref
table_ref
group_id
source_xml_path
source_shape_id
editability guess
render_policy guess
```

### Candidate Files

```text
scripts/decompile_pptx_to_ir.py
schemas/decompiled-slide-ir.schema.json
tests/test_pptx_to_ir_decompiler.py
references/pptx-to-ir-decompiler.md
```

### Acceptance

```bash
python3 -m unittest tests/test_pptx_to_ir_decompiler.py -v
python3 scripts/decompile_pptx_to_ir.py specimens/foo/original.pptx --out specimens/foo/decompiled.ir.json
```

Targets:

```text
slide count recall = 100%
critical text recall = 100%
shape/text/image inventory recall >= 95%
z-order preserved for normal shapes/text/images
coordinates within tolerance
```

### Commit

```text
ultimate-pptx phase K2 pptx to IR decompiler
```

## Phase K3 — 1:1 Rebuild Fidelity Gate

### Goal

Prove that the decompiled IR can rebuild the source deck with high visual fidelity.

### Loop

```text
original.pptx
→ decompiled.ir.json
→ rebuilt.pptx
→ render original and rebuilt
→ visual diff
→ text recall + OOXML audit + editability audit
```

### Candidate Files

```text
scripts/rebuild_decompiled_ir_pptx.py
scripts/check_rebuild_fidelity.py
tests/test_pptx_rebuild_fidelity.py
references/rebuild-fidelity-gate.md
```

### Acceptance

```bash
python3 -m unittest tests/test_pptx_rebuild_fidelity.py -v
python3 scripts/check_rebuild_fidelity.py specimens/foo/original.pptx specimens/foo/rebuilt.pptx --report specimens/foo/rebuild-fidelity-report.json
```

Targets:

```text
visual fidelity >= 97 for normal editable decks
critical text recall = 100%
editability score >= 95%
OOXML visual property audit passes
rendered perceptual QA passes
```

### Commit

```text
ultimate-pptx phase K3 rebuild fidelity
```

## Phase K4 — Template Archetype Miner

### Goal

From multiple slides/decks, extract repeated page and component patterns.

### Mine

- cover page archetypes;
- summary/dashboard archetypes;
- chart-heavy archetypes;
- table/comparison archetypes;
- metric card archetypes;
- source/risk/footer archetypes;
- title/header systems;
- spacing tokens;
- typography scale;
- repeated component geometry.

### Candidate Outputs

```text
layout_archetypes.json
component_archetypes.json
style_tokens.json
spacing_tokens.json
semantic_slots.json
```

### Candidate Files

```text
scripts/mine_template_archetypes.py
schemas/template-archetype.schema.json
schemas/component-archetype.schema.json
tests/test_template_archetype_miner.py
references/template-archetype-mining.md
```

### Acceptance

```bash
python3 -m unittest tests/test_template_archetype_miner.py -v
python3 scripts/mine_template_archetypes.py specimens/<collection> --out templates/<collection>/archetypes
```

Required:

- repeated layouts are clustered;
- semantic slots are inferred conservatively;
- source/risk/footer slots are identified;
- component archetypes include coordinate and style evidence;
- no overclaiming when evidence is weak.

### Commit

```text
ultimate-pptx phase K4 template archetype miner
```

## Phase K5 — Visual DNA Extraction from PPTX Samples

### Goal

Extract a visual DNA program from real decks.

### Extract

```text
palette
font system
grid rhythm
container shapes
corner radius
stroke style
shadow/elevation
chart grammar
table grammar
number typography
source/risk/footer grammar
icon style
spacing rhythm
```

### Output

```text
templates/<collection>/visual-dna-program.json
```

### Candidate Files

```text
scripts/extract_visual_dna_from_pptx.py
schemas/visual-dna-program.schema.json
tests/test_pptx_visual_dna_extraction.py
references/pptx-visual-dna-extraction.md
```

### Acceptance

```bash
python3 -m unittest tests/test_pptx_visual_dna_extraction.py -v
python3 scripts/extract_visual_dna_from_pptx.py specimens/<collection> --out templates/<collection>/visual-dna-program.json
```

Required:

- token extraction is backed by object evidence;
- chart/table/container grammar is included;
- output passes `check_visual_dna_realization.py` once applied to generated decks.

### Commit

```text
ultimate-pptx phase K5 pptx visual DNA extraction
```

## Phase K6 — Component Contract Extraction

### Goal

Promote repeated components into `Component Contract DSL` rules.

### Extractable Components

- title block;
- metric card group;
- chart panel;
- table block;
- source/risk rail;
- footnote/footer band;
- timeline;
- process flow;
- matrix;
- route map;
- dashboard card grid.

### Outputs

```text
templates/<collection>/component-contracts/*.contract.json
templates/<collection>/layout-constraints.json
```

### Candidate Files

```text
scripts/extract_component_contracts_from_pptx.py
scripts/promote_archetype_to_component_contract.py
tests/test_component_contract_extraction.py
references/pptx-component-contract-extraction.md
```

### Acceptance

```bash
python3 -m unittest tests/test_component_contract_extraction.py -v
python3 scripts/extract_component_contracts_from_pptx.py templates/<collection>/archetypes --out templates/<collection>/component-contracts
```

Required:

- contracts include slot evidence;
- contracts avoid overfitting to a single page;
- constraints are justified by repeated examples;
- extracted contracts can run through `check_component_contracts.py`.

### Commit

```text
ultimate-pptx phase K6 component contract extraction
```

## Phase K7 — Generalized Template Generator Synthesizer

### Goal

Turn decompiled/archetyped templates into generators that accept new content.

### Output Template Package

```text
templates/<template_id>/
  template.schema.json
  style_program.json
  visual-dna-program.json
  layout_archetypes.json
  component_contracts/
  generator.py
  validation.md
```

### Acceptance

```bash
python3 -m unittest tests/test_template_generator_synthesis.py -v
python3 scripts/synthesize_template_generator.py templates/<collection> --out templates/<template_id>
python3 scripts/validate_generated_template.py templates/<template_id>
```

Required:

- original content rebuild remains high fidelity;
- new content keeps style and component grammar;
- title/body/source/risk remain editable;
- generated decks pass current visual-system gates or a template-specific equivalent.

### Commit

```text
ultimate-pptx phase K7 template generator synthesis
```

## Phase K8 — Template Learning-to-Gate

### Goal

Convert learned PPTX patterns into durable compiler improvements.

### Promotion Targets

```text
visual_dna_program
style_program
component_contracts
layout_constraints
benchmark_cases
learning notes
unit tests
```

### Candidate Files

```text
scripts/promote_template_to_visual_system.py
scripts/check_template_learning_quality.py
tests/test_template_learning_to_gate.py
references/template-learning-to-gate.md
```

### Acceptance

```bash
python3 -m unittest tests/test_template_learning_to_gate.py -v
python3 scripts/check_template_learning_quality.py templates/<template_id>
python3 scripts/validate_skill.py
```

Required:

- every promoted rule has evidence from specimens;
- every promoted component has at least one regression test;
- benchmark corpus is extended when the template covers a new scenario/density/style;
- installed skill is synced and validated.

### Commit

```text
ultimate-pptx phase K8 template learning to gate
```

## Integration with Current Skill Architecture

The skill should become a dual compiler:

```text
Forward Compiler:
  business input / content contract → IR → PPTX

Reverse Compiler:
  existing PPTX → IR/template/DNA/contracts → generator
```

Closed loop:

```text
excellent PPTX sample
→ reverse compiler
→ learned template/DNA/contracts
→ forward compiler
→ new editable PPTX
→ QA gates
→ benchmark corpus
```

## Recommended Next Execution Order

For the next conversation, start with:

```text
K1 PPTX Specimen Analyzer
K2 PPTX → Raw IR Decompiler
K3 1:1 Rebuild Fidelity Gate
```

Only after K1–K3 are reliable should we attempt generalized template mining.

Reason:

```text
If 1:1 rebuild is weak, template abstraction is not trustworthy.
```

## Design Rules for Clone-PPTX Work

1. **Do not promise arbitrary PPTX → perfect reusable template.** Start with same-family decks.
2. **Separate clone fidelity from reusable abstraction.** 1:1 clone is a test, not the product.
3. **Extract evidence before naming semantics.** Never infer `fund-comparison-card` or `risk-rail` without repeated geometry/text/style evidence.
4. **Keep critical finance text native.** Text recall and editability are more important than visual shortcuts.
5. **Record fallback explicitly.** If a shape/effect must rasterize, write source metadata and reason.
6. **Promote repeated patterns into contracts/gates.** Do not leave discoveries as prose only.
7. **Commit each phase.** Every phase should have a rollback point and validation record.

## Why This Roadmap Matters

This route lets the skill learn from real professional decks instead of inventing style from scratch. It can grow a library of finance-proven design systems while preserving the rigor already built:

- Component Contract DSL;
- authored layout graph;
- visual DNA realization;
- OOXML audit;
- rendered perceptual QA;
- finance benchmark corpus.

In short:

```text
Learn to understand excellent PPTX first;
then learn to generate excellent PPTX more reliably.
```
