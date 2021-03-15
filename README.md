# PyMM
A python implementation of XKCD's Geothmetic Meandian ( https://xkcd.com/2435/ )

Simply run 
```python
    from GMDN import GMDN

    GMDN([1, 1, 2, 3, 5])
    >>> 2.0890
```

GMDN can also be used to get a tuple of (arithmetic mean, geometric mean, median), using geothmetic_mean found in GMDN.helpers:
```python
    from GMDN.helpers import geothmetic_meandian

    geothmetic_meandian([1, 1, 2, 3, 5])
    >>> (2.4, 1.97435048583482, 2)
```