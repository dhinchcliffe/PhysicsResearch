# From a claim to evidence

## The director's reading loop

Begin with the atlas's briefing. Ask what changed, what it means, and what could make it wrong. Follow one worked example into the derivation and then the generating code. Review the strongest countermodel before approving a new direction.

## The evidence chain

A claim in the atlas should lead to a stable claim ID, a primary source and its exact assumptions, a derivation or implementation, a test or proof, and an actual execution record. These are separate objects; the existence of one does not substitute for the others.

For the main Cycle 01 example, follow the atlas's Lesson 2 to `projects/gravity-witness/notes/derivations.txt`, the phase and measurement functions in `src/gravity_witness/gw.py`, the tests in `tests/test_gw.py`, and the `phase_calibrated_readout` section in `results/cycle01/cycle01.json`.

For the harder countermodel, follow the source registry's S05 entry, `notes/model_audit.txt`, `src/gravity_witness/dp.py`, `tests/test_dp.py` and `results/cycle01/dp_reproduction.json`. The implementation reproduces specified dynamics; it does not establish that the model is a viable local classical mediator.

## Keep the three questions separate

Does the mathematics produce entanglement? Would the specified measurement reveal it under quantified noise? Would that observation identify gravity as quantum rather than expose another interaction, invalid assumption or nonviable countermodel?

Cycle 01 makes progress on the first two. Its next gate is the physical-constraint audit recorded in `notes/next_cycle.txt`. No repository migration or passing CI status advances that scientific gate automatically.

## A completed cycle

Preserve the readable briefing, revised definitions and figure, exact assumptions, source/claim records, code, fresh test reports, dependency versions, successful checks and failed approaches. Record an explicit continue/pivot/stop decision. An independent physicist's review is a different form of evidence from another AI pass.
