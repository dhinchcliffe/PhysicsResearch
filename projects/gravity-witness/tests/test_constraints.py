"""Cycle 02: numeric, dimensional and geometric guardrails (not lab verification)."""
import math
import numpy as np
import pytest
from gravity_witness import dp
from gravity_witness.constraints import (
    G, HBAR, DEFAULT_GAP_OVER_SIGMA, DEFAULT_SPLIT_OVER_SIGMA,
    sphere_radius, nonoverlap, minimum_sigma_for_nonoverlap,
    shield_clearance_ratio, gaussian_force_fraction, dp_heating_power,
    u_to_seconds, sphere_form_factor, finite_sphere_kernel, finite_sphere_onset,
    scenario,
)


def test_published_dp_point_onset_is_reproduced_from_independent_fourier_integral():
    assert finite_sphere_onset(radius_over_sigma=0) == pytest.approx(
        dp.onset_eigenvalue(3/8,1/8), abs=3e-13)


@pytest.mark.parametrize('r',[0.,.001,.05,.375,.5,1.,2.5,4.0])
def test_fourier_kernel_recovers_gaussian_point_kernel(r):
    assert finite_sphere_kernel(r,0.) == pytest.approx(dp.kernel(r),abs=2e-12)


@pytest.mark.parametrize('a',[0.,.005,.05,.10,.15,.187])
def test_96_nodes_agree_with_128_nodes_for_finite_spheres(a):
    for r in [0.,.375,.5,.625,1.0]:
        assert finite_sphere_kernel(r,a,96) == pytest.approx(
            finite_sphere_kernel(r,a,128),abs=5e-13)


@pytest.mark.parametrize('a',[.01,.05,.1,.15,.18])
def test_finite_sphere_in_entangling_regime_and_no_false_automatic_exclusion(a):
    """At a<0.1875, nearest branch centres CAN hold disjoint spheres."""
    assert DEFAULT_GAP_OVER_SIGMA > 2*a
    assert finite_sphere_onset(radius_over_sigma=a)<0


def test_physical_radius_sigma_identification_immediately_overlaps():
    assert not nonoverlap(3/8,1.)
    assert minimum_sigma_for_nonoverlap(1.) == pytest.approx(16/3)


@pytest.mark.parametrize('a',[.001,.05,.1,.18])
def test_shield_ratio_stays_order_one_across_nonoverlap_geometry(a):
    # Limit a->0 is precisely 2L/d = 2/3, not 'much smaller than one'.
    ratio=shield_clearance_ratio(3/8,1/8,a)
    assert ratio >= 2/3
    assert ratio == pytest.approx((1/4)/(3/8-2*a))


def test_shield_ratio_unusable_on_overlapping_branches():
    assert math.isinf(shield_clearance_ratio(.375,.125,.19))


@pytest.mark.parametrize('ratio',[.001,.015,.05,.375,.5,1.,2.,4.,8.])
def test_gaussian_force_matches_negative_potential_gradient(ratio):
    sigma=1e-5; r=ratio*sigma
    h=max(r*1e-4,1e-12)
    f=lambda z: math.erf(z/(2*sigma))/z
    d=(f(r+h)-f(r-h))/(2*h)
    got=gaussian_force_fraction(r,sigma)
    assert got == pytest.approx(-r*r*d,abs=4e-6)


def test_force_ratio_tends_to_zero_or_one_as_expected():
    assert gaussian_force_fraction(1e-7,1e-5) <1e-6
    assert gaussian_force_fraction(1e-3,1e-5)>0.99999


def test_heating_has_inverse_cubic_length_dependence_and_mass_scaling():
    p=dp_heating_power(1e-14,1e-5)
    assert p==pytest.approx(G*HBAR*1e-14/(4*math.sqrt(math.pi)*1e-15))
    assert dp_heating_power(1e-14,2e-5)==pytest.approx(p/8)
    assert dp_heating_power(2e-14,1e-5)==pytest.approx(2*p)


def test_dimensionless_u_conversion():
    u=407.9285872556609;s=10e-6;m=1e-14
    t=u_to_seconds(u,s,m)
    assert G*m*m*t/(2*HBAR*s)==pytest.approx(u)


def test_example_10um_silica_is_geometrically_disjoint_but_not_shield_asymptotic():
    v=scenario(1e-14,2200,10e-6)
    assert v['no_overlap']
    assert 1e-6 < v['sphere_radius_m'] < 1.1e-6
    assert v['shield_ratio']>1.4
    assert v['finite_sphere_onset']<0
    assert v['point_gaussian_force_fraction_center']<.02


def test_invalid_parameters_are_rejected():
    for bad in [0,-1,float('nan'),float('inf')]:
        with pytest.raises(ValueError):sphere_radius(bad,2200)
        with pytest.raises(ValueError):gaussian_force_fraction(.1,bad)
        with pytest.raises(ValueError):dp_heating_power(1.,bad)
        with pytest.raises(ValueError):u_to_seconds(1.,1.,bad)
