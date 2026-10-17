"""Documentation preservation checks, not additional physics theorems."""
from __future__ import annotations
import base64
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / 'docs/atlas/2026-10-17-v0.4'


def test_v04_preserved_file_and_image_hashes():
    record = json.loads((ATLAS / 'snapshot.json').read_text())
    for name, expected in record['files'].items():
        assert hashlib.sha256((ATLAS / name).read_bytes()).hexdigest() == expected
    for image in record['images']:
        assert hashlib.sha256((ATLAS / image['file']).read_bytes()).hexdigest() == image['sha256']
    assert len(record['images']) == 6
    assert len(record['tabs']) == 3
    assert record['pdf']['reading_pages'] == 24
    assert record['pdf']['native_pages'] == 27
    assert record['revision_verified_after_exports'] is True


def test_readable_markdown_only_localizes_embedded_images():
    original = (ATLAS / 'google-export.md').read_text()
    count = []
    def replace(match):
        label, kind, data = match.groups()
        name = re.sub(r'[^a-zA-Z0-9_-]', '-', label) + '.' + ('jpg' if kind == 'jpeg' else kind)
        assert (ATLAS / 'assets' / name).read_bytes() == base64.b64decode(data)
        count.append(name)
        return '[' + label + ']: assets/' + name
    normalized = re.sub(r'\[([^\]]+)\]:\s*<data:image/([^;]+);base64,([^>]+)>', replace, original)
    assert normalized == (ATLAS / 'atlas.md').read_text()
    assert len(count) == 6


def test_latest_edition_contains_all_sections_and_no_placeholder():
    text = (ATLAS / 'atlas.md').read_text()
    for title in ('Cycle 02 — Physical constraints', 'Cycle 01 — Results & learning', 'Charter & foundations'):
        assert '# ' + title in text
    assert 'ATLAS_SCENARIO_TABLE' not in text
    assert 'Gate 03 remains open' in text
    assert '1.475' in text and '128.9' in text


def test_document_links_target_current_edition():
    readme = (ROOT / 'README.md').read_text()
    page = (ROOT / 'app/page.jsx').read_text()
    assert '[View the illustrated PDF](docs/atlas/2026-10-17-v0.4/atlas.pdf)' in readme
    assert '/blob/main/docs/atlas/2026-10-17-v0.4/atlas.pdf' in page
    assert '/blob/main/docs/atlas/2026-10-17-v0.2/atlas.pdf' not in page
    assert (ROOT / 'docs/atlas/2026-10-17-v0.2/atlas.pdf').is_file()
