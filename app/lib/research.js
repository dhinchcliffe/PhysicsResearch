// Source-of-truth: committed frozen data, read at build time. Not live instrument readings.
import cycle from "../../projects/gravity-witness/results/cycle01/cycle01.json";
import dp from "../../projects/gravity-witness/results/cycle01/dp_reproduction.json";
import claimsFile from "../../projects/gravity-witness/claims.json";
import sourcesFile from "../../projects/gravity-witness/sources.json";
import feasibility from "../../projects/gravity-witness/results/cycle02/constraints.json";
import nextClaims from "../../projects/gravity-witness/results/cycle02/claims.json";
import nextSources from "../../projects/gravity-witness/results/cycle02/sources.json";

export const research = {
  cycle: cycle.cycle,
  recorded: cycle.date,
  testCount: cycle.code_checks.tests,
  failures: cycle.code_checks.failures,
  sourceCount: sourcesFile.sources.length + nextSources.sources.length,
  claimCount: claimsFile.claims.length + nextClaims.claims.length,
  openClaims: [...claimsFile.claims, ...nextClaims.claims].filter(x => x.status === "OPEN" || x.status === "DISPUTED").length,
  witness: {
    phase: cycle.illustrative_case.delta_rad,
    mass: cycle.illustrative_case.mass_a_kg,
    distance: cycle.illustrative_case.centre_distance_m,
    split: cycle.illustrative_case.path_split_m,
    time: cycle.illustrative_case.hold_time_s,
    lambda: cycle.phase_calibrated_readout.assumed_retention_lambda,
    score: cycle.phase_calibrated_readout.score_S,
    threshold: cycle.phase_calibrated_readout.threshold_retention_lambda,
    bound: cycle.phase_calibrated_readout.separable_bound,
  },
  dp: {negativity: dp.example.negativity_at_u_1, peak: dp.example.numerical_peak_negativity},
  feasibility: {phase: feasibility.cycle, nonOverlapFactor: feasibility.geometric_threshold.sigma_over_R_must_exceed, shieldFloor: feasibility.shield_caveat.universal_lower_edge, example: feasibility.scenarios.find(s=>Math.abs(s.sigma_m-10e-6)<1e-11) ?? null}
};
// Milestones are research gates, manually adjudicated from evidence; NOT a discovery percentage.
export const milestones = [
  {number:"01",title:"Define the question",state:"complete",description:"Charter, vocabulary and rival experimental approaches established.",evidence:"Research atlas v0.2"},
  {number:"02",title:"Reproduce the mathematics",state:"complete",description:"Four-branch phase model, entanglement readout and selected classical alternatives checked.",evidence:"Cycle 01 · Python & Lean"},
  {number:"03",title:"Confront physical constraints",state:"next",description:"Cycle 02: solid-sphere entanglement survives mathematically when σ≫R, but this example faces a major shield-clearance conflict. Apparatus viability remains unproven.",evidence:"Cycle 02 · Gate open"},
  {number:"04",title:"Design a discriminating test",state:"queued",description:"Compare full distributions at matching geometries, with realistic noise and nuisance channels.",evidence:"Pending constraints"},
  {number:"05",title:"Invite independent scrutiny",state:"queued",description:"Have specialists challenge assumptions, feasibility and the technical note.",evidence:"Not yet undertaken"}
];
