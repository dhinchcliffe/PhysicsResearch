"""Gravity Witness, cycle 01: finite-dimensional checks, not a theory of gravity.

Basis order: LL, LR, RL, RR (00, 01, 10, 11). SI units in physical
functions. The matter-only Newtonian Hamiltonian is a baseline effective
interaction; executing it does NOT determine the ontology of its mediator.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from numpy.typing import NDArray
from scipy.constants import G, hbar
from scipy.linalg import expm

Array = NDArray[np.complex128]
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULI = {'I': I, 'X': X, 'Y': Y, 'Z': Z}
BITS = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])


def _real_scalar(value: float, name: str, *, positive: bool = False) -> float:
    result = float(value)
    if not np.isfinite(result) or (positive and result <= 0):
        raise ValueError(f'{name} must be finite' + (' and positive' if positive else ''))
    return result


@dataclass(frozen=True)
class Geometry:
    """Two inline path pairs, each separated by s; pair centres separated by d.

    A positions (-s/2,+s/2), B positions (d-s/2,d+s/2). Require 0<s<d.
    Point masses, orthogonal localized paths, prescribed constant separations.
    """
    m_a: float
    m_b: float
    d: float
    s: float

    def __post_init__(self) -> None:
        for name in ('m_a', 'm_b', 'd', 's'):
            object.__setattr__(self, name, _real_scalar(getattr(self, name), name, positive=True))
        if self.s >= self.d:
            raise ValueError('s must be smaller than d; branches must not coincide')

    def distances(self) -> NDArray[np.float64]:
        return np.array([self.d, self.d + self.s, self.d - self.s, self.d])

    def phase_rate(self, *, quadratic: bool = False) -> float:
        """Positive magnitude |d Delta/dt|; stable expression avoids cancellation."""
        rate = 2 * G * self.m_a * self.m_b * self.s**2 / (hbar * self.d**3)
        return float(rate if quadratic else rate / (1 - (self.s / self.d)**2))

    def phases(self, t: float) -> NDArray[np.float64]:
        """Phi=+G*m_a*m_b*t/(hbar*r), since gravitational potential is negative."""
        t = _real_scalar(t, 't')
        if t < 0:
            raise ValueError('t must be nonnegative')
        return G * self.m_a * self.m_b * t / (hbar * self.distances())


def state_from_phases(phases: NDArray[np.float64]) -> Array:
    p = np.asarray(phases, dtype=float)
    if p.shape != (4,) or not np.all(np.isfinite(p)):
        raise ValueError('phases must be a finite vector of length 4')
    return np.exp(1j * p) / 2


def controlled_phase_state(delta: float) -> Array:
    """Locally phase-equivalent canonical state (1,1,1,exp(i Delta))/2."""
    return state_from_phases(np.array([0., 0., 0., _real_scalar(delta, 'delta')]))


def density(state: Array) -> Array:
    v = np.asarray(state, dtype=complex)
    if v.shape != (4,) or not np.all(np.isfinite(v)):
        raise ValueError('state must be a finite vector of length 4')
    if not np.isclose(np.vdot(v, v), 1., atol=1e-10, rtol=0):
        raise ValueError('state must be normalized')
    return np.outer(v, v.conj())


def validate_density(rho: Array, tol: float = 1e-10) -> Array:
    r = np.asarray(rho, dtype=complex)
    if r.shape != (4, 4) or not np.all(np.isfinite(r)):
        raise ValueError('density matrix must be finite and 4x4')
    if not np.allclose(r, r.conj().T, atol=tol, rtol=0):
        raise ValueError('density matrix must be Hermitian')
    if not np.isclose(np.trace(r), 1., atol=tol, rtol=0):
        raise ValueError('density matrix must have trace one')
    if np.linalg.eigvalsh(r).min() < -tol:
        raise ValueError('density matrix must be positive semidefinite')
    return r


def phase_invariant(phases: NDArray[np.float64]) -> float:
    p = np.asarray(phases, dtype=float)
    if p.shape != (4,) or not np.all(np.isfinite(p)):
        raise ValueError('phases must be a finite vector of length 4')
    return float(p[0] + p[3] - p[1] - p[2])


def pure_concurrence(state: Array) -> float:
    density(state)  # input validation
    a, b, c, d = state
    return float(2 * abs(a * d - b * c))


def reduced_a(rho: Array) -> Array:
    return np.trace(validate_density(rho).reshape(2, 2, 2, 2), axis1=1, axis2=3)


def partial_transpose_b(rho: Array) -> Array:
    return validate_density(rho).reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)


def negativity(rho: Array) -> float:
    """Sum of magnitudes of negative eigenvalues of partial transpose, max=1/2."""
    eig = np.linalg.eigvalsh(partial_transpose_b(rho))
    return float(np.maximum(-eig, 0).sum())


def local_dephase(rho: Array, lambda_a: float, lambda_b: float) -> Array:
    """Independent, trace-preserving Z-dephasing with off-diagonal retention lambda.

    This is NOT a standalone classical theory of gravity. Factors can describe
    ordinary environmental decoherence or a specified model's derived noise.
    """
    lambdas = np.asarray([lambda_a, lambda_b], dtype=float)
    if not np.all(np.isfinite(lambdas)) or np.any(lambdas < 0) or np.any(lambdas > 1):
        raise ValueError('retention factors must be finite and in [0,1]')
    differs = BITS[:, None, :] != BITS[None, :, :]
    factors = np.prod(np.where(differs, lambdas, 1.), axis=2)
    return validate_density(rho) * factors


def negativity_equal_dephasing(delta: float, retention: float) -> float:
    _real_scalar(delta, 'delta')
    if not np.isfinite(retention) or not 0 <= retention <= 1:
        raise ValueError('retention must be in [0,1]')
    return max(0., (retention**2 + 2 * retention * abs(np.sin(delta / 2)) - 1) / 4)


def pauli_expectation(rho: Array, a: str, b: str) -> float:
    if a not in PAULI or b not in PAULI:
        raise ValueError('Pauli labels must be I, X, Y, or Z')
    return float(np.trace(validate_density(rho) @ np.kron(PAULI[a], PAULI[b])).real)


def joint_probabilities(rho: Array, a: str, b: str) -> NDArray[np.float64]:
    """Four +/- measurement outcomes, in ++,+-,-+,-- order, for two local settings."""
    if a not in ('X', 'Y', 'Z') or b not in ('X', 'Y', 'Z'):
        raise ValueError('measurement settings must be X, Y, or Z')
    r = validate_density(rho)
    values = []
    for s_a, s_b in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        projector = np.kron((I + s_a * PAULI[a]) / 2, (I + s_b * PAULI[b]) / 2)
        values.append(float(np.trace(r @ projector).real))
    out = np.array(values)
    if np.any(out < -1e-10) or not np.isclose(out.sum(), 1, atol=1e-10):
        raise ArithmeticError('invalid measurement probabilities')
    return np.clip(out, 0, 1)


def graph_witness_score(rho: Array) -> float:
    """S=<XZ>+<ZX>+<YY>. S>1 implies entanglement for any two-qubit state.

    Chosen for canonical controlled phase pi. Not necessary for entanglement
    for arbitrary states or phase choices. It does not certify its mediator.
    """
    return sum(pauli_expectation(rho, a, b) for a, b in [('X', 'Z'), ('Z', 'X'), ('Y', 'Y')])


def liouvillian_evolve(energies_over_hbar: NDArray[np.float64], gamma: float, t: float) -> Array:
    """Independent dense matrix exponential of the 16x16 master generator.

    rho_dot=-i[H/hbar,rho]+gamma/2*sum_j(Z_j rho Z_j-rho).
    gamma is the off-diagonal decay rate per qubit, in inverse seconds.
    """
    e = np.asarray(energies_over_hbar, dtype=float)
    if e.shape != (4,) or not np.all(np.isfinite(e)):
        raise ValueError('energies must be finite and length 4')
    gamma, t = _real_scalar(gamma, 'gamma'), _real_scalar(t, 't')
    if min(gamma, t) < 0:
        raise ValueError('gamma and t must be nonnegative')
    h = np.diag(e)
    eye = np.eye(4)
    # Column-major vectorization: vec(A rho B)=(B^T kron A)vec(rho).
    generator = -1j * (np.kron(eye, h) - np.kron(h.T, eye))
    for op in (np.kron(Z, I), np.kron(I, Z)):
        generator += gamma / 2 * (np.kron(op.T, op) - np.eye(16))
    r0 = np.ones((4, 4), dtype=complex) / 4
    result = (expm(t * generator) @ r0.reshape(16, order='F')).reshape(4, 4, order='F')
    return validate_density(result)


def ktm_projected(tau: float) -> Array:
    """KTM Eq.(16), equal splitting, static two-position restriction; tau=Omega_quad*t.

    x_j=s Z_j/2, K=2G*m_a*m_b/d^3, Omega_quad=K*s^2/hbar,
    gamma=Omega_quad/2. Canonical local phases removed. Only a controlled
    static-branch reduction, NOT a simulation of full oscillator dynamics.
    """
    tau = _real_scalar(tau, 'tau')
    if tau < 0:
        raise ValueError('tau must be nonnegative')
    return local_dephase(density(controlled_phase_state(-tau)), np.exp(-tau / 2), np.exp(-tau / 2))


def partial_transpose_spectrum(delta: float, lambda_a: float, lambda_b: float) -> NDArray[np.float64]:
    """Analytic spectrum for canonical |++> with arbitrary phase and local dephasing.

    Four eigenvalues, sorted. This applies only to the stated four-amplitude
    family and independent Z-dephasing, not to arbitrary mixed states.
    """
    delta = _real_scalar(delta, 'delta')
    a, b = _real_scalar(lambda_a, 'lambda_a'), _real_scalar(lambda_b, 'lambda_b')
    if min(a, b) < 0 or max(a, b) > 1:
        raise ValueError('retentions must be in [0,1]')
    sine2 = np.sin(delta/2)**2
    root_low = np.sqrt(max(0., (a-b)**2 + 4*a*b*sine2))
    root_high = np.sqrt(max(0., (a+b)**2 - 4*a*b*sine2))
    return np.sort(np.array([1-a*b-root_low, 1-a*b+root_low,
                             1+a*b-root_high, 1+a*b+root_high])/4)


def phase_calibrated_frame(rho: Array, target_delta: float) -> Array:
    """Local basis change that puts the ideal target state in Schmidt form.

    For (1,1,1,exp(i delta))/2, remove local half-phases, rotate with Hadamards,
    and remove the remaining relative i. Actual apparatus would need separately
    calibrated local rotations; this function does not establish their fidelity.
    """
    delta = _real_scalar(target_delta, 'target_delta') % (2*np.pi)
    phase = np.diag([1, np.exp(-1j*delta/2)])
    hadamard = np.array([[1,1],[1,-1]])/np.sqrt(2)
    r = np.diag([1,-1j])
    unitary = np.kron(r@hadamard@phase,hadamard@phase)
    return validate_density(unitary@validate_density(rho)@unitary.conj().T)


def phase_calibrated_score(rho: Array, target_delta: float) -> float:
    """S=<XX>-<YY>+<ZZ> in calibrated local frames; all separable states have S<=1.

    For equal local Z-retentions lambda and the target phase, S=lambda^2+
    2*lambda*abs(sin(delta/2)). This witness is not device independent.
    """
    framed = phase_calibrated_frame(rho,target_delta)
    return (pauli_expectation(framed,'X','X')-pauli_expectation(framed,'Y','Y')
            +pauli_expectation(framed,'Z','Z'))


def witness_margin(n_per_setting: int, alpha: float) -> float:
    """One-sided Hoeffding margin for 3 independent means of +/-1 outcomes.

    Equal, pre-fixed n per setting. No missing outcomes or postselection. Does
    not include calibration errors, drift, preparation uncertainty or confounders.
    """
    if isinstance(n_per_setting,bool) or int(n_per_setting)!=n_per_setting or n_per_setting<1:
        raise ValueError('n_per_setting must be a positive integer')
    if not np.isfinite(alpha) or not 0<alpha<1:
        raise ValueError('alpha must be in (0,1)')
    return float(np.sqrt(6*np.log(1/alpha)/n_per_setting))


def planning_trials(score: float, alpha: float, beta: float, systematic_allowance: float=0.) -> int:
    """Conservative iid count PER setting for type-I <=alpha, power >=1-beta.

    Assumes a guaranteed gap score-1-systematic_allowance >0. Interpret score
    as a lower bound on the expected implemented score, not merely an ideal
    prediction. The allowance is an extra prebounded witness bias. This is a
    toy sampling bound, not a laboratory feasibility forecast.
    """
    score = _real_scalar(score,'score')
    allowance = _real_scalar(systematic_allowance,'systematic_allowance')
    if allowance<0 or not 0<alpha<1 or not 0<beta<1:
        raise ValueError('invalid allowance or error probabilities')
    gap=score-1-allowance
    if gap<=0: raise ValueError('no guaranteed witness gap remains')
    return int(np.ceil(6*(np.sqrt(np.log(1/alpha))+np.sqrt(np.log(1/beta)))**2/gap**2))
