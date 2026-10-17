"""Prevent Git from silently rewriting byte-verified research CSVs."""
from pathlib import Path


def test_csv_line_endings_are_not_normalized_by_git():
    root = Path(__file__).resolve().parents[1]
    rules = (root / ".gitattributes").read_text().splitlines()
    assert "*.csv -text" in rules
