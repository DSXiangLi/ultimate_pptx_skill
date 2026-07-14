# PPTX Cloner C3.2 Slide Background Reconstruction

Use this reference when C3 diagnostic rebuilds preserve text/images but rendered slides collapse to white or lose the deck's dark/light theme material.

## Durable lesson

Many high-quality PPTX templates encode the most important visual atmosphere as slide-level OOXML background material, not as a normal shape object. If C1/C2 only inventory `slide.shapes`, C3 can preserve text, images, and geometry while still losing the whole visual system.

Observed source pattern:

```xml
<p:cSld>
  <p:bg>
    <p:bgPr>
      <a:solidFill>
        <a:srgbClr val="001514"/>
      </a:solidFill>
    </p:bgPr>
  </p:bg>
</p:cSld>
```

If this background is not extracted into IR, `python-pptx` creates rebuilt slides with the default white background.

## Implementation pattern

1. During C1 inventory, read `ppt/slides/slideN.xml` directly.
2. Extract `p:cSld/p:bg/p:bgPr` before object inventory is promoted.
3. Preserve a slide-level background field in C2 raw IR:

```json
"background": {
  "kind": "solid",
  "rgb": "001514",
  "source_xml_path": "ppt/slides/slide1.xml"
}
```

4. During C3 rebuild, apply background immediately after `prs.slides.add_slide(layout)` and before adding objects:

```python
fill = slide.background.fill
fill.solid()
fill.fore_color.rgb = RGBColor(...)
```

5. Record background materialization in `rebuild-report.json`:

```json
"backgrounds": [
  {
    "slide_id": "slide-01",
    "kind": "solid",
    "rgb": "001514",
    "produced": "native-slide-background"
  }
]
```

## Tests to add or preserve

- C2 decompiler test: sample slide with non-white background emits `slide["background"] == {"kind": "solid", "rgb": "123456", ...}`.
- C3 loop test: rebuilt PPTX `ppt/slides/slide1.xml` contains the same `p:bg/p:bgPr/a:solidFill/a:srgbClr` value.

## Interpretation of results

Background reconstruction can create very large visual-score deltas because it restores the deck's global material layer. In the P0 templates:

- `dark-minimalist-business`: C3.1 `27.72` → C3.2 `94.53`
- `it-software-sales-proposal-slides`: C3.1 `36.33` → C3.2 `80.64`

This does not mean the reusable template generator is done. It means the reverse compiler now understands one more PPTX material layer. Remaining low-scoring slides usually point to:

- grouped icon/shape systems still placeholdered;
- tables/charts not yet reconstructed;
- gradients or theme references not resolved;
- image crop/mask/transparency not yet applied;
- shape visual properties still too shallow.

## Promotion rule

Do not treat background color recovery as a complete visual DNA clone. Promote it as a reusable compiler capability and as evidence for palette/material extraction, then continue into group recursion, shape styling, chart/table classification, and component contract mining.
