from __future__ import annotations
import numpy as np
import pytest
from scipy.constants import G, hbar
from gravity_witness.gw import *


def random_qubit(rng):
    q = rng.normal(size=2) + 1j*rng.normal(size=2)
    return q / np.linalg.norm(q)


@pytest.mark.parametrize('seed', range(100))
def test_pure_state_four_independent_checks(seed):
    rng = np.random.default_rng(seed)
    p = rng.uniform(-30, 30, 4)
    v = state_from_phases(p)
    c = pure_concurrence(v)
    analytical = abs(np.sin(phase_invariant(p)/2))
    reduced = reduced_a(density(v))
    c_from_purity = np.sqrt(max(0, 2*(1-np.trace(reduced@reduced).real)))
    c_from_svd = 2*np.prod(np.linalg.svd(v.reshape(2,2), compute_uv=False))
    assert c == pytest.approx(analytical, abs=3e-14)
    assert c == pytest.approx(c_from_purity, abs=2e-12)
    assert c == pytest.approx(c_from_svd, abs=3e-14)
    assert c == pytest.approx(2*negativity(density(v)), abs=3e-14)
    # Local and global phases cannot affect entanglement.
    alpha, beta = rng.normal(size=(2,2))
    shifted = p + (alpha[:,None]+beta[None,:]).ravel() + 7.31
    assert pure_concurrence(state_from_phases(shifted)) == pytest.approx(c, abs=3e-14)
    assert np.abs(v)**2 == pytest.approx(np.full(4,.25), abs=1e-14)


@pytest.mark.parametrize('seed', range(200))
def test_noisy_closed_form_and_validity(seed):
    rng=np.random.default_rng(seed+1000)
    delta=rng.uniform(-30,30)
    lam=rng.uniform(0,1)
    rho=local_dephase(density(controlled_phase_state(delta)),lam,lam)
    validate_density(rho)
    assert negativity(rho) == pytest.approx(negativity_equal_dephasing(delta,lam), abs=3e-14)
    assert np.diag(rho).real == pytest.approx(np.full(4,.25))
    for a,b in [('X','Z'),('Z','X'),('Y','Y'),('Z','Z')]:
        probs=joint_probabilities(rho,a,b)
        assert np.dot(probs,[1,-1,-1,1]) == pytest.approx(pauli_expectation(rho,a,b),abs=1e-14)


@pytest.mark.parametrize('delta', [0,.01,.8,np.pi,4.2,2*np.pi,9.3])
@pytest.mark.parametrize('lam', [0.,.1,np.sqrt(2)-1,.6,1.])
def test_noisy_edges(delta,lam):
    rho=local_dephase(density(controlled_phase_state(delta)),lam,lam)
    assert negativity(rho) == pytest.approx(negativity_equal_dephasing(delta,lam),abs=2e-14)


@pytest.mark.parametrize('seed', range(15))
def test_matrix_exponential_reproduces_elementwise_solution(seed):
    rng=np.random.default_rng(seed+2000)
    energies=rng.normal(size=4)
    gamma=rng.uniform(.001,2)
    t=rng.uniform(.01,10)
    dense=liouvillian_evolve(energies,gamma,t)
    direct=local_dephase(density(state_from_phases(-energies*t)),np.exp(-gamma*t),np.exp(-gamma*t))
    assert dense == pytest.approx(direct,abs=3e-13)


@pytest.mark.parametrize('seed', range(50))
def test_separable_controls_and_witness_bound(seed):
    rng=np.random.default_rng(seed+3000)
    states=[np.kron(random_qubit(rng),random_qubit(rng)) for _ in range(5)]
    weights=rng.dirichlet(np.ones(5))
    rho=sum(w*density(v) for w,v in zip(weights,states))
    assert negativity(rho)<3e-14
    assert graph_witness_score(rho)<=1+3e-14
    pure=rng.normal(size=4)
    alpha,beta=pure[:2],pure[2:]
    assert pure_concurrence(state_from_phases((alpha[:,None]+beta[None,:]).ravel()))<3e-14


def test_perfectly_correlated_classical_mixture_is_not_entanglement():
    rho=np.diag([.5,0,0,.5]).astype(complex)
    assert pauli_expectation(rho,'Z','Z') == pytest.approx(1)
    assert negativity(rho)==0


@pytest.mark.parametrize('tau', np.linspace(0,20,101))
def test_ktm_projection_does_not_entangle(tau):
    assert negativity(ktm_projected(tau))<3e-14


