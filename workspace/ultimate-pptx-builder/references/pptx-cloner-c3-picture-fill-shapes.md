# PPTX Cloner C3.3 Picture-Fill Shape Reconstruction

Use this reference when C3 rebuilds show grey rectangles or generic shapes where the source deck visually shows a photo, abstract texture, device mockup, or decorative raster material.

## Durable lesson

Not every image-like visual in PPTX is a `<p:pic>` object. Some templates encode raster material as a normal shape (`<p:sp>`) whose shape properties contain an image blip fill:

```xml
<p:sp>
  <p:nvSpPr>
    <p:cNvPr id="315" name="Google Shape;315;p22"/>
  </p:nvSpPr>
  <p:spPr>
    ...
    <a:blipFill>
      <a:blip r:embed="rId3"/>
    </a:blipFill>
  </p:spPr>
</p:sp>
```

If C1 only scans `<p:pic>`, this object enters IR as `type: shape` with `fill_type: PICTURE` but no media reference. C3 then rebuilds it as a generic grey native shape, often covering a correctly restored slide background.

## Implementation pattern

1. During C1 inventory, scan both:
   - `<p:pic>`
   - `<p:sp>` containing any descendant `<a:blip>`
2. Resolve `r:embed` or `r:link` through `ppt/slides/_rels/slideN.xml.rels` just like normal picture objects.
3. Preserve the media reference on the shape as `fill_image_ref`:

```json
"fill_image_ref": {
  "relationship_id": "rId3",
  "relationship_type": "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image",
  "target": "../media/image12.png",
  "package_path": "ppt/media/image12.png"
}
```

4. During C3 rebuild, materialize picture-fill shapes as native PPTX pictures using the original shape box:

```python
slide.shapes.add_picture(BytesIO(blob), x, y, w, h)
```

5. Record the output as `native-picture-fill-shape-image`, not `native-shape`.

## Tests to add or preserve

- C2 decompiler test: a known picture-fill shape has `fill_image_ref.relationship_id` and `fill_image_ref.package_path`.
- C3 loop test: the same source shape materializes as `native-picture-fill-shape-image` in `rebuild-report.json`.

## Interpretation of results

This is not full shape styling support. It is a high-leverage raster-material recovery path for shapes whose visual meaning is actually an embedded image. Remaining fidelity gaps may still require:

- crop/mask support (`a:srcRect`, custom geometry masks);
- transparency/effect handling;
- group recursion;
- native vector reconstruction for non-raster shapes;
- z-order and clipping refinements.

## Promotion rule

Promote this as a reverse-compiler material capability, not as template DNA by itself. Visual DNA extraction may later use it as evidence for texture/photo/mockup treatment, but only after the reusable generator has a deliberate policy for when to keep, abstract, replace, or parameterize those raster materials.
