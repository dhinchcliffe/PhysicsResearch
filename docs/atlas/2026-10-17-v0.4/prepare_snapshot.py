"""Build the v0.4 reading copies from the two unchanged native Google exports.

Optional document-only dependency: PyMuPDF==1.26.7. No scientific code is run.
Run in this directory, or pass --directory to a copy containing the raw exports.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import fitz

DOC_ID = '1rkQ5z3phVVdCVBP6Obtn3HBA1U6YbQ9L78HwgeqdGAc'
REVISION = 'AHj4eMR3Cicn68IMmkd3KhBdO4JrwtkmUzTK6FlQF2DeppOScYz0RodY_C_BwzMzuMCdukrWdZwSKlC6DuoV1RIOG_Wzo_Cmig4ufcP5G0E'
TABS = [('t.pruzy2mq6utx', 'Cycle 02 — Physical constraints'),
        ('t.q5e9ydjw0gsh', 'Cycle 01 — Results & learning'),
        ('t.0', 'Charter & foundations')]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(folder: Path) -> dict:
    folder = folder.resolve()
    raw_md = (folder / 'google-export.md').read_text(encoding='utf-8')
    for _, name in TABS:
        if '# ' + name not in raw_md:
            raise ValueError('Missing document tab: ' + name)
    if 'ATLAS_SCENARIO_TABLE' in raw_md:
        raise ValueError('Unfilled scenario table')
    assets = folder / 'assets'
    assets.mkdir(exist_ok=True)
    images = []

    def image(match: re.Match) -> str:
        label, kind, data = match.groups()
        name = re.sub(r'[^a-zA-Z0-9_-]', '-', label) + '.' + ('jpg' if kind == 'jpeg' else kind)
        path = assets / name
        path.write_bytes(base64.b64decode(data, validate=True))
        images.append({'file': 'assets/' + name, 'sha256': digest(path)})
        return '[' + label + ']: assets/' + name

    markdown = re.sub(r'\[([^\]]+)\]:\s*<data:image/([^;]+);base64,([^>]+)>', image, raw_md)
    if len(images) != 6:
        raise ValueError('Expected the six preserved atlas figures')
    (folder / 'atlas.md').write_text(markdown, encoding='utf-8')

    pdf = fitz.open(folder / 'google-export.pdf')
    original_pages = len(pdf)
    outline = pdf.get_toc()
    dividers = {title for _, title in TABS}
    removed = [i for i, page in enumerate(pdf)
               if ' '.join(page.get_text().split()) in dividers and not page.get_images()]
    if len(removed) != 3:
        raise ValueError('Only the three exact Google tab-divider pages may be removed')
    keep = [i for i in range(len(pdf)) if i not in removed]
    original_texts = [pdf[i].get_text() for i in keep]
    original_images = sum(len(pdf[i].get_images()) for i in keep)
    if original_images != 6:
        raise ValueError('Native PDF does not contain six figures')
    pdf.select(keep)
    for i, page in enumerate(pdf):
        if page.get_text() != original_texts[i]:
            raise ValueError('Page selection changed narrative text')
        width, height = page.rect.width, page.rect.height
        header = 'GRAVITY WITNESS / RESEARCH ATLAS'
        page.insert_text((72, 38), header, fontname='helv', fontsize=8, color=(.25,.34,.32))
        page.draw_line((72, 49), (width-72, 49), color=(.80,.82,.79), width=.5)
        page.insert_text((72, height-33), 'AUTHOR REVIEW / 17 OCT 2026 / v0.4',
                         fontname='helv', fontsize=7.5, color=(.45,.49,.45))
        number = f'{i+1} / {len(pdf)}'
        x = width-72-fitz.get_text_length(number, fontname='helv', fontsize=8)
        page.insert_text((x, height-33), number, fontname='helv', fontsize=8, color=(.25,.34,.32))
    toc = []
    for level, title, old_page in outline:
        old_index = old_page-1
        if old_page < 1:
            continue
        if old_index in removed:
            old_index += 1
        if old_index not in keep:
            continue
        new_page = keep.index(old_index)+1
        toc.append([level, title.strip(), new_page])
    pdf.set_toc(toc)
    metadata = pdf.metadata
    metadata.update(title='Project Gravity Witness — Research Atlas v0.4',
                    author='Dion Hinchcliffe',
                    subject='Cycle 01 foundations and Cycle 02 physical-constraint audit; Gate 03 remains open')
    pdf.set_metadata(metadata)
    pdf.save(folder / 'atlas.pdf', garbage=4, deflate=True, no_new_id=True)
    pdf.close()
    check = fitz.open(folder / 'atlas.pdf')
    if len(check) != original_pages-3 or sum(len(p.get_images()) for p in check) != 6:
        raise ValueError('Final PDF page or figure count mismatch')
    for i, page in enumerate(check):
        if not all(word in page.get_text() for word in original_texts[i].split()):
            raise ValueError('Export lost narrative text')
    report = {
        'edition': '0.4', 'date': '2026-10-17',
        'source_document_id': DOC_ID,
        'source_document_url': 'https://docs.google.com/document/d/' + DOC_ID,
        'source_revision_id': REVISION,
        'exported_at_utc': '2026-10-17T14:31:20Z',
        'revision_verified_after_exports': True,
        'source_code_commit': '6ad5f4b7d4b280890829e1ce1773a317d46f953e',
        'tabs': [{'id': tab, 'title': title} for tab, title in TABS],
        'images': images,
        'pdf': {'native_pages': original_pages, 'reading_pages': len(check),
                'removed_native_pages_1_based': [i+1 for i in removed],
                'reason': 'Only exact-title, image-free Google tab divider pages removed; no research content removed',
                'additional_changes': 'Running header, page numbers, metadata and remapped bookmarks only',
                'all_kept_page_text_and_six_figures_preserved': True,
                'processor': 'PyMuPDF ' + fitz.VersionBind},
        'markdown_changes': 'Only inline base64 image definitions replaced by relative asset references',
        'editorial_scope': 'Source-based author pass; no new calculation, no experimental viability claim; Gate 03 open',
        'files': {name: digest(folder / name) for name in
                  ('google-export.pdf', 'google-export.md', 'atlas.pdf', 'atlas.md')},
    }
    (folder / 'snapshot.json').write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    check.close()
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    result = prepare(args.directory)
    print(json.dumps({'pages': result['pdf']['reading_pages'], 'figures': len(result['images']),
                      'pdf_sha256': result['files']['atlas.pdf']}, indent=2))
