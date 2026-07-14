# PPTX Cloner C3.4 Group Recursion / Child Flattening

Use this reference when C3 rebuild reports many `group` placeholders or visual diffs show missing grouped icons, cards, decorative bands, or compound components.

## Durable lesson

PowerPoint groups are not atomic visual objects. Many high-quality templates encode important component grammar as grouped child shapes, text boxes, images, and picture-fill shapes. Treating a group as one opaque placeholder destroys both fidelity and downstream template learning.

The reverse compiler should preserve the group container as structure while emitting its children as traceable IR objects:

```json
{
  "id": "slide10_shape315",
  "type": "shape",
  "group_id": "slide10_shape300",
  "parent_group_name": "Pricing card group",
  "group_depth": 1,
  "source_shape_id": "315"
}
```

## Implementation pattern

1. During C1 inventory, when a shape has `shape_type == GROUP` and exposes `.shapes`, recursively walk children.
2. Emit the group container as `type: group` with `child_count`.
3. Emit each child as a normal object with:
   - `group_id`
   - `parent_group_name`
   - `group_depth`
   - original `source_shape_id/name`
   - normal box/style/font/image/fill-image fields
4. During C2 raw IR, preserve those group fields.
5. During C3 rebuild, do **not** draw a placeholder for a group container with children. Record it as:

```json
"produced": "expanded-group-container"
```

6. Rebuild the emitted children normally in z-order.
7. Keep opaque placeholder fallback only for group containers that cannot expose children.

## Tests to add or preserve

- C2 decompiler test: grouped child text appears in slide IR and carries `group_id` + `parent_group_name`.
- C3 loop test: expanded group containers materialize as `expanded-group-container`, not `native-placeholder`, and do not appear in `unsupported_objects`.

## Interpretation of results

Group recursion usually improves both fidelity and learning quality:

- grouped text contributes to native text recall;
- grouped images and picture-fill shapes can reuse C3.1/C3.3 materialization;
- grouped component geometry becomes available for C4/C5 component mining;
- unsupported counts shift from opaque `group` placeholders to more precise child-level gaps.

After group recursion, remaining gaps often become more actionable:

- empty text containers that should be skipped rather than placeholdered;
- tables/charts requiring classification/native reconstruction;
- custom geometry, gradients, alpha, crop/mask effects;
- nested group transform errors.

## Promotion rule

Do not promote a component contract from a grouped source until the group is expanded and the repeated child structure is visible in IR. A group placeholder is evidence of a missing compiler capability, not evidence of a reusable component grammar.
