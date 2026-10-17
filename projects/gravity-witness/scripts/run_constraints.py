"""Generate reproducible conditional physical-constraints report for the Cycle 01 DP case.

Run with PYTHONPATH=projects/gravity-witness/src python projects/gravity-witness/scripts/run_constraints.py
No overwrites of baseline Cycle 01 outputs. Outputs default to cycle02/ under this project.
"""
from __future__ import annotations
from pathlib import Path
import json, csv, os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from gravity_witness.constraints import (
    sphere_radius, scenario, minimum_sigma_for_nonoverlap,
    DEFAULT_GAP_OVER_SIGMA, DEFAULT_SPLIT_OVER_SIGMA,
    shield_clearance_ratio, gaussian_force_fraction,
    finite_sphere_onset,
)

PROJECT = Path(__file__).resolve().parents[1]
ROOT = Path(os.environ.get('GW_CYCLE02_OUTPUT',PROJECT.parents[1]/'build/gravity-witness/cycle02')).resolve()
# Never accidentally overwrite either Cycle 01 outputs or arbitrary paths.
if ROOT == (PROJECT/'results/cycle01').resolve() or ROOT == (PROJECT/'results/cycle02').resolve() or ROOT == PROJECT.resolve():
    raise RuntimeError('Refusing to overwrite Cycle 01 or entire project')
ROOT.mkdir(parents=True,exist_ok=True)

mass=1e-14
rho=2200.
R=sphere_radius(mass,rho)
sigmas_um=[1,3,5,5.5,10,20,50,100]
scenarios=[scenario(mass,rho,s*1e-6) for s in sigmas_um]
Rgold=sphere_radius(mass,19300.)

