# Architecture: IR-first Editable PPTX System

## Thesis

The fundamental mistake in most HTML-to-PPTX systems is treating arbitrary DOM as the source of truth. HTML and PPTX are not isomorphic. A browser document is a flow/layout/rendering tree; a PPTX slide is an object graph of shapes, text frames, pictures, charts, tables, groups, themes, and effects.

The architecture here is therefore:

```text
content.yaml / user brief
  → content contract
  → narrative topology
  → style program
  → slide-ir.json
  → HTML preview renderer
  → PPTX renderer
  → QA loop
```

## Source of Truth

`Slide IR` is the only source of truth. HTML preview and PPTX export are derived artifacts.

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
