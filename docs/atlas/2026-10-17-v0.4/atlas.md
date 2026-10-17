# Cycle 02 — Physical constraints

# Project Gravity Witness

## Cycle 02 — From mathematics to physical constraints

Research atlas • Author-reviewed edition v0.4

17 October 2026 • Research directed by Dion Hinchcliffe • Gate 03 remains open

**Vision:** identify an observation that can distinguish low-energy quantum gravity from precisely specified classical or hybrid alternatives.

**Immediate goal:** determine whether the reproduced Diósi–Penrose entangling example can satisfy physical-size, shielding, force-law and noise constraints at the same time.

Reading route: begin with the findings below; use Cycle 01 for the measurement calculation and Charter & foundations for definitions, competing models and the research plan.

# The finding in five minutes

**The mathematical example survives a limited finite-size test, but we have not found a physically viable experiment.** Cycle 01 reproduced entanglement in a particular Gaussian-smeared Diósi–Penrose (DP) model. Cycle 02 asks whether real objects could be prepared, isolated and measured in that configuration. The answer depends on what the model’s smearing length means and on whether electromagnetic contamination can be controlled.

Two interpretations must be kept separate. If the smearing length σ is identified with the physical sphere radius R, the example requires overlapping objects and fails as a two-body geometry. If σ is an independent model parameter much larger than R, the spheres can be separate, and the tested finite-sphere extension retains an entangling onset.

The remaining obstacle is not a failed equation. It is the proposed experiment: in this fixed geometry, a centred conducting shield cannot be far from the surfaces relative to the quantum path split. That conflicts with the favourable shielding regime discussed in the source analysis. We have calculated the geometry, not the resulting decoherence rate. This is a serious feasibility warning, not a universal exclusion of DP experiments. \[S05, S20; GW-C013–C015\]

## What the evidence establishes

Checked within the model: 40 additional parameterized tests cover the uniform-sphere extension, non-overlap condition, force-ratio formulas and conversion to physical units. The original 970 Cycle 01 tests remain a separate suite. These are numerical and software checks, not experimental observations or 1,010 distinct theorems.

Still unresolved: a simultaneously achievable superposition, coherence duration, electromagnetic noise budget and allowed range of σ. Finite size alone does not remove the tested entangling onset when σ is sufficiently larger than R; that result does not establish laboratory feasibility.

Formal scope: four earlier algebra lemmas have subsequently passed Lean kernel verification. They concern determinant factorisation and local-phase cancellation, not the Cycle 02 physical-constraint arguments.

# Lesson 1 — Real spheres cannot overlap

R is the physical radius of each sphere. The parameter σ is the Gaussian gravitational smearing length: the spatial scale over which this model smooths the mass coupling. The symbol d denotes the minimum centre-to-centre distance across the four joint path combinations; L is each sphere’s left-to-right path separation.

These are the Trillo–Navascués DP conventions. In Cycle 01’s separate Newtonian example, d instead denotes the mean centre separation and s denotes the path split. In the present DP geometry, mean centre separation is d \+ L. Do not substitute one convention into the other.

The reproduced example fixes d \= 3σ/8 and L \= σ/8. Strict separation of rigid spheres requires d \> 2R, hence σ \> (16/3)R ≈ 5.33R. Equality would mean contact, not clearance. In particular, setting σ \= R makes the geometry impossible. This inequality applies to the specified configuration; it does not exclude every collapse model. \[GW-C013\]

Worked example: take two illustrative silica spheres, each of mass 10⁻¹⁴ kg and density 2,200 kg/m³. Their calculated physical radius is 1.03 µm. At σ \= 10 µm, d \= 3.75 µm, L \= 1.25 µm, and the minimum distance between solid surfaces is about 1.70 µm. Nothing overlaps — but that is not enough to perform a quantum interference experiment.

# Lesson 2 — A shield can also reveal the path

A conducting Faraday shield may prevent electric forces from being misidentified as gravity. But residual charges and dipoles can interact with their electrical images in that shield, allowing the environment to learn which path a mass followed. The resulting loss of interference is decoherence.

Consider an ideal, zero-thickness sheet centred in the narrowest gap. Its equal clearance from the nearest solid surfaces is (d − 2R)/2. Define the geometric ratio Q \= 2L/(d − 2R): path separation divided by that clearance. Every non-overlapping instance of our fixed example satisfies Q \> 2L/d \= 2/3.

The path displacement therefore cannot be much smaller than this surface clearance. That is in tension with the favourable regime discussed by Aspelmeyer. Q is our geometric screening diagnostic, not a measured decoherence factor or a universal pass/fail threshold. Finite screen thickness only reduces the available clearance; a shield-free arrangement would need a different, quantified way to suppress electromagnetic contamination. \[S20; GW-C015\]

For the σ=10 µm silica example, Q ≈ 1.475. Increasing σ makes physical separation easier, but never drives Q below its 2/3 geometric limit so long as L/d remains fixed.

## Figure C02-A — The shielding-clearance problem

![][image1]

Figure C02-A. Calculated geometric ratio Q for the fixed DP example. Increasing σ reduces Q toward 2/3, not toward zero. This is not a noise measurement. A physical calculation must include screen thickness, electrical response, residual charge and dipoles, surface defects and fluctuation spectra. Source: run\_constraints.py; GW-C015.

# Lesson 3 — Finite size does not settle the question

We replaced each point mass with a uniform solid sphere while retaining the same Gaussian smoothing. The sphere’s Fourier form factor, F(z) \= 3(sin z − z cos z)/z³, describes its spatial mass profile; z is a dimensionless wave-number–radius product. We then reconstructed the full 4 × 4 mass-density correlation matrix.

Our diagnostic is the initial slope of a partial-transpose eigenvalue, normalised by Gm²/(2ℏσ). A negative slope signals the onset of entanglement in this fixed-position model. It is not a measured rate from an apparatus. \[GW-C014\]

At R/σ \= 0, the normalised slope is −0.000191563996, reproducing the point-mass limit. At R/σ \= 0.10 it is −0.000191206279; at R/σ \= 0.18 it is −0.000190407305. All three are negative. Quadrature calculations at two different orders agree over the tested range.

