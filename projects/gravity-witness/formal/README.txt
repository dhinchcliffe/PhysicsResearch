STATUS: DRAFT, NOT EXECUTED. Do not call these machine-verified proofs.
Target toolchain: Lean 4.19.0 with mathlib v4.19.0 (pinned release tags).
No dependency download or kernel check succeeded in this environment.
The theorem covers the nonzero upper-left-pivot factorization case, determinant
necessity, local-factor identity and additive phase cancellation. Other pivots,
normalization, complex norms and the sine/concurrence formula are not encoded.

When a networked Lean environment is available:
cd formal
lake update
lake env lean GravityWitness.lean

Capture actual compiler output, inspect assumptions and commit lake-manifest.json
before promoting any claim to FORMALLY VERIFIED. Do not silently weaken theorems
to pass the compiler. The physics of the assumed state is outside these lemmas.
