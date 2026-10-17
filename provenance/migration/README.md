# PhysicsResearch import and revalidation

Date: 17 October 2026. Destination: the existing private `dhinchcliffe/PhysicsResearch` repository.

## What is preserved

The original Cycle 01 ZIP and Git history bundle are byte-identical. The original manifest covers 37 tracked files. Original results, figures, notes, source records and claim records are frozen; their archived claims are not retrospectively upgraded.

The latest connected Google Doc was exported as PDF and Markdown. Both tabs and all four images are present. The GitHub-readable Markdown changes only image references; its narrative is unchanged. The source revision and export checksums are in `docs/atlas/2026-10-17-v0.2/snapshot.json`.

The user's original two-line PhysicsResearch README is retained in `original-repository-README.md`; its purpose statement is preserved in the new main README.

## What changed structurally

Science modules moved into `projects/gravity-witness/src/gravity_witness/`; tests and generator scripts gained their own directories. Import paths changed, and generators now accept an output directory supplied by the portable runner. The generator's infrastructure metadata names PhysicsResearch and does not claim that running a numerical script verifies GitHub or Lean status.

`path-map.json` records every original artifact's destination and content hashes. Repository tests compare the non-import syntax trees of both scientific modules and both research-test modules with their originals. No scientific formula or research-test assertion was changed by the move.

New cross-platform tools provide the small worked example, protected reproduction, numerical-baseline comparison, archive verification and a separate Lean attempt with explicit status.

## Actual local execution

The 970 research checks passed again with zero failures, errors or skips. `pytest.xml` and `pytest.txt` here are the fresh migration records, not copies of the old test run. Both generator scripts completed. `comparison.log` records agreement of the numerical JSON fields and both CSV datasets with `rtol=1e-9`, `atol=1e-12`.

`numerical-run.json` records the Python 3.13.5 runtime and installed package versions. All locked package versions matched the existing environment. DNS/network access was unavailable, so dependencies were **not freshly downloaded/reinstalled locally**. A clean-network install is a distinct CI check, not implied by the local test pass.

All 16 repository-tooling tests passed locally. `repository-tests.xml` records them. These are not 16 additional physics results. Artifact verification passed 69 preservation checks.

The local Lean attempt was blocked because `lake` was absent and the installer host could not be resolved. `formal-local-status.json` is deliberately not a kernel-success claim. Subsequent formal CI evidence must be consulted separately.

## Publication receipt

The import process writes `github-import.json` with the uploaded package checksum and actual GitHub Actions run URL when it succeeds. The receipt contains no download credentials. The preserved original Git bundle is not grafted onto the remote branch: it remains recoverable historical evidence, with no misleading ancestry claim.
