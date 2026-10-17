"""Cycle 02. Conditional physical constraints on the Gaussian Diósi–Penrose example.

This does NOT establish empirical viability, eliminate all DP variants, or model a
shield's electric fields. Dimensionless Trillo/Navascués geometry d/sigma=3/8,
L/sigma=1/8 is held fixed. d is the MINIMUM BRANCH CENTRE GAP, not the mean.

Primary theory: Trillo & Navascués (2025), arXiv:2411.02287v2, Eq 8-20.
Physical critique: Aspelmeyer (2026), DOI:10.5802/crphys.270, pp 2-5.
Heating: Vinante & Ulbricht (2021), arXiv:2109.14980, Eq 1.
"""
from __future__ import annotations
from functools import lru_cache
from math import erf, exp, pi, sqrt
import numpy as np
from numpy.polynomial.hermite import hermgauss

G = 6.67430e-11       # SI (CODATA 2018, used by Cycle 01)
HBAR = 1.0545718176461565e-34  # SI, to match Cycle 01 archived baseline
DEFAULT_GAP_OVER_SIGMA = 3.0/8
DEFAULT_SPLIT_OVER_SIGMA = 1.0/8


def sphere_radius(mass_kg: float, density_kg_m3: float) -> float:
    """Geometrical radius of an incompressible, uniform-density sphere."""
    if not np.isfinite(mass_kg) or not np.isfinite(density_kg_m3) or mass_kg<=0 or density_kg_m3<=0:
        raise ValueError('mass and material density must be positive finite values')
    return float((3*mass_kg/(4*pi*density_kg_m3))**(1/3))


def nonoverlap(gap_m: float, radius_m: float) -> bool:
    """Two rigid identical spherical bodies are disjoint for EVERY branch iff d>2R."""
    if not np.isfinite(gap_m) or not np.isfinite(radius_m) or gap_m<=0 or radius_m<=0:
        raise ValueError('gap and radius must be positive finite values')
    return bool(gap_m>2*radius_m)


def minimum_sigma_for_nonoverlap(radius_m: float, gap_over_sigma: float=DEFAULT_GAP_OVER_SIGMA) -> float:
    """Geometric lower edge; requires sigma GREATER than value, not equal."""
    if not np.isfinite(radius_m) or not np.isfinite(gap_over_sigma) or radius_m<=0 or gap_over_sigma<=0:
        raise ValueError('positive finite inputs required')
    return 2*radius_m/gap_over_sigma


def shield_clearance_ratio(gap_m: float, split_m: float, radius_m: float) -> float:
    """Split / half the minimum *surface* gap; NOT an electromagnetic decoherence rate.

    Aspelmeyer's image-charge argument requires small split / shield distance.
    A perfectly centered zero-thickness shield has clearance (gap-2R)/2.
    A real finite-thickness screen only REDUCES clearance, worsening this ratio.
    A value near unity is not in the required 'much less than one' regime.
    """
    if not np.isfinite(split_m) or split_m<=0: raise ValueError('positive finite split required')
    if not nonoverlap(gap_m,radius_m): return float('inf')
    return 2*split_m/(gap_m-2*radius_m)


def gaussian_force_fraction(r_m: float, sigma_m: float) -> float:
    """Point Gaussian-smeared pair force divided by point Newton force.

    f_sigma(r)=erf[r/(2sigma)]/r. This only applies when smearing ALSO
    regularizes the pair gravitational potential as in T&N; not arbitrary DP.
    An extended-body torsion-balance bound must integrate its source geometry.
    """
    if not np.isfinite(r_m) or not np.isfinite(sigma_m) or min(r_m,sigma_m)<=0:
        raise ValueError('positive finite inputs required')
    x=r_m/(2*sigma_m)
    if x<.035:
        return float((4/(3*sqrt(pi)))*x**3*(1-3*x*x/5+3*x**4/14))
    return float(erf(x)-2*x/sqrt(pi)*exp(-x*x))


def dp_heating_power(mass_kg: float, sigma_m: float) -> float:
    """Single point-mass Gaussian white-noise DP heating, in watts.

    P = G*hbar*m/(4 sqrt(pi) sigma^3). Real structured solids require
    material/noise correlation and many-body treatment; NOT an apparatus bound.
    """
    if not np.isfinite(mass_kg) or not np.isfinite(sigma_m) or min(mass_kg,sigma_m)<=0:
        raise ValueError('positive finite inputs required')
    return G*HBAR*mass_kg/(4*sqrt(pi)*sigma_m**3)


def u_to_seconds(u: float, sigma_m: float, mass_kg: float) -> float:
    """u=G*m^2*t/(2*hbar*sigma), exact unit conversion, NOT feasible run time."""
    if any(not np.isfinite(z) or z<=0 for z in (u,sigma_m,mass_kg)):
        raise ValueError('positive finite inputs required')
    return 2*HBAR*sigma_m*u/(G*mass_kg**2)


