"""
python -m doctest -v doctest_example.py
"""

def least_common_multiple(a: int,b: int) -> int:
    """Find the least common multiple of two given numbers
    
    >>> least_common_multiple(3,5)
    15

    >>> least_common_multiple(2,8)
    8

    >>> least_common_multiple(8,12)
    24

    >>> least_common_multiple(12,8)
    24
    
    """
    c = greatest_common_factor(a,b)
    return int((a*b)/c)

def greatest_common_factor(a: int,b: int) -> int:
    """Find the greatest common factor of two given numbers
    
    >>> greatest_common_factor(15,35)
    5

    >>> greatest_common_factor(48,72)
    24

    >>> greatest_common_factor(35,15)
    5

    >>> greatest_common_factor(7,5)
    1
    """
    n = 0
    if a > b:
        while b != 0:
            n = a % b
            a = b
            b = n
        return int(a)
    else:
        while a != 0:
            n = b % a
            b = a
            a = n
        return int(b)

print(least_common_multiple(3,5))