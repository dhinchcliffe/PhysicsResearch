"""Compare reproduced scientific numbers with the frozen Cycle 01 baseline."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "projects/gravity-witness/results/cycle01"

# The peak coordinate is a flat-maximum optimizer diagnostic, not a measured
# observable. At u ≈ 408, shifts of 1e-5 change negativity by ~1e-16:
# floating-point evaluation can move the reported argmax without moving the
# peak height. Keep all predicted physical values at strict baseline tolerance.
PEAK_LOCATION_PATH = "dp_reproduction.json/example/numerical_peak_u"


def compare_numeric(expected, actual, path: str = "", failures=None) -> list[str]:
    if failures is None:
        failures = []
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            failures.append(f"{path}: expected mapping")
        else:
            for key, value in expected.items():
                if key not in actual:
                    failures.append(f"{path}/{key}: missing key")
                else:
                    compare_numeric(value, actual[key], f"{path}/{key}", failures)
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            failures.append(f"{path}: list shape mismatch")
        else:
            for i, value in enumerate(expected):
                compare_numeric(value, actual[i], f"{path}/{i}", failures)
    elif isinstance(expected, (int, float)) and not isinstance(expected, bool):
        if (not isinstance(actual, (int, float)) or isinstance(actual, bool)
                or not math.isfinite(float(actual))
                or not math.isclose(float(expected), float(actual),
                    rel_tol=0.0 if path == PEAK_LOCATION_PATH else 1e-9,
                    abs_tol=1e-4 if path == PEAK_LOCATION_PATH else 1e-12)):
            failures.append(f"{path}: {actual!r} != {expected!r}")
    # Human-readable status strings and environment metadata are not scientific predictions.
    return failures


def compare_run(run: Path) -> list[str]:
    failures = []
    for filename in ("cycle01.json", "dp_reproduction.json"):
        expected = json.loads((BASELINE / filename).read_text())
        actual = json.loads((run / "results" / filename).read_text())
        compare_numeric(expected, actual, filename, failures)
    import numpy as np
    for filename in ("negativity_vs_phase.csv", "dp_comparison.csv"):
        expected = np.genfromtxt(BASELINE / filename, delimiter=",", names=True)
        actual = np.genfromtxt(run / "results" / filename, delimiter=",", names=True)
        if expected.dtype.names != actual.dtype.names or expected.shape != actual.shape:
            failures.append(f"{filename}: columns or shape mismatch")
            continue
        for column in expected.dtype.names:
            if not np.allclose(expected[column], actual[column], rtol=1e-9, atol=1e-12):
                failures.append(f"{filename}/{column}: numerical difference exceeds tolerance")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path)
    args = parser.parse_args()
    failures = compare_run(args.run_directory.resolve())
    if failures:
        print("\n".join(failures))
        return 1
    print("PASS: all numeric JSON fields and both CSV datasets agree with Cycle 01.")
    print("Scientific predictions: rtol=1e-9, atol=1e-12. Flat numerical peak coordinate: atol=1e-4; peak height stays strictly compared.")
    print("Figure pixels and metadata are not compared.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
