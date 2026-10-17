"""Verify original archive, frozen research outputs, atlas exports and migration hashes."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify(root: Path = ROOT) -> tuple[int, list[str]]:
    checked = 0
    failures = []
    manifest = json.loads((root / "provenance/cycle01/MANIFEST.json").read_text())
    with zipfile.ZipFile(root / "archives/gravity-witness-cycle01.zip") as archive:
        for name, expected in manifest["files"].items():
            actual = sha256(archive.read("gravity-witness/" + name))
            checked += 1
            if actual != expected:
                failures.append("Original archive mismatch: " + name)
    for name, expected in json.loads((root / "provenance/migration/immutable-sha256.json").read_text()).items():
        checked += 1
        path = root / name
        if not path.is_file() or sha256(path.read_bytes()) != expected:
            failures.append("Frozen artifact mismatch: " + name)
    atlas = root / "docs/atlas/2026-10-17-v0.2"
    metadata = json.loads((atlas / "snapshot.json").read_text())
    for name, expected in metadata["files"].items():
        checked += 1
        if sha256((atlas / name).read_bytes()) != expected:
            failures.append("Atlas export mismatch: " + name)
    for image in metadata["images"]:
        checked += 1
        if sha256((atlas / image["file"]).read_bytes()) != image["sha256"]:
            failures.append("Atlas image mismatch: " + image["file"])
    return checked, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    count, failures = verify()
    if failures:
        print("\n".join(failures))
        return 1
    print(f"PASS: {count} artifact integrity checks. Checksums establish preservation, not physics validity.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