@pytest.mark.parametrize('lam', np.linspace(0,1,21))
def test_graph_witness_at_pi(lam):
    rho=local_dephase(density(controlled_phase_state(np.pi)),lam,lam)
    assert graph_witness_score(rho) == pytest.approx(2*lam+lam*lam,abs=1e-14)
    assert negativity(rho) == pytest.approx(max(0,(2*lam+lam*lam-1)/4),abs=1e-14)


@pytest.mark.parametrize('ratio', [.001,.01,.05,.1,.3,250/450,.9])
def test_geometry_and_approximation_error(ratio):
    g=Geometry(1e-14,1.2e-14,500e-6,ratio*500e-6)
    assert (1-g.phase_rate(quadratic=True)/g.phase_rate()) == pytest.approx(ratio**2,abs=1e-14)
    assert abs(phase_invariant(g.phases(2))) == pytest.approx(2*g.phase_rate(),rel=1e-8)
    # Doubling either mass doubles the rate at fixed geometry.
    assert Geometry(2*g.m_a,g.m_b,g.d,g.s).phase_rate() == pytest.approx(2*g.phase_rate())


@pytest.mark.parametrize('args', [(0,1,2,1),(1,1,1,1),(1,1,1,2),(1,1,float('nan'),.1)])
def test_bad_geometry_rejected(args):
    with pytest.raises(ValueError): Geometry(*args)


@pytest.mark.parametrize('lam', [-.1,1.1,float('nan')])
def test_bad_retention_rejected(lam):
    with pytest.raises(ValueError): local_dephase(np.eye(4)/4,lam,.5)


def test_invalid_rho_and_non_normalized_state_rejected():
    with pytest.raises(ValueError): density(np.ones(4))
    with pytest.raises(ValueError): negativity(np.diag([2.,-1.,0.,0.]))
    with pytest.raises(ValueError): negativity(np.ones((2,2)))


@pytest.mark.parametrize('seed', range(200))
def test_unequal_noise_full_spectrum(seed):
    rng=np.random.default_rng(seed+4000)
    a,b=rng.uniform(0,1,2); delta=rng.uniform(-30,30)
    rho=local_dephase(density(controlled_phase_state(delta)),a,b)
    numerical=np.linalg.eigvalsh(partial_transpose_b(rho))
    assert numerical == pytest.approx(partial_transpose_spectrum(delta,a,b),abs=3e-14)


@pytest.mark.parametrize('a,b', [(0,0),(1,1),(0,1),(1,0),(.8,.8),(.95,.1),(.1,.95)])
def test_unequal_noise_pi_witness(a,b):
    rho=local_dephase(density(controlled_phase_state(np.pi)),a,b)
    assert graph_witness_score(rho) == pytest.approx(a+b+a*b,abs=1e-14)
    assert negativity(rho) == pytest.approx(max(0,(a+b+a*b-1)/4),abs=1e-14)


@pytest.mark.parametrize('seed',range(100))
def test_phase_calibrated_witness_for_any_phase(seed):
    rng=np.random.default_rng(seed+7000)
    delta=rng.uniform(-40,40);lam=rng.uniform(0,1)
    rho=local_dephase(density(controlled_phase_state(delta)),lam,lam)
    score=phase_calibrated_score(rho,delta)
    assert score==pytest.approx(lam*lam+2*lam*abs(np.sin(delta/2)),abs=4e-14)
    assert negativity(rho)==pytest.approx(max(0,(score-1)/4),abs=4e-14)
    product=np.kron(random_qubit(rng),random_qubit(rng))
    assert phase_calibrated_score(density(product),delta)<=1+4e-14


def test_planning_bound_and_bad_inputs():
    n=planning_trials(1.2,1e-6,.05,.03)
    assert witness_margin(n,1e-6)+witness_margin(n,.05)<=.17
    assert witness_margin(n-1,1e-6)+witness_margin(n-1,.05)>.17
    with pytest.raises(ValueError): planning_trials(1.,1e-6,.05)
    with pytest.raises(ValueError): witness_margin(0,.05)


@pytest.mark.parametrize('delta',[0.,.1,1.,np.pi,4.,2*np.pi])
def test_local_visibility_is_not_noise_retention(delta):
    lam=.9
    rho=local_dephase(density(controlled_phase_state(delta)),lam,.7)
    visibility=2*abs(reduced_a(rho)[0,1])
    assert visibility==pytest.approx(lam*abs(np.cos(delta/2)),abs=1e-14)
