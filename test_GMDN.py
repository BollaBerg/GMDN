import GMDN

def test_GMDN():
    assert GMDN.GMDN([1, 1, 2, 3, 5]) == 2.0890566336242085

def test_GMDN_with_limit():
    assert GMDN.GMDN([1, 1, 2, 3, 5], 1) == 2

def test_median():
    assert GMDN.helpers._median([1, 3, 5, 2, 4]) == 3

def test_arithmetic_mean():
    assert GMDN.helpers._arithmetic_mean([1, 3, 5, 2, 4]) == 3

def test_geometric_mean():
    assert round(GMDN.helpers._geometric_mean([1, 3, 5, 2, 4]), 4) == 2.6052

def test_geothmetic_meandian():
    assert (GMDN.helpers.geothmetic_meandian([1, 1, 2, 3, 5])
            == (2.4, 1.97435048583482, 2))