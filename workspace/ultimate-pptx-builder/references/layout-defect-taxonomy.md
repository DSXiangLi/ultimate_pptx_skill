# Layout Defect Taxonomy and Architecture Diagnosis

## Purpose

Generated PPTX output is not only a deliverable; it is a diagnostic sample for the generation architecture. A visible layout defect must not be fixed by moving coordinates until the defect is classified and the missing prevention mechanism is identified.

## Classification

### A. Local Slide Bug

A single slide has a coordinate, size, spacing, or z-order mistake while the underlying component grammar remains valid.

Examples:

- A footer is too close to one bottom card because a fixed `y` coordinate was reused.
- A local note/callout is anchored too high for the current paragraph length.
- A single route segment touches one card edge.

Preferred fix:

- Adjust the shared helper or local layout slot only after confirming the issue is not repeated across roles/systems.
- Add a regression fixture if the same topology can reappear.

### B. Style-DNA Adaptation Bug

The visual system is coherent, but its component/layout grammar is not adapted to the page role, content density, language, or narrative topology.

Examples:

- A dark dashboard DNA creates too many tiny KPI cards for Chinese labels.
- A paper report DNA keeps a strong right summary rail on table-led or checklist-led pages.
- An atlas DNA treats routes as fixed decoration even when the page needs a clean title zone.

Preferred fix:

- Add page-role variants inside the visual system: chart-led, table-led, checklist-led, scenario-led, process-led, memo-led, KPI-led.
- Let content density and page intent select the variant.
- Change component grammar, not only coordinates.

### C. Systemic Skill / Architecture / Gate Gap

The deck passes existing automated checks, but human review finds a class of layout failure that could recur across future decks. The issue is missing from the skill contract or executable validation.

Examples:

- Microtext is technically native and non-overlapping but too small to read.
- Chart containers pass bounding-box checks but internal axis/legend labels are unreadable.
- Process pages contain too many nodes/cards for one slide.
- Decorative routes or grids enter title, chart, or body safe areas.
- A secondary right rail visually dominates chart/table/checklist pages.

Preferred fix:

- Update the skill reference and executable gates before repairing the deck.
- Make the current defective output fail the new gate.
- Repair via compiler/layout grammar until the gate passes.

## Required Diagnosis Before Fixing

For every visible layout problem, record:

```text
slide/system:
symptom:
class: A | B | C
root cause:
missing gate or grammar:
repair level: local slot | style variant | architecture/gate
future avoidability: preventable | partially preventable | inherently subjective
```

## Future Avoidability

Most PPTX layout defects are preventable when they involve geometry, density, text size, hierarchy, or safe areas. They should be treated as architecture bugs, not subjective polish.

| Defect class | Future avoidability |
|---|---|
| Text-box overlap / container collision | Nearly fully preventable |
| Title/decor/route unsafe proximity | Nearly fully preventable |
| Microtext below role threshold | Nearly fully preventable |
| Chart/table/checklist density overflow | Nearly fully preventable |
| Route/grid crossing content zones | Nearly fully preventable |
| Wrong page-role variant selection | Mostly preventable with content classification |
| Weak aesthetic taste / visual novelty | Partially preventable with rubrics and review |

## Blocking Rule

A generated deck must not be accepted if a visible layout issue is classified as C and no skill/gate update has been made. Fixing the current deck without updating the prevention mechanism is considered incomplete.

## Acceptance Criteria

- Every visible layout defect is classified as A local slide bug, B style-DNA adaptation bug, or C systemic skill/gate gap before repair.
- A class-C defect blocks release until the skill reference or executable gate is updated.
- The current failing output must fail the new gate before the compiler/layout grammar is repaired.
- The repaired deck must pass both geometric layout safety and visual layout architecture gates.
- Remaining subjective or local weaknesses must be documented separately from systemic gate failures.

