"""Reproduce cycle-01 outputs. Run: python run_cycle01.py"""
from __future__ import annotations
import csv, json, platform, importlib.metadata, hashlib
import xml.etree.ElementTree as ET
from pathlib import Path
import os
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from gravity_witness.gw import *
ROOT=Path(os.environ.get('GW_OUTPUT_DIR', Path(__file__).resolve().parents[3]/'build/gravity-witness/latest')).resolve()
ROOT.mkdir(parents=True,exist_ok=True)
RESULT=ROOT/'results'; FIG=ROOT/'figures'
RESULT.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)

# Symbolic checks are separate from numerical matrix computations.
d,s,A=sp.symbols('d s A', positive=True)
exact=sp.factor(A*(2/d-1/(d+s)-1/(d-s)))
assert sp.simplify(exact+2*A*s*s/(d*(d*d-s*s)))==0
relative=sp.factor(1-(-2*A*s*s/d**3)/exact)
assert sp.simplify(relative-(s/d)**2)==0
alpha0,alpha1,beta0,beta1,p0,p1,p2,p3=sp.symbols('alpha0 alpha1 beta0 beta1 p0 p1 p2 p3', real=True)
shifted=[p0+alpha0+beta0,p1+alpha0+beta1,p2+alpha1+beta0,p3+alpha1+beta1]
assert sp.expand(shifted[0]+shifted[3]-shifted[1]-shifted[2])==p0+p3-p1-p2
# At Delta=pi the matrix is exact and real. Verify all four PPT eigenvalues.
l,x=sp.symbols('l x', real=True)
vg=sp.Matrix([1,1,1,-1])/2
rg=vg*vg.T
bits=[(0,0),(0,1),(1,0),(1,1)]
rg=sp.Matrix(4,4,lambda i,j:rg[i,j]*l**sum(a!=b for a,b in zip(bits[i],bits[j])))
pt=sp.Matrix(4,4,lambda i,j:rg[2*bits[i][0]+bits[j][1],2*bits[j][0]+bits[i][1]])
poly=pt.charpoly(x)
# charpoly generates a symbol without the input assumptions; compare in its own generator.
x=poly.gen
charpoly=sp.factor(poly.as_expr())
expected=(x-(1+l*l)/4)**2*(x-(1-l*l+2*l)/4)*(x-(1-l*l-2*l)/4)
assert sp.simplify(charpoly-expected)==0
# Projected KTM noise positivity diagnostic from its Gaussian paper is a distinct algebra check.
y,g=sp.symbols('y g', real=True)
noise=sp.Matrix([[y,-2*sp.I*g],[2*sp.I*g,y]])
assert set(noise.eigenvals())=={y-2*g,y+2*g}

# Illustrative input case: original 2017 scales, but only the static hold contribution.
geo=Geometry(1e-14,1e-14,450e-6,250e-6)
t=2.5
phases=geo.phases(t); delta=phase_invariant(phases)
case={'kind':'illustrative_static_hold_not_experimental_measurement',
      'mass_a_kg':geo.m_a,'mass_b_kg':geo.m_b,'centre_distance_m':geo.d,
      'path_split_m':geo.s,'hold_time_s':t,'branch_distances_m':geo.distances().tolist(),
      'branch_phases_rad':phases.tolist(),'delta_rad':delta,
      'concurrence':pure_concurrence(state_from_phases(phases)),
      'negativity':negativity(density(state_from_phases(phases))),
      'phase_rate_rad_s':geo.phase_rate(),
      'quadratic_phase_rate_rad_s':geo.phase_rate(quadratic=True),
      'quadratic_relative_error':(geo.s/geo.d)**2}
small=Geometry(1e-14,1e-14,500e-6,50e-6)
threshold=np.sqrt(2)-1
ktm_lambda=np.exp(-np.pi/2)
examples=[]
for label,lam in [('ideal',1.),('illustrative_environmental_noise',.8),('pi_threshold',threshold),('projected_KTM',ktm_lambda)]:
    r=local_dephase(density(controlled_phase_state(np.pi)),lam,lam)
    examples.append({'label':label,'retention_lambda':float(lam),'negativity':negativity(r),
                     'score_S':graph_witness_score(r),'XZ':pauli_expectation(r,'X','Z'),
                     'ZX':pauli_expectation(r,'Z','X'),'YY':pauli_expectation(r,'Y','Y'),
                     'XZ_joint_probabilities':joint_probabilities(r,'X','Z').tolist()})

