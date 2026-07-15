# PPTX Cloner C3.5 Empty / Decorative Text Container Classification

Use this reference when C3 rebuild reports unsupported `text` objects after group recursion, but the source objects contain no meaningful text.

## Durable lesson

A PowerPoint object with a text frame is not always content. Template packs often contain empty text boxes or text-frame-capable decorative shapes, especially inside groups exported from Google Slides or design tools. If those empty containers are materialized as placeholders, the rebuilt deck gains artificial grey/purple blocks that do not exist in the source and pollute both visual fidelity and later template learning.

Empty text containers are metadata, not visual objects.

## Recognition rule

Classify an object as an empty text container when:

```text
obj.type == "text"
and obj.text.strip() == ""
```

For now this conservative rule applies only to `type: text`, not to empty `shape` objects. Empty shapes may still carry visible fill/stroke and should be handled by shape visual-property reconstruction.

## C2 IR pattern

C2 should mark these objects explicitly:

```json
{
  "type": "text",
  "text": "",
  "render_policy": "skip",
  "editability": {
    "priority": 1,
    "reason": "empty/decorative text container; preserve as metadata only"
  },
  "classification": {
    "kind": "empty-text-container",
    "reason": "text-frame object has no source text; treat as structural/decorative metadata rather than a visual placeholder"
  }
}
```

## C3 rebuild rule

During diagnostic rebuild:

1. If `classification.kind == "empty-text-container"`, do not draw a shape, text box, label, or placeholder.
2. Record materialization as:

```json
"produced": "skipped-empty-text-container"
```

3. Do not add it to `unsupported_objects`.
4. Preserve `source_shape_id`, `source_shape_name`, `group_id`, and `parent_group_name` in `rebuild-report.json` for traceability.

## Tests to preserve

- C2 decompiler test: a fixture empty text box becomes `classification.kind == "empty-text-container"`, `render_policy == "skip"`, and editability priority <= 1.
- C3 loop test: the same object produces `skipped-empty-text-container` and no `text` entries appear in `unsupported_objects`.

## Interpretation of results

This is a cleanup/classification increment, not a visual-style capability by itself. Its value is that it removes diagnostic noise after group recursion, allowing the next real blockers to surface.

Expected metric change:

- unsupported `text` count drops sharply or reaches zero;
- visual score may improve slightly if placeholders were visible;
- remaining unsupported classes become more semantically meaningful, e.g. `table`, `chart`, complex shapes, or unsupported media effects.

## Promotion rule

Do not infer template typography or component grammar from empty text containers. They may indicate authoring-tool artifacts, group scaffolding, or unused placeholders; keep them as provenance metadata only unless future evidence shows they encode a real layout slot contract.
