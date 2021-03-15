"""
Helpers for GMDN

Functions
----------
    GMDN(nums, limit) -> float
    geothmetic_meandian(nums) -> tuple
    _arithmetic_mean(nums) -> float
    _geometric_mean(nums) -> float
    _median(nums) -> float

"""
import math
import statistics
import sys

def _arithmetic_mean(nums) -> float:
    """Return arithmetic mean of nums : (a1 + a2 + ... + an)/n"""
    return sum(nums) / len(nums)



def _geometric_mean(nums) -> float:
    """Return geometric mean of nums : n-root(a1 * a2 * ... * an)"""
    exponent = 1 / len(nums)
    product = math.prod(nums)
    return product ** exponent



def _median(nums) -> float:
    """Return median of nums : a{n/2}"""
    return statistics.median(nums)



def geothmetic_meandian(nums) -> tuple:
    """
    Calculate a tuple of (arithmetic mean, geometric mean, median)

    Parameters
    ----------
    nums : iterable of floats
        List of numbers to calculate from

    Returns
    ----------
    (float, float, float)
        A tuple consisting of (arithmetic mean, geometric mean, median)
        of nums

    Usage:
    >>> geothmetic_meandian([1, 1, 2, 3, 5])
    (2.4, 1.97435048583482, 2)
    """
    return (_arithmetic_mean(nums), _geometric_mean(nums), _median(nums))



def GMDN(nums, limit=0.00001) -> float:
    """
    Calculate the geothmetic meandian of a set of numbers

    Parameters
    ----------
    nums : iterable of floats
        List of numbers to calculate geothmetic meandian of
    limit : float
        Convergence limit (default 0.00001)

    Returns
    ----------
    float
        Median of the final result (where max - min <= limit)

    Usage:
    >>> GMDN([1, 1, 2, 3, 5])
    2.0890566336242085
    >>> GMDN([1, 1, 2, 3, 5], 1)
    2
    """
    MAX_RUNS = sys.maxsize * 2 + 1

    result = geothmetic_meandian(nums)
    for _ in range(MAX_RUNS):
        max_value = max(result)
        min_value = min(result)
        
        if max_value - min_value <= limit:
            return _median(result)
        
        result = geothmetic_meandian(result)
        
    raise ValueError(F"Results didn't converge in {MAX_RUNS} applications")