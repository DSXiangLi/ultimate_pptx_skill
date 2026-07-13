# Architecture: IR-first Editable PPTX System

## Thesis

The fundamental mistake in most HTML-to-PPTX systems is treating arbitrary DOM as the source of truth. HTML and PPTX are not isomorphic. A browser document is a flow/layout/rendering tree; a PPTX slide is an object graph of shapes, text frames, pictures, charts, tables, groups, themes, and effects.

The architecture here is therefore a dual compiler:

```text
Forward compiler:
content.yaml / user brief
  → content contract
  → narrative topology
  → style program
  → slide-ir.json
  → HTML preview renderer
  → PPTX renderer
  → QA loop

Reverse compiler / PPTX cloner:
existing.pptx
  → OOXML/theme/master/layout/object inventory
  → decompiled raw slide-ir.json
  → 1:1 rebuild fidelity loop
  → layout archetypes + visual DNA + component contracts
  → reusable generator
  → benchmark/gate/learning promotion
```

## Source of Truth

`Slide IR` is the only source of truth for generated decks. HTML preview and PPTX export are derived artifacts. In reverse-compiler work, the original PPTX is evidence and the 1:1 rebuilt deck is a fidelity test; the durable source of truth remains the decompiled/promoted IR, style program, visual DNA, component contracts, and generator.

## Renderer Responsibilities

| Layer | Responsibility | Must Not Do |
|---|---|---|
| Content Contract | facts, slots, compliance, priorities | invent data |
| Narrative Topology | semantic relationship | choose visual texture |
| Style Program | tokens, DNA, material strategy | hardcode page content |
| Slide IR | object graph | depend on arbitrary DOM |
| HTML Renderer | visual preview/layout feedback | become source of truth |
| PPTX Renderer | native/vector/raster export | silently flatten critical content |
| QA Loop | catch drift and editability failures | rubber-stamp first render |
| PPTX Specimen Analyzer | extract package/theme/master/layout/object evidence from existing decks | infer semantics before evidence |
| PPTX Cloner | test decompiled IR by rebuilding the source deck | treat direct duplication as reusable abstraction |
| Template Miner | promote repeated layouts/components/DNA into contracts and gates | promote one-off decoration or photo assets as system DNA |

## Acceptance Mechanism

A build cannot move to PPTX export unless:

1. Content contract has required fields.
2. Style program declares native/vector/raster policy.
3. Slide IR passes schema validation.
4. Critical editability priorities are declared.

A build cannot be released unless:

1. PPTX audit confirms critical content remains editable.
2. Preview-vs-PPTX visual comparison has no blocking drift.
3. Finance practicality checks pass.

A cloned template cannot be promoted into the forward compiler unless:

1. The source specimen has provenance, rendered previews, extracted text, and OOXML inventories.
2. Decompiled IR can rebuild the source with measured visual/text/editability fidelity.
3. Every promoted visual DNA or component contract cites specimen evidence.
4. New-content generation preserves the cloned system's core visual language while keeping critical text/charts/tables editable.
5. Learned patterns become tests, schemas, component contracts, benchmark cases, gates, or learning notes rather than prose-only observations.
