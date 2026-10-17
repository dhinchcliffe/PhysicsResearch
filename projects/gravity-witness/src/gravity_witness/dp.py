"""Static Gaussian-smeared DP model used by Trillo & Navascues (2025).

Source: arXiv:2411.02287v2, Eqs. (10)-(14), (20), (22), (23).
Positions use units of sigma. Equal constituent masses are m. Time variable
u = G*m^2*t/(2*hbar*sigma). H_free=0; no motion or finite-body structure.
This is a specified hybrid/collapse model, not a validated classical ontology.
"""
from __future__ import annotations
import numpy as np
from scipy.special import erf
from scipy.linalg import expm
from scipy.optimize import brentq
from .gw import Array, density, controlled_phase_state, validate_density


def kernel(r: float) -> float:
    """sigma*f(r*sigma) = erf(r/2)/r, with analytic small-r limit."""
    r=float(r)
    if not np.isfinite(r) or r<0: raise ValueError('r must be finite and nonnegative')
    if r<1e-3:
        return float((1-r*r/12+r**4/160-r**6/2688)/np.sqrt(np.pi))
    return float(erf(r/2)/r)


def kernel_second(r: float) -> float:
    r=float(r)
    if not np.isfinite(r) or r<0: raise ValueError('r must be finite and nonnegative')
    if r<1e-3:
        return float((-1/6+3*r*r/40-5*r**4/448)/np.sqrt(np.pi))
    return float(2*erf(r/2)/r**3 - np.exp(-r*r/4)/np.sqrt(np.pi)*(0.5+2/r**2))


def configurations(gap: float, split: float, transverse: bool=False) -> np.ndarray:
    """Four configurations (A0B0,A0B1,A1B0,A1B1), shape (4,2,3).

    Inline gap is minimum branch distance, not centre separation. This differs
    from gw.Geometry.d: centre distance = gap + split in the inline setup.
    """
    gap,split=float(gap),float(split)
    if not (np.isfinite(gap) and np.isfinite(split) and min(gap,split)>0):
        raise ValueError('gap and split must be positive and finite')
    if transverse:
        aa=np.array([[0,0,0],[0,split,0]])
        bb=np.array([[gap,0,0],[gap,split,0]])
    else:
        aa=np.array([[0,0,0],[split,0,0]])
        bb=np.array([[gap+split,0,0],[gap+2*split,0,0]])
    return np.array([[a,b] for a in aa for b in bb],dtype=float)


def mass_density_gram(configs: np.ndarray) -> np.ndarray:
    c=np.asarray(configs,dtype=float)
    if c.shape!=(4,2,3) or not np.all(np.isfinite(c)):
        raise ValueError('configs must be finite with shape (4,2,3)')
    return np.array([[sum(kernel(np.linalg.norm(a-b)) for a in x for b in y)
                      for y in c] for x in c])


def generator_coefficients(configs: np.ndarray) -> Array:
    f=mass_density_gram(configs)
    diag=np.diag(f)
    return (1j-1)*diag[:,None]+(-1j-1)*diag[None,:]+2*f


def evolve(configs: np.ndarray, u: float, rho0: Array|None=None) -> Array:
    u=float(u)
    if not np.isfinite(u) or u<0: raise ValueError('u must be finite and nonnegative')
    r=density(controlled_phase_state(0.)) if rho0 is None else validate_density(rho0)
    return validate_density(r*np.exp(u*generator_coefficients(configs)))


def evolve_lindblad(configs: np.ndarray, u: float) -> Array:
    """Independent reconstruction: diagonal Lindblad operators from Gram spectrum.

    In units of u: Hamiltonian diag(-F_aa), jumps diag(sqrt(2*w_j)*v_j).
    This verifies the completely-positive generator, not its classical reading.
    """
    f=mass_density_gram(configs)
    w,v=np.linalg.eigh(f)
    if w.min()<-1e-10: raise ArithmeticError('mass-density Gram matrix not positive')
    eye=np.eye(4);h=-np.diag(np.diag(f))
    gen=-1j*(np.kron(eye,h)-np.kron(h.T,eye))
    for value,column in zip(np.maximum(w,0),v.T):
        jump=np.diag(np.sqrt(2*value)*column)
        jj=jump.conj().T@jump
        gen+=np.kron(jump.conj(),jump)-.5*(np.kron(eye,jj)+np.kron(jj.T,eye))
    r0=np.ones((4,4),complex)/4
    out=(expm(float(u)*gen)@r0.reshape(16,order='F')).reshape((4,4),order='F')
    return validate_density(out)


def onset_eigenvalue(gap: float, split: float, transverse: bool=False) -> float:
    """E_minus divided by G*m^2/(2*hbar*sigma), source Eq.(20)/(23)."""
    if transverse:
        interaction=np.sqrt(2)*(kernel(gap)-kernel(np.hypot(gap,split)))
    else:
        interaction=abs(kernel(gap+2*split)+kernel(gap)-2*kernel(gap+split))/np.sqrt(2)
    return kernel(0)-kernel(split)-interaction


def limiting_distances() -> dict[str,float]:
    """Recompute the two published limiting distance/sigma values."""
    inline=brentq(lambda z:-.5*kernel_second(0)-abs(kernel_second(z))/np.sqrt(2),.1,1.5,
                  xtol=1e-13)
    transverse=brentq(lambda z:kernel(0)-np.sqrt(2)*kernel(z),1,4,xtol=1e-13)
    return {'inline_small_split_gap_over_sigma':float(inline),
            'transverse_large_split_gap_over_sigma':float(transverse)}
