# Contributing to PhysicsResearch

This is a private, director-led research program. Changes should make the science easier to understand, reproduce and challenge—not merely increase the number of outputs.

## Before changing a model

Identify the affected claim ID, primary source, exact equation, model assumptions and intended domain. Keep mathematical prediction, interpretation of the mediator, and experimental viability distinct. Record discrepancies with the literature rather than silently reconciling them.

## A useful pull request

Explain the change in ordinary language. Include the claim IDs, changed assumptions, a worked example, the strongest counterargument, and the exact commands used to test it. Attach a fresh run record; inherited test output is not evidence of a new run.

Run the standard checks from the repository root:

```bash
python -m pytest -q
python tools/verify_artifacts.py
python tools/reproduce.py
```

For formal changes, also run:

```bash
python tools/check_formal.py
```

Do not weaken a theorem, insert an admission, suppress a failed check, or widen a tolerance merely to pass. Explain intentional changes to baselines in a separate reviewable decision. A new theorem needs its statement, assumptions, actual kernel output and axiom audit; a numerical cross-check is not a theorem.

## Records to preserve

Keep `projects/gravity-witness/results/cycle01/`, `figures/cycle01/`, the original archive and original manifest immutable. New runs go under ignored `build/`; accepted research cycles get their own named snapshot after review. Keep negative results and the failure log. Record scientific and software environment changes separately.

The claim and source registries use their original Cycle 01 path vocabulary. Consult `provenance/migration/path-map.json` when following those references. Do not edit historical records merely to remove past infrastructure failures.

## Data and permissions

No secrets, personal access tokens, unrelated user data, or unlicensed third-party papers/code belong in the repository. The original program remains private; publication and licensing require a separate decision. Do not change repository visibility or sharing as part of routine work.
