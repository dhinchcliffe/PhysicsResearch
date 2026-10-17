# Project Gravity Witness

What realizable protocol, or combination of measurements, would distinguish low-energy quantum-gravity predictions from strong specified classical/hybrid alternatives after realistic uncertainty and theoretical assumptions are included?

Start with the [full research atlas](../../docs/atlas/2026-10-17-v0.2/atlas.md). For setup and every execution command, use the [repository README](../../README.md); commands are run from the repository root.

## Project contents

`src/gravity_witness/gw.py` implements the finite-dimensional two-mass baseline, phase invariants, dephasing, observables, calibrated readout and restricted KTM comparison. `dp.py` implements selected static Gaussian-smeared Diósi–Penrose dynamics and an independent Lindblad cross-check. Units and limits are documented in their docstrings.

`tests/` is the original 970-check research suite, relocated with import changes only. `scripts/` generates numbers and figures. `results/cycle01/` and `figures/cycle01/` preserve the original outputs; new runs go to the repository's ignored `build/` directory.

`notes/` preserves the original briefing, derivations, model audit, failure log and next gate. `sources.json` records actual source-audit depth, while `claims.json` distinguishes kinds of evidence. These retain historical filenames; resolve them using the [path map](../../provenance/migration/path-map.json).

`formal/` is a separate pinned Lean project. The original cycle did not run Lean. The formal checker and compiler logs determine subsequent status; neither Python tests nor this project index establish formal verification.
