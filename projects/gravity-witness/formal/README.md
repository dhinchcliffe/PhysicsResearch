# Formal algebra track

## Status and scope

The Cycle 01 file is a proof draft. Its four theorem statements cover determinant necessity, a nonzero-pivot factorization implication, local-factor scaling and additive phase cancellation. They do not prove the complete concurrence identity, the remaining pivot cases, any gravitational field theory, or apparatus feasibility.

`README.txt` preserves the original historical status. Current execution is reported by `tools/check_formal.py` and the separate formal CI job. Missing network/toolchain is **blocked**, rejected source is **failed**, and a successful build plus direct source check and axiom audit is **kernel_checked**. Do not infer a successful run from a workflow being present.

## Pinned environment

`lean-toolchain` selects Lean 4.19.0. `lakefile.toml` selects mathlib v4.19.0. The first prepared run creates `lake-manifest.json`; preserve that exact resolution alongside successful compiler evidence before promoting the proofs. Do not upgrade to an unpinned master branch.

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
