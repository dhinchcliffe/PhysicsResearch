# The research atlas

The atlas is the director's explanatory canvas: intuition, definitions, examples, calculations, objections and decisions in one narrative.

## Current edition — v0.4, 17 October 2026

[Read the complete atlas](2026-10-17-v0.4/atlas.md) · [Download the illustrated PDF](2026-10-17-v0.4/atlas.pdf) · [Export and processing provenance](2026-10-17-v0.4/snapshot.json)

Start with **Cycle 02 — Physical constraints**. The author-reviewed edition incorporates the finite-sphere calculation, the non-overlap condition, the shielding-clearance diagnostic, conditional force/noise comparisons and the practical review request. **Gate 03 remains open:** no experimentally viable parameter window or universal exclusion of Diósi–Penrose models has been established.

The complete edition has three sections: Cycle 02, Cycle 01 and Charter & foundations. All six figures and the illustrative parameter table are included. The reading PDF has **24 numbered pages** and remapped bookmarks. The unchanged [native PDF export](2026-10-17-v0.4/google-export.pdf) has 27 pages; the reading copy removes only the three exact-title Google tab-divider pages, then adds running headers and page numbers. No research text or figure was removed.

The [native Markdown export](2026-10-17-v0.4/google-export.md) is preserved. The GitHub-readable version changes only embedded base64 image definitions to relative asset paths.

[Living Google Doc](https://docs.google.com/document/d/1rkQ5z3phVVdCVBP6Obtn3HBA1U6YbQ9L78HwgeqdGAc)

The v0.4 author pass was applied to that live document. It reconciles older infrastructure statements with subsequent GitHub publication and the four-lemma Lean verification, distinguishes the two distance conventions, and makes model assumptions and evidence limitations explicit. It introduces no new calculation or gate advancement. The frozen scientific records are unchanged.

## Historical edition

[v0.2 narrative](2026-10-17-v0.2/atlas.md) · [v0.2 native PDF](2026-10-17-v0.2/atlas.pdf) · [v0.2 provenance](2026-10-17-v0.2/snapshot.json)

This original two-tab, four-figure snapshot remains untouched, including its then-current statements about an unavailable remote and an uncompiled Lean draft. Those are historical execution conditions, not the current status.

## Reproduce the reading-copy preparation

The document-only processor is [prepare_snapshot.py](2026-10-17-v0.4/prepare_snapshot.py). In a separate environment, install its pinned PDF dependency and process the preserved native exports:

```bash
python -m venv .venv-atlas
# macOS/Linux:
source .venv-atlas/bin/activate
# Windows PowerShell instead: .\.venv-atlas\Scripts\Activate.ps1
python -m pip install PyMuPDF==1.26.7
python docs/atlas/2026-10-17-v0.4/prepare_snapshot.py
```

This regenerates only the dated edition's derived Markdown, assets, reading PDF and metadata. It does not edit the native exports, install scientific dependencies, execute physics calculations or modify earlier snapshots. Regenerate in a scratch copy with `--directory` to avoid changing tracked derived files during experimentation.

## Refresh procedure

Read current native document metadata and all tab identities. Perform requested editorial changes in place, with revision-guarded writes. Export fresh PDF and Markdown; verify the revision again after both exports and repeat if it changed mid-export.

Create a new dated/versioned folder, preserving raw exports. Check every section, figure, table and notation in rendered PDF pages. Any reading-copy transformation must be explicit and reproducible; preserve all narrative content. Record document/revision IDs, export time, transformations and hashes in `snapshot.json`.

Update this index, the root README and the dashboard PDF target in the reviewed commit. Keep historical snapshots and scientific baselines unchanged. Google Docs comments and revision history are not part of an export; the native document remains their source of truth.
