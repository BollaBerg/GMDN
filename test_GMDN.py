import GMDN

def test_GMDN():
    assert round(GMDN.GMDN((1, 1, 2, 3, 5), 0.0001), 4) == 2.0890

def test_median():
    assert GMDN._median([1, 3, 5, 2, 4]) == 3

def test_arithmetic_mean():
    assert GMDN._arithmetic_mean([1, 3, 5, 2, 4]) == 3

def test_geometric_mean():
    assert round(GMDN._geometric_mean([1, 3, 5, 2, 4]), 4) == 2.6052