"""Preservation and tooling checks; these are not additional physics theorems."""
from __future__ import annotations
import ast
import base64
import importlib.util
import json
import math
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET
import pytest

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects/gravity-witness"


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_all_frozen_artifacts_are_preserved():
    count, failures = load_tool("verify_artifacts").verify()
    assert count >= 44
    assert failures == []


def test_historical_research_count_is_not_inflated():
    suites = ET.parse(PROJECT / "results/cycle01/pytest.xml").getroot().iter("testsuite")
    rows = list(suites)
    assert sum(int(r.attrib["tests"]) for r in rows) == 970
    for key in ("failures", "errors", "skipped"):
        assert sum(int(r.attrib.get(key, 0)) for r in rows) == 0


@pytest.mark.parametrize("filename", ["gw.py", "dp.py", "test_gw.py", "test_dp.py"])
def test_scientific_statements_unchanged_except_import_paths(filename):
    with zipfile.ZipFile(ROOT / "archives/gravity-witness-cycle01.zip") as z:
        original = z.read("gravity-witness/" + filename).decode()
    path = PROJECT / ("tests" if filename.startswith("test_") else "src/gravity_witness") / filename
    moved = path.read_text()
    def nonimport_ast(source):
        tree = ast.parse(source)
        tree.body = [node for node in tree.body if not isinstance(node, (ast.Import, ast.ImportFrom))]
        return ast.dump(tree, include_attributes=False)
    assert nonimport_ast(original) == nonimport_ast(moved)


def test_atlas_contains_both_tabs_and_four_images():
    folder = ROOT / "docs/atlas/2026-10-17-v0.2"
    source = (folder / "google-export.md").read_text()
    normalized = (folder / "atlas.md").read_text()
    images = []
    def normalizer(match):
        label, typ, content = match.groups()
        name = re.sub(r'[^a-zA-Z0-9_-]', '-', label) + '.' + ('jpg' if typ == 'jpeg' else typ)
        assert (folder / "assets" / name).read_bytes() == base64.b64decode(content)
        images.append(name)
        return f"[{label}]: assets/{name}"
    expected = re.sub(r'\[([^\]]+)\]:\s*<data:image/([^;]+);base64,([^>]+)>', normalizer, source)
    assert expected == normalized
    assert len(images) == 4
    assert "# Cycle 01 — Results & learning" in normalized
    assert "# Charter & foundations" in normalized


@pytest.mark.parametrize("bad", [float("nan"), float("inf"), 1.01, "1.0"])
def test_numeric_comparison_detects_bad_values(bad):
    assert load_tool("compare_results").compare_numeric({"x": 1.0}, {"x": bad})


def test_numeric_comparison_accepts_stated_tolerance():
    assert load_tool("compare_results").compare_numeric({"x": 1.0}, {"x": 1 + 1e-11}) == []


def test_numeric_comparison_detects_missing_and_shape_changes():
    module = load_tool("compare_results")
    assert module.compare_numeric({"x": 1.0}, {})
    assert module.compare_numeric([1, 2], [1])


def test_formal_lint_ignores_comments_but_rejects_admissions():
    module = load_tool("check_formal")
    assert module.admission_tokens("/- sorry /- admit -/ -/\n-- axiom\ntheorem x : True := by trivial") == []
    assert module.admission_tokens("theorem x : True := by sorry") == ["sorry"]
    assert module.admission_tokens("axiom anything : False") == ["axiom"]


def test_draft_has_no_explicit_admissions():
    assert load_tool("check_formal").admission_tokens((PROJECT / "formal/GravityWitness.lean").read_text()) == []


def test_reproduction_outputs_are_not_committed_baselines():
    source = (ROOT / "tools/reproduce.py").read_text()
    assert "Refusing to overwrite" in source
    assert "Output must be inside build/" in source
    assert "GW_OUTPUT_DIR" in source
