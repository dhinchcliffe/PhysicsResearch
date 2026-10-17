"""Reproduce selected DP-model results; no model-viability/novelty claim."""
from pathlib import Path
import os
import json,csv
import numpy as np
from scipy.optimize import minimize_scalar,brentq
from scipy.constants import G,hbar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp
from gravity_witness import dp
from gravity_witness.gw import *
root=Path(os.environ.get('GW_OUTPUT_DIR', Path(__file__).resolve().parents[3]/'build/gravity-witness/latest')).resolve()
(root/'results').mkdir(parents=True,exist_ok=True)
(root/'figures').mkdir(parents=True,exist_ok=True)
c=dp.configurations(3/8,1/8)
f=dp.mass_density_gram(c)
phase_rate=phase_invariant(np.diag(f))
maximum=minimize_scalar(lambda u:-negativity(dp.evolve(c,u)),bounds=(0,1000),method='bounded',
                        options={'xatol':1e-8})
mp.mp.dps=60
mf=lambda x:mp.erf(x/2)/x if x else 1/mp.sqrt(mp.pi)
d,L=mp.mpf(3)/8,mp.mpf(1)/8
onset=mf(0)-mf(L)-abs(mf(d+2*L)+mf(d)-2*mf(d+L))/mp.sqrt(2)
rows=[]
for u in np.linspace(0,3000,601):
    rows.append({'u_dimensionless':float(u),'DP_negativity':negativity(dp.evolve(c,u)),
                 'matched_hamiltonian_only_negativity':abs(np.sin(phase_rate*u/2))/2})
with (root/'results/dp_comparison.csv').open('w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
fig,ax=plt.subplots(figsize=(8.6,4.7),layout='constrained')
ax.plot([r['u_dimensionless'] for r in rows],[r['matched_hamiltonian_only_negativity'] for r in rows],
        label='Same softened Hamiltonian, no collapse noise',linewidth=2)
ax.plot([r['u_dimensionless'] for r in rows],[r['DP_negativity'] for r in rows],
        label='Full DP channel: entangles, then loses entanglement',linewidth=2)
ax.set(xlabel='Dimensionless time u = G m squared t / (2 hbar sigma)',
       ylabel='Negativity (0 to 0.5)',title='A harder comparison: the specified DP model can also entangle',ylim=(-.01,.52))
ax.legend(fontsize=9);ax.grid(alpha=.25)
fig.savefig(root/'figures/04_dp_countermodel.png',dpi=180);plt.close(fig)
report={'source':'arXiv:2411.02287v2, Eqs.10-14,20,22,23',
 'scope':'equal masses; static four-branch subspace; Gaussian cutoff; not a finite-body apparatus model',
 'interpretation':'mathematical predictions reproduced; classical/local interpretation and empirical viability not established',
 'units':{'length':'sigma','time':'u = G*m^2*t/(2*hbar*sigma)'},
 'limiting_distances':dp.limiting_distances(),
 'example':{'gap_over_sigma':3/8,'split_over_sigma':1/8,
  'onset_eigenvalue_per_unit_u':float(onset),'onset_high_precision':mp.nstr(onset,55),
  'paper_printed_onset':-.0001915,'printed_number_absolute_difference':float(abs(onset+mp.mpf('.0001915'))),
  'negativity_at_u_1':negativity(dp.evolve(c,1)),
  'numerical_peak_u':float(maximum.x),'numerical_peak_negativity':float(-maximum.fun),
  'matched_hamiltonian_phase_rate_per_unit_u':float(phase_rate)},
 'fair_comparison_note':'The plotted unitary control shares the DP-softened Hamiltonian. It is NOT point-Newton gravity; softening must separately face force-law constraints.',
 'viability_gate':'Compare sigma and finite-body/shielding assumptions with laboratory constraints before treating this as a viable competing experiment model.'}
(root/'results/dp_reproduction.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
