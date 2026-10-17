# CI comparison note — 2026-10-17

A fresh Python 3.13 / SciPy 1.17 GitHub Actions run reproduced the 970 scientific checks but failed when comparing the *location* of a numerically flat DP negativity maximum. The frozen maximum was at u = 407.9285872556609; a new run reported u = 407.9285932952039. The peak heights differed by about 1.7e-16. No model source, baseline outputs, or physics result changed.

The comparator now gives only `dp_reproduction.json/example/numerical_peak_u` a justified absolute location tolerance of `1e-4`; every physical prediction, including the peak NEGATIVITY and all CSV values, retains strict `rtol=1e-9, atol=1e-12`. Two focused tests ensure a material shift in the argmax still fails, and an incorrect peak height still fails. This repair prevents machine-precision optimizer jitter from being mistaken for a model change.

It is a reproducibility guard—not a new scientific result and not a relaxation of the physical prediction thresholds.
