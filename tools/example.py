"""Print the illustrative two-mass calculation; requires no package installation."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects/gravity-witness/src"))
from gravity_witness.gw import (Geometry, phase_invariant, pure_concurrence,
    state_from_phases, density, controlled_phase_state, local_dephase,
    phase_calibrated_score, negativity)

geometry = Geometry(m_a=1e-14, m_b=1e-14, d=450e-6, s=250e-6)
phases = geometry.phases(2.5)
delta = phase_invariant(phases)
noise_retention = 0.95
rho = local_dephase(density(controlled_phase_state(delta)), noise_retention, noise_retention)
print("ILLUSTRATIVE MODEL — not an experiment or verified apparatus performance")
print(f"Joint phase Δ = {delta:.6f} rad")
print(f"Ideal concurrence C = {pure_concurrence(state_from_phases(phases)):.6f}")
print(f"Assumed local noise retention λ = {noise_retention}")
print(f"Noisy negativity N = {negativity(rho):.6f}")
print(f"Calibrated score S = {phase_calibrated_score(rho, delta):.6f}; separable ceiling = 1")
