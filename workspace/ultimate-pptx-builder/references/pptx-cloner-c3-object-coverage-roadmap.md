# PPTX Cloner C3 Object-Coverage Roadmap

## Context

The C3 diagnostic rebuild baseline can pass strict package/text/render gates while still producing low visual fidelity if dominant PPTX material layers are unsupported or placeholdered. This is acceptable only as an early diagnostic baseline. The next cloner iterations should turn repeated missing categories into executable reconstruction support before C4 archetype mining or C5 visual DNA promotion.

Observed baseline pattern:

- `dark-minimalist-business`: package/text/render pass, native text recall 100%, but visual score was low until images and slide backgrounds were reconstructed.
- `it-software-sales-proposal-slides`: package/text/render pass, native text recall 100%, but visual score remained low until images and slide backgrounds were reconstructed.

Treat this as a compiler coverage backlog, not as final clone quality.

## Principle

Do not make visual fidelity threshold-blocking until the loop can reconstruct the dominant visual object/material classes for the specimen family. Otherwise the gate punishes known placeholder coverage rather than isolating real layout/rendering drift.

Instead, C3 should progress in object/material-coverage increments:

```text
C3.0 package/text/render baseline
→ C3.1 image relationship reconstruction
→ C3.2 slide/background/master material reconstruction
→ C3.3 shape visual-property reconstruction
→ C3.4 group recursion / child flattening
→ C3.5 empty/decorative text container classification
→ C3.6 chart/table classification and partial native reconstruction
→ C3.mature visual fidelity threshold
```

Each increment must update the loop report with object-class/material recall, unsupported counts, visual score deltas, and blocker/optimization-queue entries.

## C3.1 — Image Relationship Reconstruction

Highest-leverage step for real templates with photo/mockup/logo/illustration-heavy slides.

Requirements:

1. Parse slide relationship files (`ppt/slides/_rels/slideN.xml.rels`) and map `rId` to `ppt/media/*` targets.
2. Preserve relationship id, media target/package path, content type/ext, sha, source shape id/name, box coordinates, and crop metadata if available.
3. In C3 rebuild, call native PPTX image insertion using the extracted media file and original box.
4. If crop/mask support is not implemented, record it as a named degradation rather than dropping the image.
5. Report image object recall separately from text/shape recall.

Acceptance:

- image placeholders decrease materially;
- rebuilt PPTX remains strict-package valid;
- source/rebuilt slide count and native text recall remain 100%;
- every missing image has a named cause.

## C3.2 — Slide/Background/Master Material Reconstruction

Background material is a first-class visual-DNA layer. Many templates encode dark or colored atmosphere as `p:cSld/p:bg/p:bgPr`, not as a normal shape object. If C1/C2 only inventory shapes, C3 may preserve text/images while the deck visually collapses to white.

Requirements:

1. Parse slide XML backgrounds before object-only inventory.
2. Preserve slide-level `background` in raw IR with source XML traceability.
3. Rebuild solid RGB backgrounds as native slide backgrounds.
4. Classify gradients, image backgrounds, theme references, layout/master inheritance, and unresolved backgrounds explicitly rather than defaulting to white.
5. Report background materialization separately from object materialization.
6. Compare source-vs-rebuilt visual score before/after C3.2 on at least two P0 specimens.

Acceptance:

- colored/dark slides no longer collapse to white;
- rebuilt PPTX remains strict-package valid;
- slide/text/image recall remains intact;
- every non-solid background has a named degradation cause.

## C3.3 — Shape Visual-Property Reconstruction

After images/backgrounds, restore shape styling because shallow rectangle materialization destroys visual DNA evidence.

First implemented slice: picture-fill shapes. Some image-like visuals are encoded as `<p:sp>` with `<a:blip>` rather than `<p:pic>`. These must preserve `fill_image_ref` and materialize as `native-picture-fill-shape-image` before generic shape reconstruction.

Prioritize:

- picture-fill shape media relationship recovery;
- fill color and transparency;
- line color/width/dash;
- rounded rectangle radius when representable;
- simple arrows/lines/connectors;
- shadow/glow as classified degradation if native support is limited;
- theme color resolution to RGB/alpha.