def sphere_form_factor(x: np.ndarray) -> np.ndarray:
    """Fourier transform of normalized uniform sphere: 3(sin x - x cos x)/x^3."""
    xx=np.asarray(x,dtype=float)
    return np.where(abs(xx)<.04,
                    1-xx*xx/10+xx**4/280-xx**6/15120,
                    3*(np.sin(xx)-xx*np.cos(xx))/np.where(xx==0,1,xx**3))


@lru_cache(maxsize=20)
def _gausshermite(n: int) -> tuple[np.ndarray,np.ndarray]:
    x,w=hermgauss(n)
    return x,w


@lru_cache(maxsize=400)
def finite_sphere_kernel(distance_over_sigma: float, radius_over_sigma: float, order: int=96) -> float:
    """sigma*f_{sigma,R}(d), uniform solid spheres with Gaussian mass smearing.

    (2/pi) integral_0^infty exp(-q^2) [3 j1(qR/sigma)/(qR/sigma)]^2
                  sinc(q d/sigma) dq

    Gauss-Hermite (even integrand): 1/pi sum_j w_j F(q_j R/sigma)^2
                                                    sinc(q_j d/sigma).
    Reduces exactly to erf(d/(2sigma))/(d/sigma) for R -> 0.
    This is a CONDITIONAL coherent-body extension, not a microscopic composite
    model or a new independent experimental gravity fit.
    """
    s=float(distance_over_sigma);a=float(radius_over_sigma)
    if not np.isfinite(s) or not np.isfinite(a) or s<0 or a<0: raise ValueError('nonnegative finite inputs required')
    x,w=_gausshermite(order)
    form=sphere_form_factor(x*a)
    return float(np.dot(w,form*form*np.sinc(x*s/pi))/pi)


def finite_sphere_onset(gap_over_sigma: float=DEFAULT_GAP_OVER_SIGMA,
                         split_over_sigma: float=DEFAULT_SPLIT_OVER_SIGMA,
                         radius_over_sigma: float=0.) -> float:
    """Initial PPT slope E_minus / [G*m^2/(2*hbar*sigma)].

    Build full cross/self mass-density Gram matrix of TWO extended spheres
    in each of four configurations. Same CP evolution assumption as Cycle 01;
    no kinetic propagation, elasticity, traps or shield decoherence included.
    """
    from gravity_witness import dp  # reuse the preserved Cycle 01 branch setup
    g=float(gap_over_sigma); l=float(split_over_sigma);a=float(radius_over_sigma)
    positions=dp.configurations(g,l,False)
    f=np.array([[sum(finite_sphere_kernel(float(np.linalg.norm(z-t)),a) for z in v for t in w)
                  for w in positions] for v in positions])
    diag=np.diag(f)
    coeff=(1j-1)*diag[:,None]+(-1j-1)*diag[None,:]+2*f
    rho0=np.ones((4,4),dtype=complex)/4
    projection=np.eye(4)-rho0
    derivative=(coeff*rho0).reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    spectrum=np.linalg.eigvalsh(projection @ derivative @ projection)
    return float(spectrum.min())


def scenario(mass_kg: float, density_kg_m3: float, sigma_m: float,
             gap_over_sigma: float=DEFAULT_GAP_OVER_SIGMA,
             split_over_sigma: float=DEFAULT_SPLIT_OVER_SIGMA,
             peak_u: float=407.9285872556609) -> dict:
    radius=sphere_radius(mass_kg,density_kg_m3)
    gap=gap_over_sigma*sigma_m
    split=split_over_sigma*sigma_m
    fit=nonoverlap(gap,radius)
    return dict(
       mass_kg=mass_kg, density_kg_m3=density_kg_m3, sigma_m=sigma_m,
       sphere_radius_m=radius, gap_m=gap, split_m=split,
       minimum_surface_gap_m=gap-2*radius,
       center_distance_m=gap+split,
       no_overlap=fit,
       shield_ratio=(shield_clearance_ratio(gap,split,radius) if fit else None),
       point_gaussian_force_fraction_min_gap=gaussian_force_fraction(gap,sigma_m),
       point_gaussian_force_fraction_center=gaussian_force_fraction(gap+split,sigma_m),
       point_gaussian_force_fraction_52um=gaussian_force_fraction(52e-6,sigma_m),
       point_gaussian_heating_w=dp_heating_power(mass_kg,sigma_m),
       peak_time_s=u_to_seconds(peak_u,sigma_m,mass_kg),
       radius_over_sigma=radius/sigma_m,
       finite_sphere_onset=finite_sphere_onset(gap_over_sigma,split_over_sigma,radius/sigma_m),
    )
