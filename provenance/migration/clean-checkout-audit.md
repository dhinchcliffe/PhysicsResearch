# Clean-checkout preservation audit

The first GitHub numerical workflow at commit `93c21ca5072560a51f91db2a9b92583d805bed48` installed all 18 pinned dependencies successfully on Python 3.13.16 and passed `pip check`, but stopped at the frozen-artifact integrity gate.

Git's initial `text=auto` handling normalized CRLF to LF in `negativity_vs_phase.csv` and `dp_comparison.csv`. Their numbers did not change, but their bytes no longer matched the preserved original SHA-256 manifest. This is an import preservation defect, not a scientific result or a reason to weaken the integrity check.

The repair explicitly marks CSV files `-text` and restores only the two known CSV members directly from the checksum-verified original ZIP. The repair verifies the Git index bytes before committing. The original manifest, archive, predictions and tests remain unchanged. The one-time repair workflow is retired after verified completion.

Initial failed run: https://github.com/dhinchcliffe/PhysicsResearch/actions/runs/39022307759

Subsequent numerical CI must pass the original integrity checks before running the research suite. A passing local run is not substituted for that clean-checkout check.
