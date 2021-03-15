"""
A python implementation of XKCD's Geothmetic Meandian

If arithmetic mean, geometric mean and median are not the same number,
it can be hard to tell which to use. The Geothmetic Meandian fixes this,
by finding where the mean, geometric mean and median converges.

The comic inspiring this can be found at https://xkcd.com/2435/

The module exposes GMDN (from GMDN.helpers) at the top level.

For more info, see https://github.com/BollaBerg/GMDN

Functions
----------
    GMDN(nums, limit) -> float

Modules
----------
    helpers

"""

from GMDN.helpers import GMDN