# Numerical reproduction grids: save data, not just pictures.
tau=np.linspace(0,2*np.pi,501)
rows=[]
for z in tau:
    row={'tau_phase_rad':float(z)}
    for name,gamma_ratio in [('ideal',0.),('example_noise',.10),('projected_KTM',.5)]:
        lam=np.exp(-gamma_ratio*z)
        row[name+'_negativity']=negativity_equal_dephasing(z,lam)
    rows.append(row)
with (RESULT/'negativity_vs_phase.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

fig,ax=plt.subplots(figsize=(8.6,4.7),layout='constrained')
for name,label in [('ideal','Ideal effective interaction'),('example_noise','Example: decay rate / phase rate = 0.10'),('projected_KTM','Projected classical channel: ratio = 0.50')]:
    ax.plot(tau,[r[name+'_negativity'] for r in rows],label=label,linewidth=2)
ax.set(xlabel='Accumulated nonlocal phase |Delta| (radians)',ylabel='Negativity (0 to 0.5)',
       title='Same force coupling, different coherence: a model-specific test',ylim=(-.015,.53))
ax.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0','pi/2','pi','3pi/2','2pi'])
ax.legend(fontsize=9,loc='upper right');ax.grid(alpha=.25)
fig.savefig(FIG/'01_entanglement_and_noise.png',dpi=180);plt.close(fig)

lams=np.linspace(0,1,301)
fig,ax=plt.subplots(figsize=(8.6,4.7),layout='constrained')
ax.plot(lams,2*lams+lams*lams,label='S = 2 lambda + lambda squared',linewidth=2)
ax.axhline(1,linestyle='--',label='All separable states: S <= 1')
ax.axvline(threshold,linestyle=':',label=f'Threshold retention: {threshold:.4f}')
ax.scatter([ktm_lambda,.8],[2*ktm_lambda+ktm_lambda**2,2*.8+.8**2])
ax.annotate('Projected KTM',xy=(ktm_lambda,2*ktm_lambda+ktm_lambda**2),xytext=(.03,1.35),arrowprops={'arrowstyle':'->'})
ax.annotate('Illustrative noisy quantum case',xy=(.8,2*.8+.8**2),xytext=(.38,2.68),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Local coherence retention lambda (0 to 1)',ylabel='Three-setting witness score S',
       title='At phase pi, entanglement requires enough retained coherence',ylim=(0,3.1))
ax.legend(fontsize=9,loc='upper left');ax.grid(alpha=.25)
fig.savefig(FIG/'02_witness_threshold.png',dpi=180);plt.close(fig)

r=np.linspace(0,.8,200)
fig,ax=plt.subplots(figsize=(8.6,4.7),layout='constrained')
ax.plot(r,100*r*r,linewidth=2)
ax.scatter([.1,250/450],[1,100*(250/450)**2])
ax.annotate('s/d = 0.10: 1% error',xy=(.1,1),xytext=(.17,8),arrowprops={'arrowstyle':'->'})
ax.annotate('250 / 450: 30.9% error',xy=(250/450,100*(250/450)**2),xytext=(.12,45),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Path splitting / centre separation (s/d)',ylabel='Quadratic phase underestimate (%)',
       title='Do not compare models outside a shared approximation regime')
ax.grid(alpha=.25)
fig.savefig(FIG/'03_approximation_guard.png',dpi=180);plt.close(fig)

# A phase-calibrated witness at the actual small-phase illustrative case.
retention=.95  # chosen assumption, NOT an achieved laboratory visibility
rho=local_dephase(density(controlled_phase_state(delta)),retention,retention)
framed=phase_calibrated_frame(rho,delta)
score=phase_calibrated_score(rho,delta)
c=abs(np.sin(delta/2))
small_phase_threshold=float(np.sqrt(1+c*c)-c)
protocol={'scope':'illustrative equal local dephasing; trusted calibrated axes',
 'target_phase_rad':delta,'assumed_retention_lambda':retention,
 'score_S':score,'separable_bound':1.,'negativity':negativity(rho),
 'threshold_retention_lambda':small_phase_threshold,
 'retention_is_not_final_single_particle_visibility':True,
 'final_single_particle_visibility':float(2*abs(reduced_a(rho)[0,1])),
 'settings':{a+b:{'expectation':pauli_expectation(framed,a,b),
   'probabilities_pp_pm_mp_mm':joint_probabilities(framed,a,b).tolist()}
   for a,b in [('X','X'),('Y','Y'),('Z','Z')]},
 'sampling_example':{'assumptions':'iid; pre-fixed sample size; bounded systematic bias; no postselection',
   'alpha':.001,'beta':.05,'systematic_allowance':.03,
   'trials_per_setting':planning_trials(score,.001,.05,.03),
   'not_a_lab_feasibility_forecast':True}}
fig,ax=plt.subplots(figsize=(8.6,4.7),layout='constrained')
ax.plot(lams,lams*lams+2*lams*c,linewidth=2,label='Predicted score at |Delta| = %.3f rad'%abs(delta))
ax.axhline(1,linestyle='--',label='Separable-state ceiling: S = 1')
ax.axvline(small_phase_threshold,linestyle=':',label='Threshold retention: %.3f'%small_phase_threshold)
ax.scatter([retention],[score])
ax.annotate('Assumed retention 0.95: S = %.3f'%score,xy=(retention,score),
 xytext=(.25,1.18),arrowprops={'arrowstyle':'->'})
ax.set(xlabel='Local noise-channel retention lambda (not measured visibility)',
 ylabel='Calibrated three-setting score S',title='A concrete readout for the illustrative 2.5-second hold',ylim=(0,1.5))
ax.legend(loc='upper left',fontsize=9);ax.grid(alpha=.25)
fig.savefig(FIG/'05_calibrated_readout.png',dpi=180);plt.close(fig)
# Read the executed test report; never hand-maintain a passing-test count.
test_report=ET.parse(RESULT/'pytest.xml').getroot()
suites=list(test_report.iter('testsuite'))
checks={k:sum(int(t.attrib.get(k,0)) for t in suites) for k in ('tests','failures','errors','skipped')}
assert checks['failures']==0 and checks['errors']==0
report={
 'cycle':'01','date':'2026-10-17','status':'reproduction_and_model_audit; no new discovery claimed',
 'constants':{'G':float(G),'hbar':float(hbar),'source':'scipy.constants installed version'},
 'illustrative_case':case,
 'small_splitting_case':{'d_m':small.d,'s_m':small.s,'exact_rate_rad_s':small.phase_rate(),
   'quadratic_rate_rad_s':small.phase_rate(quadratic=True),'quadratic_relative_error':.01},
 'phase_calibrated_readout':protocol,
 'dp_reproduction_file':'results/dp_reproduction.json',
 'pi_phase':{'threshold_retention_lambda':float(threshold),
   'max_decay_exponent_gamma_t':float(np.log(1+np.sqrt(2))),
   'max_decay_rate_over_phase_rate_at_pi':float(np.log(1+np.sqrt(2))/np.pi),
   'cases':examples},
 'symbolic_checks':{'exact_inline_phase':str(exact),'quadratic_relative_error':str(relative),
   'local_phase_invariance':'passed','pi_partial_transpose_characteristic_polynomial':str(charpoly),
   'KTM_noise_matrix_eigenvalues':['y-2*g','y+2*g']},
 'code_checks':{**checks,'report':'results/pytest.xml','nature':'parameterized numerical/unit tests, not formal proofs or external expert review'},
 'formal_verification':{'status':'NOT_EXECUTED','reason':'This numerical script does not execute Lean. Consult the separate formal verification report.'},
 'external_physics_review':'NOT_PERFORMED',
 'experimental_data_collected':False,
 'repository_remote':{'intended':'dhinchcliffe/PhysicsResearch','status':'configured target; remote availability is not checked by this numerical script'},
 'versions':{'python':platform.python_version(),**{n:importlib.metadata.version(n) for n in ['numpy','scipy','sympy','matplotlib','pytest']}}
}
(RESULT/'cycle01.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
