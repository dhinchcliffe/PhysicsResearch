"""Attempt the pinned Lean build; missing tools or proof holes fail, never silently pass."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
FORMAL = ROOT / "projects/gravity-witness/formal"


def uncomment(source: str) -> str:
    """Remove nested Lean block and line comments for a narrow admission lint."""
    out = []
    i, depth = 0, 0
    while i < len(source):
        if source[i:i+2] == "/-":
            depth += 1; i += 2
        elif depth and source[i:i+2] == "-/":
            depth -= 1; i += 2
        elif depth:
            i += 1
        elif source[i:i+2] == "--":
            end = source.find("\n", i)
            i = len(source) if end == -1 else end
        else:
            out.append(source[i]); i += 1
    return "".join(out)


def admission_tokens(source: str) -> list[str]:
    return re.findall(r"\b(?:sorry|admit|sorryAx|axiom)\b", uncomment(source))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true", help="Resolve pinned dependencies and fetch mathlib cache (network required).")
    parser.add_argument("--output", type=Path, default=ROOT / "build/formal/latest")
    args = parser.parse_args()
    output = (ROOT / args.output).resolve() if not args.output.is_absolute() else args.output.resolve()
    if not output.is_relative_to((ROOT / "build").resolve()):
        parser.error("Output must be inside build/.")
    output.mkdir(parents=True, exist_ok=True)
    report = {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "status": "not_checked",
              "toolchain": (FORMAL / "lean-toolchain").read_text().strip(),
              "source_sha256": hashlib.sha256((FORMAL / "GravityWitness.lean").read_bytes()).hexdigest(),
              "scope": "four algebra lemmas only; not quantum field theory, experimental validity or a unified theory"}
    command_log = output / "lean.log"
    code = 1
    try:
        tokens = admission_tokens((FORMAL / "GravityWitness.lean").read_text())
        if tokens:
            raise RuntimeError("Explicit proof admission or custom axiom found: " + ", ".join(tokens))
        lake = shutil.which("lake")
        if not lake:
            report["status"] = "blocked"
            raise RuntimeError("lake is missing. Install elan/Lean as documented in README.md.")
        commands = [[lake, "env", "lean", "--version"]]
        if args.prepare:
            commands += [[lake, "update"], [lake, "exe", "cache", "get"]]
        commands += [[lake, "build"], [lake, "env", "lean", "GravityWitness.lean"],
                     [lake, "env", "lean", "AxiomAudit.lean"]]
        with command_log.open("w", encoding="utf-8") as log:
            for command in commands:
                log.write("$ " + " ".join(command) + "\n"); log.flush()
                result = subprocess.run(command, cwd=FORMAL, text=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT, check=False)
                log.write(result.stdout); log.flush(); print(result.stdout, end="")
                if result.returncode:
                    raise RuntimeError("Lean command failed: " + " ".join(command))
                if command[-1] == "AxiomAudit.lean" and "sorryAx" in result.stdout:
                    raise RuntimeError("Axiom audit includes sorryAx.")
        report["status"] = "kernel_checked"
        report["audit_note"] = "Inspect lean.log and standard Lean axioms; kernel checking does not verify physical assumptions."
        manifest = FORMAL / "lake-manifest.json"
        if manifest.exists():
            shutil.copy2(manifest, output / "lake-manifest.json")
            report["lake_manifest_sha256"] = hashlib.sha256(manifest.read_bytes()).hexdigest()
        code = 0
    except (RuntimeError, OSError) as exc:
        if report["status"] != "blocked":
            report["status"] = "failed"
        report["error"] = str(exc)
        print(str(exc), file=sys.stderr)
    (output / "status.json").write_text(json.dumps(report, indent=2) + "\n")
    print("Formal report:", output / "status.json")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
