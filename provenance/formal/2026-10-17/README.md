# First recorded Lean kernel verification

On 17 October 2026 the independent GitHub-hosted workflow successfully installed Lean 4.19.0, resolved mathlib v4.19.0, built the project, checked `GravityWitness.lean` directly, and printed the axiom dependencies of all four named lemmas. No theorem statement or proof body was changed to obtain this result.

[Successful run](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022307768) · [Job](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022307768/job/117366387551)

The tested repository commit was `93c21ca5072560a51f91db2a9b92583d805bed48`. `status.json` is the actual runner-produced status, not a hand-written assertion of success. Its time field records the start of the check. The axiom audit completed and the artifact was uploaded by 09:48:04 UTC.

## Scope

Only four finite algebra statements are kernel-checked: factorization implies zero determinant; the converse for a nonzero upper-left pivot; determinant scaling under local factors; and cancellation of additive local phases. This does not establish the full concurrence identity, all pivot cases, physical model validity, the feasibility of an experiment, or a unified theory.

`compiler-excerpt.txt` preserves the concluding compiler output and all four axiom lists. Each lists only `propext`, `Classical.choice`, and `Quot.sound`; none lists `sorryAx`. These are Lean's foundational assumptions, not experimental assumptions.

The generated dependency resolution is now committed as [lake-manifest.json](../../../projects/gravity-witness/formal/lake-manifest.json). Its SHA-256 matches the runner status: `cca367447e512e9fb1e6bd24c08abc9f5b19236eafc13baca539d45ea8a622e9`.

The original downloadable workflow artifact is named `formal-evidence-93c21ca5072560a51f91db2a9b92583d805bed48`, ID `12097057060`, SHA-256 `8b10baf7159abc1fdc106bf00f3c5633ac7a360b36ed4b1324ea4337e7b5bd5d`. It also contains the full installation log and manifest; GitHub's artifact retention for this run is 30 days. The essential status, compiler conclusion, axiom dependencies and dependency resolution are preserved here in Git beyond that retention window.

The earlier local blocked report and the atlas's historical uncompiled-draft wording remain unchanged. They describe the earlier execution environment. This separate dated record establishes the subsequent verification and must not be used to retroactively change the historical account.
