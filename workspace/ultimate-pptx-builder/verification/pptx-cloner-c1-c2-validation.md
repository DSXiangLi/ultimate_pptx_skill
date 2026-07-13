# PPTX Cloner C1/C2 Implementation Validation

Date: 2026-07-13

## Scope

Started implementing the PPTX Cloner / Reverse Compiler path from `references/pptx-cloner.md`.

Implemented the first practical slice:

```text
C1 specimen analyzer
→ C2 raw IR decompiler
→ evidence packs for two P0 templates
```

This does **not** yet implement C3 1:1 rebuild fidelity. The current output is enough to inspect source package/object evidence and plan the rebuild/export bridge.

## Implemented Files

- `scripts/analyze_pptx_specimen.py`
  - Copies source PPTX into a specimen workspace.
  - Unpacks OOXML package.
  - Extracts text into Markdown.
  - Builds object inventory with object type, z-order, bbox, text, style/font hints, source XML path, source shape id/name.
  - Builds theme inventory.
  - Builds master/layout inventory.
  - Builds asset inventory for media and charts.
  - Records provenance including source URL/license note/SHA256/slide count/object count.
  - Renders slides through existing LibreOffice/pdftoppm renderer when not skipped.
  - Creates `rendered/contact-sheet.png` from rendered slide images.

- `scripts/decompile_pptx_to_ir.py`
  - Converts PPTX object inventory into conservative raw Slide IR.
  - Preserves source XML and shape IDs.
  - Marks text-bearing objects as `render_policy: native` and editability priority 5.
  - Keeps non-text image objects as raster and groups as hybrid.
  - Does not infer high-level semantics yet; `role_guess` remains conservative.

- `tests/test_pptx_specimen_analyzer.py`
  - Covers evidence pack generation and contact sheet creation.

- `tests/test_pptx_to_ir_decompiler.py`
  - Covers slide count, text recall, object classes, source references, editability, and render policy.

## Test Results

```bash
python3 -m unittest tests.test_pptx_specimen_analyzer tests.test_pptx_to_ir_decompiler -v
```

Result:

```text
Ran 3 tests in 0.982s
OK
```

## Real Template Evidence Packs

Generated specimens for the first two P0 templates:

### `dark-minimalist-business`

Source:

```text
research/pptx-template-library/files/dark-minimalist-business.pptx
```

Output:

```text
specimens/dark-minimalist-business/
  original.pptx
  provenance.json
  unpacked/
  rendered/slide-*.png
  rendered/contact-sheet.png
  extracted-text.md
  object-inventory.json
  theme-inventory.json
  master-layout-inventory.json
  asset-inventory.json
  decompiled.raw.ir.json
```

Summary:

```json
{
  "slides": 21,
  "objects": 165,
  "rendered": 21,
  "themes": 2,
  "masters": 1,
  "layouts": 4,
  "media": 58,
  "text_objects": 126
}
```

Visual contact sheet review: rendered normally; no blank slides, obvious missing images, or乱码. Overall style matches dark minimalist business.

### `it-software-sales-proposal-slides`

Source:

```text
research/pptx-template-library/files/it-software-sales-proposal-slides.pptx
```

Output:

```text
specimens/it-software-sales-proposal-slides/
  original.pptx
  provenance.json
  unpacked/
  rendered/slide-*.png
  rendered/contact-sheet.png
  extracted-text.md
  object-inventory.json
  theme-inventory.json
  master-layout-inventory.json
  asset-inventory.json
  decompiled.raw.ir.json
```

Summary:

```json
{
  "slides": 14,
  "objects": 175,
  "rendered": 14,
  "themes": 2,
  "masters": 1,
  "layouts": 11,
  "media": 23,
  "text_objects": 83
}
```

Visual contact sheet review: rendered normally; no blank slides, obvious missing images, or乱码. Overall style matches dark gradient enterprise proposal.

## Important Finding: External Specimen Package Strictness

The two downloaded source templates open/render successfully, but the existing strict package gate fails them:

```bash
python3 scripts/check_pptx_package.py \
  research/pptx-template-library/files/dark-minimalist-business.pptx \
  research/pptx-template-library/files/it-software-sales-proposal-slides.pptx
```

Result:

```text
FAIL pptx package
- dark-minimalist-business.pptx: missing required Office part: docProps/app.xml
- dark-minimalist-business.pptx: missing required Office part: docProps/core.xml
- dark-minimalist-business.pptx: missing required Office part: ppt/tableStyles.xml
- it-software-sales-proposal-slides.pptx: missing required Office part: docProps/app.xml
- it-software-sales-proposal-slides.pptx: missing required Office part: docProps/core.xml
```

Interpretation:

- External specimens may be useful and renderable even when they do not satisfy this project's stricter generated-output package gate.
- Do not block C1/C2 specimen analysis on strict package compliance.
- C3 rebuilt/generated outputs **must** pass strict package compliance, because they are products of this skill.
- Future cloner reports should distinguish:
  - `source_openable/renderable`
  - `source_strict_package_pass`
  - `rebuilt_strict_package_pass`

## C3 Implementation Cut Recommended Next

Do not try to rebuild every OOXML feature at once. The next C3 slice should be:

1. Add `scripts/rebuild_decompiled_ir_pptx.py` using `python-pptx` / existing `export_ir_pptx.py` materialization patterns.
2. Support first-pass native rebuild for:
   - text boxes with text/font/color/box/z approximation;
   - simple shapes with fill/stroke/box;
   - raster images only when `image_ref` can be resolved from `asset-inventory` / OOXML relationships;
   - groups as flattened child placeholders or classified unsupported, not silently ignored.
3. Add `scripts/check_rebuild_fidelity.py` that compares:
   - slide count;
   - critical text recall;
   - object class/count recall;
   - rendered original vs rebuilt image availability;
   - strict package check for rebuilt output.
4. First target should not be 97 visual fidelity. First target should be an honest baseline report:
   - slide count recall = 100%;
   - critical text recall = 100%;
   - rebuilt package strict pass;
   - known unsupported objects classified.
5. Only after this baseline should visual fidelity scoring become blocking.

## Next Template Expansion Rule

Do not add more templates until C3 baseline works for at least:

- `dark-minimalist-business`
- `it-software-sales-proposal-slides`

Reason: if these two cannot rebuild into a strict, text-complete PPTX, mining additional template families will create attractive but unactionable prose.