The calculation does not include moving wave packets, preparation and trapping, internal or thermal noise, collisions, electromagnetic and Casimir forces, or readout. Its scope is the entangling onset in the stated static model.

The technical result is narrow but useful: replacing a point with a finite sphere does not, by itself, remove the tested DP entangling onset when σ can be substantially larger than R. Whether that interpretation and parameter range are physically allowed remains a separate question.

# Lesson 4 — Compare like with like

In this specific Gaussian-smoothed point-pair potential, the force ratio to Newton is erf(x) − (2x/√π)e^(−x²), with x=r/(2σ). The model yields only 0.4855% of an unsmeared Newton point-pair force at the nearest branch distance r \= 0.375σ, and 1.1323% at r \= 0.5σ.

The cited torsion-balance experiment reached a 52 µm surface separation between extended bodies and reported limits for Yukawa corrections. That is not the same calculation as our Gaussian-smoothed point-pair force. A valid constraint on σ requires integrating the Gaussian interaction over the actual attractor and detector, then comparing the predicted signal with the data and uncertainties. Our point-pair graph does not perform that fit and establishes no experimental exclusion interval. \[S25; GW-C016\]

## Figure C02-B — Conditional Gaussian force response

![][image2]

Figure C02-B. Calculated Gaussian-smoothed point-pair force relative to Newton’s point-pair force. A point-pair evaluation at 52 µm is only an illustration; it is not the response of the cited extended-body apparatus. No confidence limit on σ is extracted here. Source: run\_constraints.py; GW-C016.

# Lesson 5 — Time and noise must be considered together

The Cycle 01 static DP calculation reaches its numerical entanglement peak near u \= 407.93, where u \= Gm²t/(2ℏσ). Converting that dimensionless point for masses of 10⁻¹⁴ kg gives about 129 s at σ \= 10 µm, 258 s at 20 µm and 645 s at 50 µm.

These are time conversions of the original static point-mass model, not finite-sphere peak predictions, minimum measurement times or achieved coherence durations. This project has not established an apparatus operating point that combines the required mass, splitting, coherence and electromagnetic controls.

For the stated Gaussian white-noise, single-mass DP prescription, spontaneous heating is P \= Gℏm/(4√πσ³). Larger σ strongly suppresses this intrinsic heating term. It does not make thermal or environmental decoherence negligible, nor justify treating every composite body as one constituent. \[S24; GW-C018\]

The cited 2026 XENONnT result gives a model-conditional lower bound R₀ \> 4.5 × 10⁻¹⁰ m at 95% confidence for its Markovian DP prescription. That alone does not exclude the illustrative micrometre-scale σ values. The cutoff definitions and noise conventions must first be matched. A suggested upper cutoff based on macroscopic classicality is a theoretical criterion, not an empirical upper limit. Other smearing kernels are a further model choice. \[S23, S26, S27; GW-C017\]

# Illustrative parameter settings

Scenario: each sphere has mass 10⁻¹⁴ kg, density 2,200 kg/m³ and radius 1.03 µm. The fixed ratios are d/σ \= 3/8 and L/σ \= 1/8. Values are rounded from the committed calculation.

| σ (µm) | d (µm) | L (µm) | Spheres | Q | Peak t (s) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 5 | 1.875 | 0.625 | Overlap | — | 64.5 |
| 10 | 3.75 | 1.25 | Separate | 1.475 | 128.9 |
| 20 | 7.50 | 2.50 | Separate | 0.918 | 257.8 |
| 50 | 18.75 | 6.25 | Separate | 0.749 | 644.5 |

The last column converts the original static point-mass peak at u ≈ 407.93 into seconds. It is not a finite-sphere prediction or a required minimum measurement time. No row is an experimentally certified operating point.

# How the research director can help

The most valuable action is to arrange a thirty-minute technical review with a researcher actively developing gravity-induced-entanglement (GIE) experiments. Ask for simultaneous demonstrated numbers—not optimistic separate projections—for mass and material, coherent splitting L, achieved coherence time, minimum centre separation, available electromagnetic shield thickness/clearance, and noise from charge, dipoles, vibration and thermal photons.

Three review questions: (1) Can any viable shielding approach accommodate L/d≈1/3 without fatal path information? (2) Can an experimentally validated short-range-gravity response limit the Gaussian σ of this exact DP model rather than a Yukawa proxy? (3) Are there published apparatus operating points at which the mass, splitting and coherence time are achieved together?

The Cycle 02 note identifies Markus Aspelmeyer, David Trillo and Miguel Navascués as potential reviewers through the cited literature. No outreach has been sent. The request should be for a critique of the model assumptions and access to relevant apparatus-response or noise data, not an endorsement of a discovery.

# Gate decision and next work

Gate 03 remains open. The fixed inline example fails geometrically if σ \= R; allowing a larger independent σ avoids overlap but leaves a serious shielding concern. We have neither a certified surviving experimental window nor a general exclusion of DP models.

The next work is an electrostatic decoherence calculation with realistic screen and charge properties, a Gaussian-interaction fit to the extended short-range-gravity apparatus, and centre-of-mass wave-packet dynamics with thermal noise. Only then should surviving models be compared through full measurement distributions in the same geometry. Transverse paths, shield-free arrangements and the other experiment families remain alternatives.

# Reproduction and source record

Private repo: https\://github.com/dhinchcliffe/PhysicsResearch/tree/main/projects/gravity-witness

Reading note: projects/gravity-witness/notes/cycle02\_constraints.md

Python: python \-m pytest \-q projects/gravity-witness/tests/test\_constraints.py

Regenerate: PYTHONPATH=projects/gravity-witness/src python projects/gravity-witness/scripts/run\_constraints.py

## Cycle 02 source register

