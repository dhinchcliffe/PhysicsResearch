PROJECT GRAVITY WITNESS
Cycle 01 / 17 October 2026 / research started with the director's approval.

PURPOSE
Identify experimentally distinguishable predictions of specified gravity models.
This package reproduces selected finite-dimensional calculations. It does not
report an experiment, an independently reviewed discovery, or a unified theory.

START HERE
notes/cycle01_brief.txt       Plain-language findings and limitations.
notes/derivations.txt         Assumptions, definitions and mathematical argument.
notes/model_audit.txt         Competing models and active literature disputes.
notes/next_cycle.txt          The next acceptance gate, not an unattended job.
claims.json / sources.json   Claim-level provenance and source audit depth.
results/cycle01.json         Computed baseline and calibrated readout.
results/dp_reproduction.json Published DP predictions independently implemented.
results/pytest.xml           Actual execution record: 970 test cases passed.
figures/                    Five figures generated from equations, not data.
formal/                     Lean proof draft; NOT kernel-checked.

REPRODUCE (from the repository root; Python 3.13 used here)
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.lock
bash tools/reproduce.sh

The tested environment is listed in results/environment.json. requirements.lock
pins direct and resolved runtime dependencies, but is not a hash-locked wheel
supply-chain manifest. Numeric tests have explicit tolerances. Figure byte hashes
may differ on another OS/backend even when numerical results agree.

VALIDATION BOUNDARIES
970 is a count of parameterized checks, not 970 theorems or independent reviews.
Two separate numerical implementations and symbolic identities cross-check
selected results. No external physicist reviewed this cycle. No experimental
data were collected. Apparatus viability and literature priority remain open.

STORAGE AND PUBLICATION
A local Git repository and export bundle preserve this cycle. The intended
private remote is dhinchcliffe/gravity-witness. It has NOT been created: the
connected GitHub action set has no repository-creation action. Do not describe
this package as pushed or hosted on GitHub. tools/publish_private.sh is an
explicit, user-controlled publishing option, not an action already performed.
No paper PDFs or third-party author code are redistributed in this package.

LIVING ATLAS
https://docs.google.com/document/d/1rkQ5z3phVVdCVBP6Obtn3HBA1U6YbQ9L78HwgeqdGAc
