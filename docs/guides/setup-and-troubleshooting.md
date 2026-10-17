# Setup and troubleshooting

## Python cannot be found

Install Python 3.13 for your operating system and ensure its virtual-environment support is available. The project intentionally uses the Cycle 01 package versions, not whichever versions happen to be current. Confirm the active interpreter with:

```bash
python --version
python -m pip --version
```

Both should refer to the intended virtual environment. The calculations do not require CUDA, a GPU, API keys or remote execution.

## A pinned package will not install

Read the first pip error. Check Python version, CPU architecture, network/DNS, available disk space and whether the platform has a compatible wheel. Do not remove version pins just to bypass the error. A changed environment must be recorded and scientifically revalidated. The repository's local migration run used preinstalled packages matching all pins; it did not reinstall them from the internet.

The version lock does not pin wheel hashes, the OS, BLAS or rendering fonts. Numerical comparison tolerances are explicit. Byte-identical plots across machines are not promised.

## `No module named gravity_witness`

Use the documented runners from the repository root. Pytest gets its source path from `pyproject.toml`; `tools/example.py` and `tools/reproduce.py` set the local import path themselves. Do not execute the project generator scripts from arbitrary directories without providing the appropriate source path and output directory.

## A reproduction destination already exists

Choose a new name or let the runner create a timestamped one. The runner intentionally refuses to overwrite an existing run and refuses destinations outside `build/`. The frozen baseline must never be replaced by a routine rerun.

## Tests or numeric comparisons fail

Read the new run's logs and XML report. Check whether the installed package versions match. Reduce to the smallest failing test. Inspect units and distinguish DP gap distances from point-Newton centre distances. Do not widen tolerances or delete tests without documenting a substantive reason.

## Lean or `lake` cannot be found

Follow the official Lean installation guide linked in the root README. On macOS/Linux, make the elan environment visible to the current shell:

```bash
source "$HOME/.elan/env"
```

On Windows, reopen the terminal after installing elan. An absent toolchain produces a blocked formal status, never a passing one.

## Mathlib cache or network fails

The first `--prepare` run needs external downloads. Keep the pinned Lean and mathlib release. A dependency failure is not a failed theorem, but it also does not establish the theorem. Save the status and log; retry preparation in a working network environment. Once resolved, review and commit the generated `lake-manifest.json` with the compiler evidence in a deliberate verification change.

## The atlas mentions an old repository

The copied Google Doc and original cycle records faithfully retain their historical text. The current repository README and migration record explain the change to PhysicsResearch. Do not silently edit the snapshot to make it look as though the original run had infrastructure it did not have.