meta={
  'cycle':'02', 'date':'2026-10-17',
  'status':'CONDITIONAL_CONSTRAINT_AUDIT; NOT EXPERIMENTAL VIABILITY CERTIFICATION',
  'reference_geometry':{'minimum_centre_gap_over_sigma':.375,'branch_split_over_sigma':.125,
    'centres_separation_over_sigma':.5,'fixed_geometry_shield_ratio_floor':'2*split/gap = 2/3 as R/sigma -> 0'},
  'source_crosswalk':{
    'S05':'https://arxiv.org/pdf/2411.02287v2',
    'S20':'https://comptes-rendus.academie-sciences.fr/physique/item/10.5802/crphys.270.pdf',
    'S23':'https://doi.org/10.1103/2jm3-4976',
    'S24':'https://eprints.soton.ac.uk/456167/1/2109.14980.pdf',
    'S25':'https://pubmed.ncbi.nlm.nih.gov/32216404/',
    'S26':'https://doi.org/10.1103/h74z-zvfv',
    'S27':'https://doi.org/10.1088/1367-2630/ad8c77'
  },
  'geometry_scope':'Two rigid, equal-density spheres; Trillo inline 4 fixed COM branches. H=0 for computed DP onset. Hard-sphere collision is an exact geometry test under the stated rigid-sphere assumption.',
  'material_assumptions':{
    'silica_label':'illustrative homogeneous density 2200 kg/m^3, not an apparatus specification',
    'gold_label':'illustrative homogeneous density 19300 kg/m^3, not an apparatus specification',
    'mass_kg_each':mass,
    'silica_equivalent_radius_m':R,
    'gold_equivalent_radius_m':Rgold,
  },
  'geometric_threshold':{
    'sigma_over_R_must_exceed':2/DEFAULT_GAP_OVER_SIGMA,
    'silica_sigma_m_strict_lower_edge':minimum_sigma_for_nonoverlap(R),
    'gold_sigma_m_strict_lower_edge':minimum_sigma_for_nonoverlap(Rgold),
    'physical_size_interpretation_sigma_approx_R':'FAIL in this fixed geometry because d=0.375 sigma < 2R at sigma=R',
  },
  'phenomenological_sigma_case':{
    'sigma_is_independent_of_solid_body_radius':True,
    'finite_sphere_onset_at_R_over_sigma_0':finite_sphere_onset(radius_over_sigma=0),
    'finite_sphere_onset_at_R_over_sigma_0_1':finite_sphere_onset(radius_over_sigma=.1),
    'finite_sphere_onset_at_R_over_sigma_0_18':finite_sphere_onset(radius_over_sigma=.18),
    'conclusion':'Nonoverlapping spheres with phenomenological sigma >> R can mathematically entangle in this static Gaussian finite-sphere extension; not an apparatus prediction.'
  },
  'shield_caveat':{
    'source_requirement':'Aspelmeyer argues spatial delocalization must be MUCH smaller than distance to conducting shield to limit which-path information',
    'ratio_definition':'2*L/(d-2R) for ideal zero-thickness shield centered between closest surfaces',
    'universal_lower_edge':2*DEFAULT_SPLIT_OVER_SIGMA/DEFAULT_GAP_OVER_SIGMA,
    'conclusion':'Ratio >= 2/3 for all non-overlapping R; no value in THIS geometry is in a demonstrably much-less-than-one regime. This is not a calculated electromagnetic decoherence rate or a theorem ruling out alternative shielding.'
  },
  'force_kernel_caveat':{
    'formula':'F/F_Newton = erf(r/(2sigma)) - (r/(sqrt(pi)*sigma))*exp(-r^2/(4sigma^2))',
    'point_source_only':True,
    'fraction_at_nearest_gap_independent_of_sigma':gaussian_force_fraction(.375,1.0),
    'fraction_at_mean_centres_independent_of_sigma':gaussian_force_fraction(.5,1.0),
    'lab_bound':'Lee et al. 2020 confirms Newtonian gravity in torsion-balance extended bodies at separations down to 52 um, but applying it to sigma demands modeling the apparatus response; no direct sigma exclusion is claimed from the plotted point-pair fractions.'
  },
  'external_empirical_constraints':{
    'XENONnT_2026_95pct_lower_R0_m':4.5e-10,
    'applicability':'Markovian stochastic DP with specified X-ray noise spectrum and nuclear/electron response; sigma convention and exact kernel mapping need confirmation; does not exclude micrometre-scale sigma by itself',
    'macroscopic_classicality_suggested_upper_R0_m':1e-4,
    'upper_is_empirical':False,
    'source_upper':'Figurato et al. 2024 (model-dependent classicality requirement), not a laboratory upper limit',
    'short_range_gravity':'52 um lowest source-detector separation in Lee 2020; Yukawa interaction exclusion not interchangeable with Gaussian-smeared pair force parameter without experiment convolution'
  },
  'scenarios':scenarios,
  'pending':['Convolve exact force kernel over 2020 torsion geometry + likelihood','Obtain shield geometry/dipole noise and actual surface and coating thickness','Free-wave-packet/trapping evolution and COM coherence times','Heating with constituent-granularity and correlated noise','Test sigma normalization against XENONnT 2026 and non-Gaussian smearing','Assess locality interpretation: Feng/Vedral/Marletto 2026'],
  'claim':'No viable parameter window has been experimentally certified; hard-sphere and shield reasoning is strong evidence against THIS convenient configuration under Aspelmeyer shielding assumptions, not a universal DP no-go theorem.'
}
with (ROOT/'constraints.json').open('w') as f:json.dump(meta,f,indent=2,allow_nan=False);f.write('\n')
with (ROOT/'scenarios.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(scenarios[0].keys()));writer.writeheader();writer.writerows(scenarios)

# An explanatory chart: natural-bound 2L/(d-2R), which cannot become << 1.
sig=np.geomspace(max(1e-6,minimum_sigma_for_nonoverlap(R)*1.001),1e-4,140)
ratio=[shield_clearance_ratio(.375*s,.125*s,R) for s in sig]
fig,ax=plt.subplots(figsize=(9,4.6),layout='constrained')
ax.plot(sig*1e6,ratio,linewidth=2.2,label='Minimum-distance / zero-thickness ideal shield')
ax.axhline(2/3,linestyle=':',linewidth=1.6,label='Point-mass geometric floor: 2/3')
ax.axvline(minimum_sigma_for_nonoverlap(R)*1e6,linestyle='--',linewidth=1,label='Disjoint-sphere threshold')
ax.set(ylim=(0,3.7),xlim=(5,100),xlabel='Phenomenological smearing length sigma (um)',ylabel='Split / closest surface-to-shield distance',title='Hard-sphere geometry cannot reach the small-displacement screening regime')
ax.grid(alpha=.17);ax.legend(loc='upper right',fontsize=8);fig.savefig(ROOT/'shield_ratio.png',dpi=150);plt.close(fig)

# Point-pair force is a conditional kernel diagnostic, not a torsion-balance fit.
sig=np.geomspace(1e-6,1e-4,180)
fig,ax=plt.subplots(figsize=(9,4.6),layout='constrained')
ax.plot(sig*1e6,[gaussian_force_fraction(52e-6,x) for x in sig],linewidth=2.1,label='At 52 um (point-pair proxy)')
ax.plot(sig*1e6,[gaussian_force_fraction(.375*x,x) for x in sig],linewidth=2.1,label='At nearest DP branch gap 0.375 sigma')
ax.plot(sig*1e6,[gaussian_force_fraction(.5*x,x) for x in sig],linewidth=2.1,label='At average branch separation 0.5 sigma')
ax.axhline(1,linestyle=':',label='Unsmeared Newton pair force')
ax.set(xscale='log',yscale='log',xlim=(1,100),ylim=(1e-3,1.2),xlabel='Smearing length sigma (um)',ylabel='Smoothed point-pair force / Newtonian pair force',title='A phenomenological Gaussian smearing would change short-distance forces')
ax.grid(alpha=.17);ax.legend(fontsize=8);fig.savefig(ROOT/'conditional_force.png',dpi=150);plt.close(fig)
print('Cycle 02 conditional constraint audit written to',ROOT)
print('Silica radius:',R*1e6,'um. Strict sigma lower edge:',minimum_sigma_for_nonoverlap(R)*1e6,'um.')
print('Geometric shield ratio floor:',2/3)
print('Finite-sphere DP onset at R/sigma=0.1:',finite_sphere_onset(radius_over_sigma=.1))
print('Point-smeared gravity force fraction at 0.375sigma:',gaussian_force_fraction(.375,1.))
