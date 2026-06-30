#!/usr/bin/env python3
"""Check that visual language and narrative intent remain orthogonal.

Visual language names/grammar must describe visual attributes only: palette,
material, typography, light, motif, container grammar, density, rhythm. Narrative
intent may describe business use cases such as committee decision, strategy
update, or risk review, but those terms must not leak into visual identifiers.
"""
from __future__ import annotations
from pathlib import Path
import copy
import json
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
VARIANT_DIR = ROOT / "examples" / "variants"
COMPILER = ROOT / "scripts" / "compile_spec_to_ir.py"
ANCHOR = ROOT / "examples" / "visual-anchors" / "glass-fintech-pptx.anchor.json"

VISUAL_LANGUAGES = {"matte-institutional", "luminous-glass", "terminal-cockpit"}
NARRATIVE_INTENTS = {"investment_committee_decision", "strategy_update", "risk_review"}
NARRATIVE_LEAK_TERMS = {
    "committee", "strategy", "risk-review", "risk_review", "stress", "pressure", "allocation",
    "投委会", "策略", "风险复盘", "压力测试", "资产配置", "审议",
}
VISUAL_KEYS = {
    "visual_language", "visual_variant", "visual_grammar", "visual_coordinates",
    "motif", "panel_material", "metric_style", "footer_treatment", "layout_rhythm",
    "chart_treatment", "controlled_visual_languages", "controlled_variants",
}


def fail(msg: str) -> None:
    print("FAIL narrative/visual orthogonality: " + msg)
    sys.exit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path}: {exc}")


def has_leak(value) -> str | None:
    text = json.dumps(value, ensure_ascii=False).lower() if not isinstance(value, str) else value.lower()
    for term in NARRATIVE_LEAK_TERMS:
        if term.lower() in text:
            return term
    return None


def check_visual_identifier(label: str, value) -> None:
    leak = has_leak(value)
    if leak:
        fail(f"{label} leaks narrative/business term {leak!r}: {value!r}")


def compile_contract(contract: dict) -> dict:
    with tempfile.TemporaryDirectory(prefix="pptx-orthogonality-") as td:
        in_path = Path(td) / "contract.json"
        out_path = Path(td) / "out.ir.json"
        in_path.write_text(json.dumps(contract, ensure_ascii=False, indent=2), encoding="utf-8")
        proc = subprocess.run([sys.executable, str(COMPILER), str(in_path), str(out_path)], cwd=str(ROOT), text=True, capture_output=True)
        if proc.returncode != 0:
            fail("compiler failed during orthogonality check:\nSTDOUT:\n%s\nSTDERR:\n%s" % (proc.stdout, proc.stderr))
        return load_json(out_path)


def role_counts(ir: dict) -> dict[str, int]:
    counts = {}
    for slide in ir.get("deck", {}).get("slides", []):
        for obj in slide.get("objects", []):
            role = obj.get("role")
            counts[role] = counts.get(role, 0) + 1
    return counts


def check_anchor() -> None:
    doc = load_json(ANCHOR)
    anchor = doc.get("visual_anchor") or {}
    controlled = anchor.get("controlled_visual_languages") or anchor.get("controlled_variants") or {}
    if set(controlled) != VISUAL_LANGUAGES:
        fail(f"anchor controlled visual languages must be {sorted(VISUAL_LANGUAGES)}, got {sorted(controlled)}")
    for name, spec in controlled.items():
        check_visual_identifier(f"anchor visual language name {name}", name)
        check_visual_identifier(f"anchor visual language spec {name}", spec)
    coords = anchor.get("mutable_coordinates") or {}
    if "compliance_tone" in coords:
        fail("mutable_coordinates.compliance_tone couples visual anchor to business/compliance narrative; use formality or footer_treatment instead")
    for key, value in coords.items():
        check_visual_identifier(f"mutable coordinate {key}", key)
        check_visual_identifier(f"mutable coordinate values {key}", value)


def check_contracts() -> list[Path]:
    files = sorted(VARIANT_DIR.glob("glass-fintech-*.contract.json"))
    if not files:
        fail("no controlled variant contracts found")
    seen_visual = set()
    seen_narrative = set()
    for path in files:
        contract = load_json(path)
        visual_language = contract.get("visual_language")
        narrative_intent = contract.get("narrative_intent")
        if visual_language not in VISUAL_LANGUAGES:
            fail(f"{path.name} visual_language must be one of {sorted(VISUAL_LANGUAGES)}, got {visual_language!r}")
        if narrative_intent not in NARRATIVE_INTENTS:
            fail(f"{path.name} narrative_intent must be one of {sorted(NARRATIVE_INTENTS)}, got {narrative_intent!r}")
        if "visual_variant" in contract:
            fail(f"{path.name} still uses visual_variant; use visual_language + narrative_intent")
        check_visual_identifier(f"{path.name} visual_language", visual_language)
        check_visual_identifier(f"{path.name} visual_coordinates", contract.get("visual_coordinates", {}))
        seen_visual.add(visual_language)
        seen_narrative.add(narrative_intent)
    if seen_visual != VISUAL_LANGUAGES:
        fail(f"controlled contracts do not cover all visual languages: {sorted(seen_visual)}")
    if seen_narrative != NARRATIVE_INTENTS:
        fail(f"controlled contracts do not cover all narrative intents: {sorted(seen_narrative)}")
    return files


def check_compiler_orthogonality(files: list[Path]) -> None:
    # A narrative-intent change must not change visual grammar or visual roles for the same visual_language.
    sample = load_json(files[0])
    base_ir = compile_contract(sample)
    base_deck = base_ir.get("deck") or {}
    if base_deck.get("visual_language") != sample.get("visual_language"):
        fail("IR does not preserve visual_language from contract")
    if base_deck.get("narrative_intent") != sample.get("narrative_intent"):
        fail("IR does not preserve narrative_intent from contract")
    changed = copy.deepcopy(sample)
    alternatives = sorted(NARRATIVE_INTENTS - {sample.get("narrative_intent")})
    changed["narrative_intent"] = alternatives[0]
    changed_ir = compile_contract(changed)
    if changed_ir.get("deck", {}).get("visual_grammar") != base_deck.get("visual_grammar"):
        fail("Changing narrative_intent changed visual_grammar; visual language is coupled to narrative")
    visual_role_set = {"institutional-gridline", "institutional-ruler", "luminous-ribbon", "spotlight-orb", "terminal-gridline", "status-chip"}
    base_roles = {k: v for k, v in role_counts(base_ir).items() if k in visual_role_set}
    changed_roles = {k: v for k, v in role_counts(changed_ir).items() if k in visual_role_set}
    if base_roles != changed_roles:
        fail("Changing narrative_intent changed visual-language role counts; visual roles are coupled to narrative")

    # A visual-language change on the same narrative/content must change visual grammar.
    changed_visual = copy.deepcopy(sample)
    changed_visual["visual_language"] = sorted(VISUAL_LANGUAGES - {sample.get("visual_language")})[0]
    changed_visual_ir = compile_contract(changed_visual)
    if changed_visual_ir.get("deck", {}).get("visual_grammar") == base_deck.get("visual_grammar"):
        fail("Changing visual_language did not change visual_grammar")
    if changed_visual_ir.get("deck", {}).get("narrative_intent") != sample.get("narrative_intent"):
        fail("Changing visual_language changed narrative_intent")


def main() -> int:
    check_anchor()
    files = check_contracts()
    check_compiler_orthogonality(files)
    print("PASS narrative/visual orthogonality visual_languages=%d narrative_intents=%d" % (len(VISUAL_LANGUAGES), len(NARRATIVE_INTENTS)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