Acceptance:

- simple native shapes no longer collapse into generic grey rectangles;
- report separates geometry recall from visual-property recall;
- unsupported effects are classified with source object references.

## C3.4 — Group Recursion / Child Flattening

Groups should not remain single opaque placeholders when their children are PPTX-native objects.

Implemented first slice: C1 recursively emits group children with `group_id`, `parent_group_name`, and `group_depth`; C2 preserves those fields; C3 records group containers as `expanded-group-container` instead of drawing opaque placeholders when children are available.

Approach:

1. Recursively parse group shape trees.
2. Preserve group transform and child transforms.
3. Emit children as IR objects with `group_id` and inherited transform applied or explicitly represented.
4. Rebuild native children when possible.
5. Leave group-only effects as classified degradation.

Acceptance:

- group placeholder count drops;
- child text/images/shapes inside groups contribute to recall;
- z-order remains deterministic and traceable.

## C3.5 — Empty / Decorative Text Container Classification

After group recursion, many remaining `text` placeholders may be empty text-frame artifacts rather than missing content.

Implemented first slice: C2 classifies empty `type: text` objects as `classification.kind == "empty-text-container"`, lowers editability priority to 1, and sets `render_policy: skip`; C3 records them as `skipped-empty-text-container` and does not draw placeholders or list them as unsupported.

Acceptance:

- unsupported `text` placeholders drop to zero when all text objects are empty/decorative;
- critical text recall remains 100%;
- skipped objects preserve source shape/group traceability in `rebuild-report.json`.

## C3.6 — Chart/Table Classification and Partial Reconstruction

Charts and tables can initially stay classified before full native reconstruction, but they must not be anonymous placeholders.

Implemented first table slice: C1 extracts native PowerPoint table rows, columns, and cell text; C2 emits structured `table_ref` with `classification.kind == "native-table-candidate"`; C3 rebuilds simple native tables with `slide.shapes.add_table(...)` and records `produced: native-table`.

Minimum classification:

- chart XML relationship and chart type if available;
- table grid geometry, cell text, row/column count;
- whether business-critical data is present;
- native/editable reconstruction feasibility;
- fallback policy.

Native reconstruction should start with simple tables and common charts only after classification is reliable.

## When to Promote to C4–C7

Do not mine archetypes or promote visual DNA from a specimen while dominant object/material classes are placeholders, unless the promoted claim explicitly excludes those objects.

Allowed:

- mining typography/layout from decks where text/shape/background coverage is strong;
- mining dark executive spacing from text/shape-heavy pages;
- noting unresolved group/chart/table treatment as evidence gaps.

Not allowed:

- claiming a photo/card/component system when photos are still placeholders;
- claiming dark/gradient material grammar when slide/background material is missing;
- claiming chart/table grammar before chart/table extraction or classification exists;
- using low-fidelity placeholder rebuilds as proof of reusable visual DNA.

## Report Fields to Add or Preserve

Every C3 loop report should expose:

```json
{
  "object_class_coverage": {
    "text": {"source": 0, "rebuilt_native": 0, "recall": 0.0},
    "shape": {"source": 0, "rebuilt_native": 0, "recall": 0.0},
    "image": {"source": 0, "rebuilt_native": 0, "recall": 0.0},
    "group": {"source": 0, "expanded_children": 0, "opaque_placeholders": 0},
    "chart": {"source": 0, "classified": 0, "rebuilt_native_or_vector": 0},
    "table": {"source": 0, "classified": 0, "rebuilt_native_or_vector": 0}
  },
  "material_coverage": {
    "background": {"source": 0, "rebuilt_native": 0, "classified_degradation": 0},
    "gradient": {"source": 0, "rebuilt_native": 0, "classified_degradation": 0}
  },
  "visual_score_delta_by_increment": [],
  "unsupported_by_cause": [],
  "next_object_coverage_backlog": []
}
```

This makes fidelity improvement measurable and prevents subjective “looks better” claims from replacing compiler evidence.
