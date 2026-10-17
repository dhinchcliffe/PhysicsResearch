# Completed repository verification — 17 October 2026

The scientific source and permanent verification workflows were tested at commit `b6610cde5ffc1adc86e0ea7fa2aa71ebdb818d19`. Subsequent documentation updates do not change those tested sources.

## Numerical verification: passed

[Successful GitHub run](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022877499) · [Job](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022877499/job/117368030954)

A clean Ubuntu runner installed all 18 pinned Python dependencies under Python 3.13.16. `pip check` succeeded. All 69 preserved-artifact checks passed after the exact CSV-byte repair.

The downloaded JUnit records show 970 research checks and 17 repository checks, with zero failures, errors or skips in either suite: 987 numerical/software checks in total, not 987 mathematical proofs.

Both result generators completed. The comparison log states that all numeric JSON fields and both CSV datasets agree with the frozen Cycle 01 baseline at `rtol=1e-9`, `atol=1e-12`. Figure pixels and metadata are deliberately not treated as numerical results.

The numerical artifact was downloaded and its SHA-256 matched GitHub's reported digest: `40db8ef592dd4750aa8665d557d4eae6181600a7ae5cf8a8bdabf1865ed0ab5b`. Artifact ID: `12096723641`. The runner's `run.json` reports `status: passed`, start `2026-10-17T09:54:47.684448+00:00`, finish `2026-10-17T09:54:52.887609+00:00`.

The runner's `network_dependencies_reinstalled: false` describes the numerical script itself: it never installs packages. The preceding GitHub workflow step did install the locked dependencies. These are separate execution stages, not contradictory claims.

## Formal verification: passed

[Successful second GitHub run](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022877480) · [Job](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022877480/job/117368030701)

The pinned Lean 4.19.0 project passed again with the committed dependency manifest. The first successful run's actual runner status, compiler conclusion and all four axiom lists are preserved in [the dated formal record](../formal/2026-10-17/README.md).

Exactly four original finite algebra lemmas were checked. No `sorryAx` occurs in their audited dependencies; the reported foundational axioms are `propext`, `Classical.choice`, and `Quot.sound`. This is not a proof of experimental viability, the full concurrence identity, a gravitational field theory, or a unified theory.

## Source preservation

The original archive, original Git-history bundle, source registry, claim ledger, baseline numerical outputs and five figures are retained. The fresh native Google Docs PDF and Markdown exports include both tabs and four embedded images, with revision and checksums in [snapshot.json](../../docs/atlas/2026-10-17-v0.2/snapshot.json).

The CSV normalization defect and repair are recorded in [the clean-checkout audit](clean-checkout-audit.md). Hashes and scientific tests were not relaxed. Temporary import/repair workflows have been removed from the active branch; only the permanent numerical and formal verification workflows remain.

GitHub workflow artifacts have 30-day retention. The original research record and essential dated verification results are committed permanently. No repository-visibility change, new scientific claim, or unattended research schedule is implied by this migration.
