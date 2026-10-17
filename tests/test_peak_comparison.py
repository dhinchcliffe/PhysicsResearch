"""Regression guard for the non-observable optimizer location under roundoff."""
from tools.compare_results import compare_numeric, PEAK_LOCATION_PATH

def test_flat_argmax_roundoff_is_tolerated_but_not_large_drifts():
    # Same peak height up to 2e-16; SciPy can choose nearby equivalent coordinates.
    expected=407.9285872556609
    observed=407.9285932952039
    assert compare_numeric(expected,observed,PEAK_LOCATION_PATH)==[]
    assert compare_numeric(expected,expected+0.001,PEAK_LOCATION_PATH)
    
def test_peak_height_remains_strict():
    path="dp_reproduction.json/example/numerical_peak_negativity"
    expected=0.042844724244786574
    assert compare_numeric(expected,expected,path)==[]
    assert compare_numeric(expected,expected+0.000001,path)

def test_all_other_numeric_fields_keep_existing_precision():
    assert compare_numeric(123.456,123.456000005,"dp_reproduction.json/other")
    assert compare_numeric(0.45,0.45+1e-8,"cycle01.json/signal")