[\[S05\] Trillo & Navascués (2025). The Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement. Physical Review D 111, L121101. Selected model and geometry: https\://arxiv.org/pdf/2411.02287v](https://arxiv.org/pdf/2411.02287v2)2

[\[S20\] Aspelmeyer (2026). Quantum entanglement by gravity as tests of gravitational collapse models à la Diósi and Penrose. Physical-size, shielding and σ interpretation: https\://doi.org/10.5802/crphys.27](https://doi.org/10.5802/crphys.270)0

[\[S23\] XENONnT Collaboration (2026). Challenging Spontaneous Quantum Collapse with the XENONnT Dark Matter Detector. Model-conditional cutoff bound: https\://doi.org/10.1103/2jm3-497](https://doi.org/10.1103/2jm3-4976)6

[\[S24\] Vinante & Ulbricht (2021). Gravity-related collapse of the wave function and spontaneous heating: revisiting the experimental bounds. Gaussian heating equation: https\://arxiv.org/abs/2109.1498](https://arxiv.org/abs/2109.14980)0

[\[S25\] Lee et al. (2020). New Test of the Gravitational 1/r² Law at Separations down to 52 µm. Extended-body experiment, not a direct Gaussian σ bound: https\://doi.org/10.1103/PhysRevLett.124.10110](https://doi.org/10.1103/PhysRevLett.124.101101)1

[\[S26\] Piccione et al. (2026). Diffusion minimization via optimal smearing in collapse and hybrid classical-quantum gravitational models. Abstract screened; no alternative kernel reproduced: https\://doi.org/10.1103/h74z-zvf](https://doi.org/10.1103/h74z-zvfv)v

[\[S27\] Figurato et al. (2024). On the effectiveness of the collapse in the Diósi–Penrose model. Conditional classicality criterion, not an experimental upper bound: https\://doi.org/10.1088/1367-2630/ad8c7](https://doi.org/10.1088/1367-2630/ad8c77)7

[Verification record: the separate numerical workflow checks the original 970 tests and the 40 Cycle 02 tests. https\://github.com/dhinchcliffe/PhysicsResearch/actions/runs/3903934989](https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39039349892)2

[Formal evidence: four earlier algebra lemmas, with their exact scope and compiler output. https\://github.com/dhinchcliffe/PhysicsResearch/blob/main/provenance/formal/2026-10-17/README.m](https://github.com/dhinchcliffe/PhysicsResearch/blob/main/provenance/formal/2026-10-17/README.md)d

Source and claim identifiers retain the project numbering. The Cycle 02 extensions are under projects/gravity-witness/results/cycle02/. Inclusion in a registry does not imply every equation or experimental dataset has been independently reproduced.

Edition record: v0.3 added the Cycle 02 calculations and figures. This v0.4 author pass clarifies assumptions, notation, evidence status and source links; it adds no new numerical result. Frozen Cycle 01 and Cycle 02 research artifacts remain unchanged.

This is a reproducible modelling audit, not an experimental result or a claim that a laboratory can operate at the illustrative parameters.

# Cycle 01 — Results & learning

# Cycle 01 — From question to measurement

## Verified mathematical foundations • Original results, 17 October 2026

# The mathematical foundation

Cycle 01 established a checked two-mass calculation, a three-setting entanglement readout and two contrasting comparison models. One cannot entangle the specified input in the modelled regime; the other can. This section preserves that mathematical foundation. The preceding Cycle 02 section reports the subsequent physical-constraints audit and the still-open feasibility gate.

Status: reproduction and preliminary measurement design. The 970 passing Cycle 01 checks are numerical and software tests, not 970 proofs. Four narrow algebra lemmas were subsequently kernel-verified in Lean. No new physical discovery, apparatus demonstration, discriminator against all viable alternatives or independent physics review is claimed.

A correction matters. The initial charter treated the Aziz–Howl classical-gravity entanglement claim too confidently. Direct rebuttals contest its dynamics and/or attribute the effect to quantum matter exchange. The conditional local-mediator witness has not simply been overturned. We will keep the prediction, its assumptions and its physical interpretation separate. \[S04, S14, S15, S19, S22\]

The most useful result for your oversight is that the theory now ends in a measurable score, not just an impressive equation. In an explicitly idealized example, that score is 1.200 versus a separable-state ceiling of 1\. The assumed noise performance has not been achieved or validated; it tells us what the experiment would need to preserve.

Read the next three lessons to understand the score, the competing models and the two interpretive traps. Full derivations, source audits, failure records and code are preserved in the private PhysicsResearch repository; the original Cycle 01 archive remains unchanged.

# Lesson 1 — What is changing in the four paths?

Imagine two quantum wave patterns, each with a left and a right branch. There are four joint alternatives: LL, LR, RL and RR. Gravity changes the angle, or phase, of each alternative. Phase is like a hand on a clock: a common rotation changes no relative reading, but a difference between clocks changes their relationship. The analogy describes phase only; ordinary clocks are not entangled quantum systems.

The joint phase is Δ \= φ\_LL \+ φ\_RR − φ\_LR − φ\_RL. A phase that belongs only to A, only to B, or to all four alternatives cancels. In the ideal equally weighted state, concurrence C \= |sin(Δ/2)|. Here C is an entanglement measure from 0 to 1\. Negativity N is another measure, from 0 to 0.5 for two qubits; in this pure-state example N \= C/2. \[S01, S16–S18; reproduced in gw.py\]

Worked example: assume two point masses of 10⁻¹⁴ kg, centre separation d \= 450 micrometres, branch splitting s \= 250 micrometres, and a 2.5-second static hold. The four distances are 450, 700, 200 and 450 micrometres. The calculation gives Δ \= −0.313934 radians, C \= 0.156323 and N \= 0.078162. These are illustrative inputs, not an experimental achievement or a full interferometer simulation.

A useful surprise: all four path populations remain 25%. Counting which path each mass occupies would miss this entanglement. We must recombine or rotate the quantum states and measure the right correlations.

# Lesson 2 — The actual measurement score

Use fresh prepared pairs for three measurement settings: XX, YY and ZZ, after calibrated local rotations. X, Y and Z mean perpendicular spin measurement axes. Each spin measurement returns \+1 or −1. A correlation such as ⟨XX⟩ is the average product of the two outcomes in that setting.

Compute S \= ⟨XX⟩ − ⟨YY⟩ \+ ⟨ZZ⟩. Every separable two-qubit state satisfies S ≤ 1 under these trusted-measurement assumptions. A separable state is a mixture of independent states; it may still have ordinary correlations. The bound follows from the geometry of the two local spin vectors and survives mixing. This is a standard entanglement witness in suitable local frames, not a new Bell test or a device-independent proof.

For our example, assume independent dephasing retains λ \= 0.95 of each local branch coherence. Then S \= 1.199515 and N \= 0.049879. The code supplies all four outcome probabilities for each setting. In this particular state/noise family, S \= λ² \+ 2λ|sin(Δ/2)|. The threshold is λ \= 0.855821, not a universal coherence requirement.

An observed S \> 1 would establish entanglement only after accounting for statistical and measurement errors. It would not establish that gravity caused it. Initial entanglement, electromagnetic coupling, quantum matter exchange, unwanted selection of outcomes, and spin/readout artifacts must be independently excluded or bounded.

![][image3]

*Figure C01-A. Calculated readout versus assumed noise-channel retention for the 2.5-second example. The point at 0.95 is an assumption, not measured performance. Generated by run\_cycle01.py; claim GW-C003.*

## What would count as evidence?

A preliminary protocol is now specified: prepare independently, allow an interaction for a prescribed time, apply calibrated local rotations, collect the three joint-outcome distributions, and compare the score with its separable bound. Repeat over preselected times and geometries while collecting matched controls. No postselection or favorable parameter changes after looking at the result.

The archive includes a conservative sampling example: 3,968 prepared pairs per setting would suffice under its stated independent-trial, fixed-sample and bounded-bias assumptions. This is not a prediction of laboratory time or feasibility. A real noise budget and a guaranteed implemented signal are missing. We will not convert a toy statistical bound into an apparatus promise.

# Lesson 3 — An easy opponent and a harder one

The Kafri–Taylor–Milburn model represents gravity through measurement and classical feedback. Its source equation couples the force to enough decoherence to prevent entanglement in our static two-branch restriction. We reproduce that behavior analytically and numerically. It is a useful benchmark, not the strongest currently viable alternative; particular pairwise extensions already face experimental constraints. \[S02, S21\]

The harder comparison is the Gaussian-smeared Diósi–Penrose model studied by Trillo and Navascués. We implemented its correlated noise rather than substituting independent noise. The calculation reproduces the published limiting distance ratios 0.850872 and 2.210928 and an example that does entangle. A separate Lindblad implementation agrees with the direct evolution. \[S05; dp.py and test\_dp.py\]

This does not establish a viable classical-gravity loophole. The interpretation as local classical mediation is disputed, and the example is not certified experimentally feasible. Cycle 02 has now tested finite size and simple geometric constraints: the finite-sphere onset persists for the tested ratios, but the fixed arrangement raises a substantial shielding concern. Apparatus-specific decoherence and force-law exclusions remain uncalculated. \[S08, S20; GW-C013–C018\]

![][image4]

*Figure C01-B. The specified DP dynamics can entangle, but not like a noiseless evolution with the SAME softened gravitational Hamiltonian. Time is dimensionless, u \= Gm²t/(2ℏσ). This is not a comparison with point-Newton gravity at unmatched coupling. Generated by run\_dp.py; claim GW-C006.*

# Two traps the research must avoid

TRAP 1: Inconsistent approximations. The frequently useful small-splitting approximation gives a joint phase smaller than the exact point-Newton result by the fraction (s/d)². Our illustrative 250/450 geometry therefore has a 30.9% approximation error. Comparing an exact quantum calculation with an approximate classical one could manufacture an apparent difference. At s/d \= 0.1, the error is 1%. This is an elementary guardrail we derived, not a new discovery or an error attributed to the original papers.

![][image5]

*Figure C01-C. Exact relative error of the quadratic inline phase approximation. A fair comparison needs a shared accuracy regime or consistently exact models. Generated by run\_cycle01.py; claim GW-C004.*

TRAP 2: Mistaking lost interference for environmental noise. For the stated family, final single-particle visibility is V \= λ|cos(Δ/2)|, not λ. At Δ \= π it vanishes even with no environmental decoherence, because the masses are entangled. A separate matched control is needed to identify noise retention. That control's physical validity must also be tested. \[Derived and numerically cross-checked; GW-C011\]

# What has actually been checked?

970 parameterized tests pass with zero failures, errors or skips. Checks cover pure-state identities, local-phase invariance, partial-transpose eigenvalues, unequal dephasing, separable negative controls, independent matrix-exponential implementations, density-matrix validity, and selected DP numerical limits. SymPy checks selected exact algebra; a 60-digit scalar calculation checks a DP onset value. These are cross-checks within this project, not external expert replication.

The original failure log retains library, rounding, approximation and access issues. Lean could not be installed during the initial local run. Subsequent GitHub-hosted verification with Lean 4.19.0 and pinned mathlib checked four lemmas: factorisation implies zero determinant; a converse with a nonzero upper-left pivot; determinant scaling under local factors; and cancellation of local additive phases.

That verification does not establish the full concurrence identity, every factorisation case, any gravitational field theory or experimental feasibility. The dated compiler evidence is preserved separately from the historical uncompiled draft.

The current answer to our research question is still conditional: we have a concrete readout and checked model comparisons, but not yet a realizable protocol that robustly excludes the strongest viable alternatives. “Viable” must be earned by an independent constraint audit, not granted because a model produces a graph.

# The handoff to physical constraints

The physical-constraints audit requested after Cycle 01 is now reported in Cycle 02\. Its feasibility gate remains open. The next stage is to bound the actual shielding and environmental noise, interpret the relevant force measurements in the same model, and compare full distributions only for surviving, matched apparatus configurations. The gravitational-noise/coherence and optical cross-correlation tracks remain open.

For your own check: Why do four equal path counts not rule out entanglement? Why can a score above 1 establish entanglement without identifying gravity as its cause? Why is the DP model's mathematically entangling example not automatically an experimentally viable counterexample? Why is final visibility not a direct measure of environmental noise?

# Code, provenance and continuity

The original Cycle 01 archive contains 37 tracked files, including five figures and the then-uncompiled Lean draft, with a Git-history bundle and SHA-256 manifest. Its local commit was ea86abd353217f9c65a8b36a1945573ff8f1a796. These frozen artifacts preserve the state of that initial run; they are not the current repository inventory or verification status.

[Private research archive: gravity-witness-cycle01.zip](https://drive.google.com/file/d/1tiHsjSg-f1lVPt6nYH0l1RRkcNzBjGwa/view?usp=drivesdk)

Current record: dhinchcliffe/PhysicsResearch is the private GitHub repository. It preserves the original archive, subsequent Lean verification, Cycle 02 calculations and the dashboard. Earlier statements about an unavailable remote describe the initial run, not the present project. The frozen v0.2 atlas remains available for historical context.

# Primary sources for this cycle

Source IDs retain the charter's numbering. The archive's sources.json records what was actually read or reproduced; a listed paper is not automatically an audited result.

[S01 — Bose et al., 2017: branch-phase experiment framework.](https://arxiv.org/abs/1707.06050)

[S02 — Kafri, Taylor and Milburn, 2014: classical-channel benchmark.](https://arxiv.org/abs/1401.0946)

[S05 — Trillo and Navascués, 2025, arXiv v2: selected DP equations reproduced.](https://arxiv.org/pdf/2411.02287v2)

[S08 — Feng, Vedral and Marletto, 2026: locality challenge to collapse-model interpretation.](https://doi.org/10.1103/83rl-nygv)

[S14 — Gundhi, Infantino and Bassi, 2026: direct challenge to Aziz–Howl; version-access limits recorded.](https://arxiv.org/abs/2604.19696)

[S15 — Tibau Vidal and Iyer, 2026: matter-exchange and subsystem interpretation.](https://arxiv.org/html/2607.03429v1)

S16 — Wootters (1998). Entanglement of Formation of an Arbitrary State of Two Qubits. https\://arxiv.org/abs/quant-ph/9709029

S17 — Horodecki, Horodecki & Horodecki (1996). Separability of Mixed States: Necessary and Sufficient Conditions. https\://arxiv.org/abs/quant-ph/9605038

S18 — Peres (1996). Separability Criterion for Density Matrices. https\://arxiv.org/abs/quant-ph/9604005

[S19 — Marletto and Vedral, 2017: conditional mediator witness.](https://arxiv.org/abs/1707.06036)

[S20 — Aspelmeyer (2026): physical-size and shielding arguments inform Cycle 02; experiment-specific noise and exclusion calculations remain open.](https://comptes-rendus.academie-sciences.fr/physique/articles/10.5802/crphys.270/)

[S21 — Altamirano et al.: constraints on a pairwise local classical channel.](https://arxiv.org/abs/1612.07735)

[S22 — Marletto, Oppenheim, Vedral and Wilson, 2025: direct rebuttal to the classical-mediator interpretation.](https://arxiv.org/abs/2511.07348)

# Change record

2026-10-17 | v0.2. Charter approved; Cycle 01 executed. Added checked calculations and illustrated learning notes, preserved the charter and original diagram, corrected the overstated classical-gravity claim, and recorded infrastructure and scientific limits. No novelty or experimental-success claim.

# Charter & foundations

# PROJECT GRAVITY WITNESS

## An explanatory research atlas and experimental-discriminator program

Research atlas v0.4 • 17 October 2026 • Charter approved; Cycle 01 reproduced; initial Cycle 02 constraint audit completed. Start with Cycle 02 for current findings. The physical-feasibility gate remains open.

# READ THIS FIRST

## The question in one minute

Gravity, as Einstein describes it, is the geometry of spacetime. Quantum mechanics describes particles and fields with superposition, interference and entanglement. Both theories work spectacularly in their domains. We do not yet know whether gravity itself must obey quantum rules. An experiment can help by comparing precisely specified models, rather than attempting to prove every imaginable theory wrong.

The motivating experiment is almost childlike in its structure: prepare each of two tiny masses so that it can follow a LEFT or a RIGHT path in quantum superposition. Let the masses interact while carefully suppressing non-gravitational forces. Then recombine the paths and measure correlations. Four path combinations experience four different gravitational distances. Their quantum phases can encode entanglement.

CORRECTION / DISPUTED: Some proposed classical or hybrid models predict entanglement, but their locality assumptions, physical viability and interpretation are contested. In particular, the Aziz–Howl claim has direct technical rebuttals. The conditional local-mediator witness has not simply been overturned. Our task is to compare precisely specified predictions while auditing initial separability, other quantum channels, subsystem definitions and experimental constraints. See the Cycle 01 tab and sources S04–S08, S14, S15, S19, S20 and S22.

## The north-star question

What realizable experimental protocol—or coordinated set of measurements—would distinguish the predictions of low-energy quantized gravity from strong, explicitly defined classical-gravity/quantum-matter alternatives, after realistic noise, confounders and theoretical assumptions are included?

The target is a testable discriminator: a protocol whose observable predictions separate specified models, with derivations, loopholes, parameter ranges and limits of inference made explicit. The current work does not claim a unified theory.

## How to read this atlas

The atlas develops concepts through intuition, an analogy where useful, a precise definition, a worked example and a challenge to the interpretation. The claim ledgers distinguish reproduced results, model extensions, disputed interpretations and open questions. A numerical check, a formal algebra proof and an experimental observation are different kinds of evidence; none should be silently substituted for another.

## Figure 1 — the thought experiment

![][image6]

Figure 1\. A conceptual—not-to-scale—view of the four branch distances and three kinds of observables. Initial versions of this document will use original, reproducible figures; every subsequent major result gets a diagram with units and a link to its generating code.

# THE ESSENTIAL VOCABULARY

Classical gravitational field. A field described by ordinary numbers (for example a spacetime metric), rather than a quantum superposition of field states. Classical does NOT necessarily mean noiseless, deterministic, or compatible with every intuitive notion of locality.

Quantum gravitational field. A gravitational field with genuinely quantum degrees of freedom; the weak-field, low-energy baseline can be treated in perturbative quantum theory without requiring a complete theory of the Planck regime.

Superposition. A quantum state with amplitudes for multiple alternatives, such as LEFT and RIGHT, capable of interfering. This is not a mass literally chopped into two pieces.

Entanglement. Two quantum systems are entangled if their shared state cannot be expressed as a separable combination of independent states. A correlation alone is not enough: classically correlated objects can share information without entanglement.

Phase. The angle of a complex quantum amplitude. Relative phase differences change interference and can create entanglement when they depend jointly on both masses' positions.

Coherence / decoherence. Coherence is the preservation of relative quantum phases; decoherence is their loss through interaction or averaging over uncontrolled degrees of freedom. Reduced visibility can arise for many non-gravitational reasons.

Interferometer. An apparatus that splits and recombines alternative paths, turning phase changes into measurable differences. A Stern–Gerlach apparatus can couple a spin state to alternative paths; a Michelson interferometer uses optical paths.

Mediator. The mechanism that transmits an interaction between systems. “Gravity creates entanglement” and “the gravitational FIELD must be quantum” are different claims unless the mediator's allowed operations are specified.

LOCC / locality. Local operations and classical communication cannot create entanglement from an initially separable state. However, the information-theoretic sense of locality in this theorem is not identical to spatiotemporal locality. This distinction is central to the 2025–2026 disagreement. \[S06–S07\]

Backreaction. The effect of quantum matter on the gravitational field that in turn acts on matter. A viable hybrid theory must specify this interaction, not only gravity acting on a prescribed quantum system.

Stochasticity / diffusion. Random behavior governed by probabilities, including possible fluctuations of spacetime or the motion of matter. An otherwise-classical gravity theory may imply extra diffusion or decoherence.

Discriminator. An observable or combination of observables for which competing models predict measurably different distributions after uncertainties and nuisance parameters are considered.

# THE CANONICAL TWO-MASS EXAMPLE

## Intuition: four possible worlds, one shared experiment

Mass A can be at L or R, and mass B can be at L or R. The two-mass system has four joint alternatives: LL, LR, RL and RR. Each pair has its own separation dᵢⱼ. Gravity acts differently at different distances, so each alternative acquires a different phase over a duration t. After recombination, quantum spin correlations can reveal whether the two systems were entangled.

## A small piece of mathematics

Under an idealized Newtonian weak-field model with sharply localized branches and equal masses m, an interaction-dependent branch phase has magnitude φᵢⱼ \= G m² t / (ℏ dᵢⱼ). Here G is Newton’s gravitational constant, ℏ is the reduced Planck constant, t is interaction time and dᵢⱼ is branch separation. This expression by itself is a toy-model phase, not a complete experimental prediction. \[S01, S04\]

The part that matters for two-particle entanglement is Δφ \= φ\_LL \+ φ\_RR − φ\_LR − φ\_RL. In an ideal pure, equally weighted two-qubit state with only branch-dependent phases, the concurrence is C \= |sin(Δφ/2)|. C \= 0 means no entanglement; C \= 1 is maximal entanglement. A common phase that affects all four branches equally cancels. Four supporting determinant and local-phase lemmas have been checked in Lean; the full concurrence formula has not been formalised here.

Worked example: if Δφ \= 0, there is no entanglement in this toy state. If Δφ \= π, C \= 1\. In a realistic apparatus, the branches are wave packets rather than mathematical points; spin-readout visibility, decoherence, thermal motion and unintended electromagnetic coupling complicate the interpretation.

First challenge question: Could an apparent correlation come from charge, magnetic fields or shared preparation noise rather than gravity? Second: If a classical-gravity model produces nonzero C through quantum matter, what else can we measure to tell it apart?

# COMPETING THEORIES — FIRST MODEL REGISTRY

M0 | Quantized weak-field gravity (baseline). A low-energy quantum interaction model predicts branch-dependent phases and potentially gravity-mediated entanglement in appropriate preparations. This is NOT a complete ultraviolet theory of quantum gravity. Track all approximations.

M1 | Classical measurement-and-feedback channel (Kafri–Taylor–Milburn). Gravity is represented as classical communication, with associated decoherence and heating. Such a channel cannot create entanglement from an initially separable input under its assumptions. Test its model-specific noise tradeoffs. \[S02\]

M2 | Mean-field semiclassical gravity / Schrödinger–Newton. Quantum matter interacts with a field sourced by an expectation value. State-dependent dynamics may produce optical cross-correlations distinguishable in a specially designed interferometer. Test that specific model rather than all classical gravity. \[S10\]

M3 | Stochastic classical-quantum gravity (Oppenheim and related work). Classical spacetime couples to quantum matter through probabilistic dynamics. Predicts characteristic relationships involving decoherence, metric fluctuations and diffusion; realizations and consistency constraints matter. \[S03, S09\]

M4 | Diósi–Penrose-type collapse dynamics. Reproduced within a limited static model. Cycle 01 implements selected Gaussian-smeared dynamics and an entangling example. Cycle 02 retains an entangling onset in tested finite-sphere extensions, derives a non-overlap condition and identifies a shielding-clearance concern. Neither local classical mediation nor experimental viability is established. \[S05, S08, S20; GW-C013–C018\]

M5 | Classical gravitational field with QFT matter (Aziz–Howl). DISPUTED, not an established viable counterexample. The Nature paper claims entanglement with classical gravity; direct rebuttals challenge the calculation and/or identify quantum matter exchange rather than gravity as its mediator. Full QFT calculations have not been reproduced in this project. Audit subsystem partition, retained amplitudes, matter propagation and postselection before using this model. \[S04, S14, S15, S22\]

MODEL AUDIT RULE. For each model record the exact state space and dynamics, fields treated as classical/quantum, assumptions about locality, complete positivity, no-signaling and conservation, adjustable parameters, empirical constraints, and explicit predictions for every measurable quantity. Do not call a model viable merely because it appears in a paper.

# Three experiment families — the comparison programme

## Candidate A | Two masses, one gravitational interaction, several readouts

Preparation: independent spatial superpositions of two small masses. Readouts: spin correlations or another entanglement witness, single-particle coherence/visibility, heating and environmental noise. Perturbations: vary mass m, minimum branch separation d, superposition size Δx and interaction time t. Controls: shielding, charge neutralization, electromagnetic and Casimir–Polder forces, spin-pulse artifacts, vibration, and uncorrelated controls. Compare models at the same settings; identify regions where the quantum signal is resolvable and specified classical signals are not.

## Candidate B | Metric diffusion versus loss of coherence

The question: Must a model that keeps spacetime classical predict a relationship between additional fluctuations and loss of matter-wave coherence? Observable families can include displacement or strain-noise spectra and coherence-loss bounds. These need not be measurable on one apparatus. Investigate whether jointly available observations already rule out parameter ranges. Recent 2026 work derives strain spectra for several classical-quantum models. \[S03, S09\]

## Candidate C | Schrödinger–Newton optical cross-correlations

A January 2026 Physical Review D proposal uses a Michelson-type interferometer to test correlations between common and differential mirror motion expected under a specific semiclassical evolution. Reported feasibility is a model calculation with stated cryogenic and squeezed-light assumptions, not a demonstrated experiment or universal classical-gravity exclusion. \[S10\]

Experimental feasibility reality check. The 2025 EU-supported CLOSEtoQG project report describes why preparing picogram-scale masses in micrometre-scale spatial superpositions with roughly second-scale coherence is still an enormous challenge. Our first eight weeks are a theoretical and computational program—not an assertion that we can build this apparatus or collect new physical data. \[S11\]

Two 2026 alternatives belong in the experiment scan: paired atom interferometers that avoid some highly nonclassical massive states \[S12\], and mechanically constrained motions that may relax free-fall requirements under stated short-time assumptions \[S13\]. These proposals could change which apparatus offers the strongest near-term route.

Quantitative discrimination rule. For every candidate, specify the entire predicted measurement distribution P(y | model, parameters, nuisance noise), not just a slogan or a single expected mean. A hypothetical difference of 0.10 versus 0.13 in a measured correlation would not discriminate models if the uncertainty is 0.20; a large separation compared with validated noise might. Optimize worst-case model separation over credible nuisance-parameter ranges, report the models that remain degenerate, and preregister design criteria before searching for favorable settings.

Selection gate. Score only after reproduction against identical criteria: (i) distinct predictions relative to known alternatives; (ii) physical feasibility/noise controls; (iii) mathematical tractability; (iv) proximity to existing apparatus or public observations; (v) potential genuinely new result. No prior commitment to one candidate.

# THE EVIDENCE AND INFERENCE LADDER

Level 0 — Mathematical exercise: an equation or simulation is internally consistent; it may still not describe nature.

Level 1 — Reproduction: published analytical and numerical results match within stated domains and uncertainty.

Level 2 — Discrimination: named models differ for a specified observable under a specified set of assumptions and parameter values.

Level 3 — Experimental proposal: the difference survives validated nuisance models, quantified feasibility and available measurement precision.

Level 4 — Empirical inference: observation rules out specific models or parameter ranges at a stated confidence/likelihood level.

Level 5 — Fundamental claim: inference that gravity has nonclassical degrees of freedom requires the additional assumptions to be explicit; none of Levels 0–4 alone establishes a complete theory unifying gravity and quantum mechanics.

# WORKING ARCHITECTURE — ONE NARRATIVE, ONE AUDIT TRAIL

Google Docs: THIS atlas is the readable source of context. Keep a short synopsis, a glossary, diagrams, examples, model comparisons, a chronological learning narrative, and a decision log. Never allow a 100-page undifferentiated document: expand detailed papers as linked annexes when needed.

Code record: the private dhinchcliffe/PhysicsResearch repository preserves Python models, tests, figures, numerical outputs, claim and source ledgers, the original archive and dated Lean verification. Cycle 02 extends the record without overwriting Cycle 01\. Versioned atlas snapshots belong under docs/atlas/; the readable Google Doc remains the living narrative.

Python: NumPy/SciPy/SymPy, unit tests, parameter sweeps, uncertainty propagation, plotted observable distributions and data provenance; use pinned environments and deterministic random seeds. Avoid claiming experimental precision from an idealized simulation.

Lean 4 \+ mathlib: four narrow algebra lemmas are now kernel-verified with the pinned toolchain. The proved converse uses a nonzero upper-left pivot; it is not a complete treatment of every case. Further targets must state their assumptions and exact scope. Formalisation of the full concurrence identity, quantum field theory, general relativity and apparatus physics is not claimed.

Review protocol: one solver drafts; a distinct adversarial pass searches for counterexamples, missing terms, invalid limiting cases, dimensional inconsistencies and paper mismatches; computational tests and/or formal checks verify specifics. “Astra agrees with itself” is not evidence.

Provenance protocol: all scientific claims get a persistent ID, primary literature citations, classification (established/reproduced/proposed/disputed/open), date, theory assumptions, linked calculation or source, and explicit known objections. Negative results stay recorded.

The user-facing learning ritual. Every working session begins with a five-minute “what changed and why it matters” explanation; then one worked example with each symbol defined; then one diagram; then the strongest objection; then a choice or question for the research director. A question is welcome at any depth.

# Original eight-week plan — governed by evidence gates

Gate 0 | Approved on 17 October 2026\. The work remains private. Cycle 01 provides the reproduction foundation; Cycle 02 begins the physical-constraints audit. The original week ranges below describe the intended sequence, not a report of elapsed time or an automatic research schedule. Gate 03 remains open until physical feasibility is supported.

Weeks 1–2 | Evidence baseline: acquire and closely read the primary model papers, extract equations/assumptions, build a comparison matrix and literature challenge register. First deliverable: teaching atlas v1 and three candidate comparison memos.

Weeks 3–4 | Reproduction: reproduce the ideal two-mass phase calculation, an established entanglement witness, at least one classical-channel/decoherence result, and one quantitative classical-entanglement or metric-diffusion result. First Lean algebra theorem. Independent numerical checks required.

Weeks 5–6 | Discriminator search: quantify where predictions diverge with nuisance parameters marginalized or bounded; explore sensitivity to m, d, Δx and t, alternative observables, and whether a two-experiment joint constraint is materially stronger. Register candidate innovations and aggressively try to falsify each.

Weeks 7–8 | Stress test and draft: assess instrument feasibility, model completeness, likelihood or information-discrimination metric, counterexamples and published priority. Produce a reproducible technical note. Seek qualified specialist review before public claims or submission.

At every gate: either CONTINUE with evidence, PIVOT with a documented reason, or STOP because the purported novelty already exists or the predicted signal cannot survive realistic constraints.

# DELIVERABLES AND REVIEW STANDARDS

After each research cycle: 1-page plain-language briefing; updated figure; new or corrected definitions; what calculations passed; what failed; strongest new counterargument; evidence links; next decision. Code must execute cleanly from a pinned environment. A public claim needs independent physical review.

Success minimum: a correct public, reproducible map of models, assumptions and observables plus verified toy calculations. Strong success: a previously unreported, independently checked parameter bound or experiment-design insight. Exceptional success: a publishable, new discrimination result. Unification itself is beyond the scope of this program.

# LEARNING CHECKPOINT — CAN YOU ANSWER THESE?

Why can two particles be correlated without being entangled? What does the phase Δφ contain that a common phase does not? Why does a classical field not necessarily imply a purely LOCC information channel? What combination of measurements would reject a specified model even when it predicts some entanglement?

These are teaching prompts, not prerequisites. Each will acquire an interactive example or diagram during the research program.

# Foundational sources — original registry

S01  Bose et al. (2017). Spin entanglement witness of quantum gravity. Physical Review Letters 119, 240401\.  [https\://doi.org/10.1103/PhysRevLett.119.240401](https://doi.org/10.1103/PhysRevLett.119.240401)

S02  Kafri, Taylor & Milburn (2014). A classical channel model for gravitational decoherence. New Journal of Physics 16, 065020\.  [https\://doi.org/10.1088/1367-2630/16/6/065020](https://doi.org/10.1088/1367-2630/16/6/065020)

S03  Oppenheim (2023). A postquantum theory of classical gravity? Physical Review X 13, 041040\.  [https\://doi.org/10.1103/PhysRevX.13.041040](https://doi.org/10.1103/PhysRevX.13.041040)

S04  Aziz & Howl (2025). Classical theories of gravity produce entanglement. Nature 646, 813–817.  [https\://doi.org/10.1038/s41586-025-09595-7](https://doi.org/10.1038/s41586-025-09595-7)

S05  Trillo & Navascués (2025). Diósi–Penrose model of classical gravity predicts gravitationally induced entanglement. Physical Review D 111, L121101.  [https\://doi.org/10.1103/PhysRevD.111.L121101](https://doi.org/10.1103/PhysRevD.111.L121101)

S06  Di Biagio (accepted 2026). Gravity-induced entanglement is not a theory-independent witness of nonclassicality of the gravitational field. Physical Review D.  [https\://doi.org/10.1103/r8ry-sp35](https://doi.org/10.1103/r8ry-sp35)

S07  Boulle & Franzmann (2026). Subsystems independence in gravitationally induced entanglement proposals. Physical Review D 114, 025015\.  [https\://doi.org/10.1103/tgjx-y7hl](https://doi.org/10.1103/tgjx-y7hl)

S08  Feng, Vedral & Marletto (2026). Collapse-based models for gravity do not violate the entanglement-based witness of nonclassicality. Physical Review D 113, 104055\.  [https\://doi.org/10.1103/83rl-nygv](https://doi.org/10.1103/83rl-nygv)

S09  Hirotani & Matsumura (2026). Testing classical-quantum gravity with geodesic deviation. Physical Review D 114, 026014\.  [https\://doi.org/10.1103/fx1h-97sx](https://doi.org/10.1103/fx1h-97sx)

S10  Liu, Chen, Somiya & Ma (2026). Testing the quantum nature of gravity through interferometry. Physical Review D 113, 022002\.  [https\://doi.org/10.1103/15n3-zzjw](https://doi.org/10.1103/15n3-zzjw)

S11  European Commission / CORDIS (last updated February 2025). CLOSEtoQG experimental-platform progress and constraints.  [https\://cordis.europa.eu/project/id/101041115/reporting](https://cordis.europa.eu/project/id/101041115/reporting)

S12  Howl, Cooper & Hackermüller (2026). Gravitationally induced entanglement in atom interferometry. Physical Review A 114, 023306\.  [https\://doi.org/10.1103/l62d-gz5c](https://doi.org/10.1103/l62d-gz5c)

S13  Williams (2026). Gravity-induced entanglement under constrained dynamics. Physical Review A 114, 032221\.  [https\://doi.org/10.1103/pg7l-f26t](https://doi.org/10.1103/pg7l-f26t)

Source policy: the registry is an initial reading list, not a claim that every equation has been independently audited yet. Primary published papers outrank summaries. Flag contradictory claims explicitly instead of silently harmonizing them.

# DECISION LOG / CHANGELOG

2026-10-17 | v0.1: charter created and initially held for approval. The programme adopted comparative, multi-observable model discrimination, nominated three experiment families and defined its evidence ladder.

2026-10-17 | v0.2: charter approved and Cycle 01 executed; initial assumptions and contested interpretations recorded. GitHub import and four-lemma Lean verification followed.

2026-10-17 | v0.3: Cycle 02 added finite-sphere, geometry, force-ratio and heating checks, plus two figures. No feasible experimental window was certified.

2026-10-17 | v0.4: author pass reconciled the three sections, clarified notation and conditional findings, updated verification status and prepared the complete PDF snapshot. No scientific gate was advanced and no new calculation was introduced.

[image1]: assets/image1.png

[image2]: assets/image2.png

[image3]: assets/image3.png

[image4]: assets/image4.png

[image5]: assets/image5.png

[image6]: assets/image6.png