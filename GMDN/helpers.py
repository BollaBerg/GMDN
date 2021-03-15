import math
import statistics
import sys

def _arithmetic_mean(nums):
    return sum(nums) / len(nums)
    
def _geometric_mean(nums):
    exponent = 1 / len(nums)
    product = math.prod(nums)
    return product ** exponent
    
def _median(nums):
    return statistics.median(nums)

def geothmetic_meandian(nums):
    return (_arithmetic_mean(nums), _geometric_mean(nums), _median(nums))

def GMDN(nums, limit):
    """An implementation of https://xkcd.com/2435/ """
    MAX_RUNS = sys.maxsize * 2 + 1

    result = geothmetic_meandian(nums)
    for _ in range(MAX_RUNS):
        max_value = max(result)
        min_value = min(result)
        
        if max_value - min_value <= limit:
            return _median(result)
        
        result = geothmetic_meandian(result)
        
    raise ValueError(F"Results didn't converge in {MAX_RUNS} applications")