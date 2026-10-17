"""Cross-platform, non-destructive Cycle 01 reproduction. No network calls."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "projects/gravity-witness"


def run_logged(command: list[str], log: Path, env: dict[str, str]) -> None:
    """Preserve output and fail immediately when a subprocess fails."""
    print("Running:", " ".join(command), flush=True)
    with log.open("w", encoding="utf-8") as output:
        process = subprocess.Popen(command, cwd=ROOT, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert process.stdout is not None
        for line in process.stdout:
            output.write(line)
            print(line, end="", flush=True)
        result = process.wait()
    if result:
        raise subprocess.CalledProcessError(result, command)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New output directory inside build/; must not exist.")
    args = parser.parse_args()
    now = datetime.now(timezone.utc)
    output = args.output or Path("build/gravity-witness") / now.strftime("%Y%m%dT%H%M%S.%fZ")
    output = (ROOT / output).resolve() if not output.is_absolute() else output.resolve()
    if not output.is_relative_to((ROOT / "build").resolve()):
        parser.error("Output must be inside build/ to protect committed research snapshots.")
    if output.exists():
        parser.error(f"Refusing to overwrite {output}; choose a new output directory.")
    results = output / "results"
    results.mkdir(parents=True)
    (output / "figures").mkdir()
    env = os.environ.copy()
    env["PYTHONPATH"] = str(PROJECT / "src") + os.pathsep + env.get("PYTHONPATH", "")
    env["GW_OUTPUT_DIR"] = str(output)
    env["MPLBACKEND"] = "Agg"
    env["PYTHONHASHSEED"] = "0"
    report = {"started_at_utc": now.isoformat(), "python": platform.python_version(),
              "platform": platform.platform(), "status": "running",
              "network_dependencies_reinstalled": False,
              "purpose": "numerical/software reproduction, not a formal proof or experiment",
              "packages": {}}
    try:
        for line in (ROOT / "requirements.lock").read_text().splitlines():
            if "==" in line:
                name, expected = line.split("==", 1)
                actual = importlib.metadata.version(name)
                report["packages"][name] = {"expected": expected, "actual": actual}
                if actual != expected:
                    raise RuntimeError(f"Pinned dependency mismatch: {name}: {actual} != {expected}")
        if sys.version_info[:2] != (3, 13):
            raise RuntimeError("Use Python 3.13 for the pinned Cycle 01 environment.")
        run_logged([sys.executable, "-m", "pytest", "-q", str(PROJECT / "tests"),
                    f"--junitxml={results / 'pytest.xml'}"], results / "pytest.txt", env)
        suites = list(ET.parse(results / "pytest.xml").getroot().iter("testsuite"))
        checks = {key: sum(int(s.attrib.get(key, 0)) for s in suites)
                  for key in ("tests", "failures", "errors", "skipped")}
        if checks["tests"] != 970 or any(checks[k] for k in ("failures", "errors", "skipped")):
            raise RuntimeError(f"Cycle 01 test gate changed: {checks}; review deliberately.")
        run_logged([sys.executable, str(PROJECT / "scripts/run_dp.py")], results / "run_dp.log", env)
        run_logged([sys.executable, str(PROJECT / "scripts/run_cycle01.py")], results / "run_cycle01.log", env)
        run_logged([sys.executable, str(ROOT / "tools/compare_results.py"), str(output)],
                   results / "comparison.log", env)
        report["status"] = "passed"
        report["scientific_test_counts"] = checks
    except (subprocess.CalledProcessError, RuntimeError, importlib.metadata.PackageNotFoundError) as exc:
        report["status"] = "failed"
        report["error"] = str(exc)
        print(f"Reproduction failed: {exc}", file=sys.stderr)
    finally:
        report["finished_at_utc"] = datetime.now(timezone.utc).isoformat()
        (output / "run.json").write_text(json.dumps(report, indent=2) + "\n")
        print(f"Run record: {output / 'run.json'}")
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
