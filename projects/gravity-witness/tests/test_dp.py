from __future__ import annotations
import numpy as np
import pytest
from gravity_witness.gw import *
from gravity_witness import dp


def raw_pt(matrix):
    return matrix.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)


def test_published_limiting_distances_and_example():
    roots=dp.limiting_distances()
    assert roots['inline_small_split_gap_over_sigma']==pytest.approx(.850872,abs=5e-7)
    assert roots['transverse_large_split_gap_over_sigma']==pytest.approx(2.21093,abs=5e-6)
    assert dp.onset_eigenvalue(3/8,1/8)==pytest.approx(-.0001915,abs=1e-7)  # Paper prints an approximate/truncated value.


@pytest.mark.parametrize('seed',range(100))
def test_gram_channel_and_short_time_ppt(seed):
    rng=np.random.default_rng(seed+5000)
    gap,split=10**rng.uniform(-1.3,1,2)
    transverse=bool(seed%2)
    c=dp.configurations(gap,split,transverse)
    gram=dp.mass_density_gram(c)
    assert np.linalg.eigvalsh(gram).min()>-1e-12
    coefficients=dp.generator_coefficients(c)
    assert np.diag(coefficients)==pytest.approx(np.zeros(4),abs=1e-13)
    assert coefficients==pytest.approx(coefficients.conj().T,abs=1e-13)
    assert coefficients.real.max()<1e-13
    r0=np.ones((4,4),complex)/4
    projector=np.eye(4)-r0
    initial_ppt_generator=projector@raw_pt(coefficients*r0)@projector
    assert np.linalg.eigvalsh(initial_ppt_generator).min()==pytest.approx(
        min(0,dp.onset_eigenvalue(gap,split,transverse)),abs=3e-13)
    # Completely positive evolution preserves positivity for arbitrary pure inputs.
    q=rng.normal(size=4)+1j*rng.normal(size=4);q/=np.linalg.norm(q)
    validate_density(dp.evolve(c,float(10**rng.uniform(-3,3)),density(q)))


@pytest.mark.parametrize('seed',range(10))
def test_independent_lindblad_reconstruction(seed):
    rng=np.random.default_rng(seed+6000)
    c=dp.configurations(*10**rng.uniform(-1,1,2),transverse=bool(seed%2))
    u=10**rng.uniform(-1,1)
    assert dp.evolve_lindblad(c,u)==pytest.approx(dp.evolve(c,u),abs=1e-12)


def test_actual_entangling_example_not_roundoff():
    c=dp.configurations(3/8,1/8)
    n=negativity(dp.evolve(c,1.))
    assert n>1e-4
    assert n<3e-4
    # The reported slope is computed independently, without relying on a plotted curve.
    tiny=1e-3
    assert negativity(dp.evolve(c,tiny))/tiny==pytest.approx(-dp.onset_eigenvalue(3/8,1/8),rel=2e-4)


@pytest.mark.parametrize('u',[0,.1,1,10,100,1000])
def test_nonentangling_inline_regime(u):
    assert negativity(dp.evolve(dp.configurations(2,.125),u))<3e-13
