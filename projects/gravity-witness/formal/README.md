# Formal algebra track

## Status and scope

**The four original algebra lemmas were kernel-checked successfully on GitHub on 17 October 2026.** The recorded run built the pinned project, checked the source directly, and audited the axiom dependencies. See [the dated evidence](../../../provenance/formal/2026-10-17/README.md) and [the successful run](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022307768).

The four theorem statements cover determinant necessity, a nonzero-pivot factorization implication, local-factor scaling and additive phase cancellation. They do not prove the complete concurrence identity, the remaining pivot cases, any gravitational field theory, or apparatus feasibility.

`README.txt` and the comment in the unchanged source preserve the original historical draft status. Current execution is reported by `tools/check_formal.py` and the separate formal CI job. Missing network/toolchain is **blocked**, rejected source is **failed**, and a successful build plus direct source check and axiom audit is **kernel_checked**. Do not infer a successful run from a workflow merely being present.

## Pinned environment

`lean-toolchain` selects Lean 4.19.0. `lakefile.toml` selects mathlib v4.19.0. `lake-manifest.json` commits the exact dependency revisions produced by the successful build. Do not upgrade dependencies to unpinned branches.

Install elan according to the root README, then run from the repository root:

```bash
python tools/check_formal.py --prepare
```

Subsequent runs without dependency preparation:

```bash
python tools/check_formal.py
```

Inspect `build/formal/latest/status.json` and `lean.log`. The checker rejects explicit `sorry`, `admit`, project-specific `axiom` declarations, and `sorryAx` in the emitted axiom dependencies. The lint is a guardrail, not a replacement for Lean's kernel.

`AxiomAudit.lean` prints the dependencies of all four named lemmas. Review standard Lean foundational axioms separately from the physical assumptions that are not encoded by these statements.
