"""
Doctest example:

Doctest module executes the code and verify if it work exactly as intended.

Run the test at terminal with:
python -m doctest -v doctest_example.py

More information about doctest please visit:
https://docs.python.org/3/library/doctest.html
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
    value_test(a)
    value_test(b)
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
    value_test(a)
    value_test(b)
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

def factorial(n: int = 5) -> int:
    """This function calculates the factorial of n:

    >>> factorial(5)
    24

    >>> factorial(1)
    1

    >>> factorial(0)
    1

    """
    value_test(n)
    if type(n) == float: n = int(n)
    factorial = 1
    for i in range(1,n):
        factorial *= i
    return factorial

def value_test(n: int) -> None:
    """This function runs validation tests for a given number n:

    >>> value_test(5)
    
    >>> value_test(-5)
    Traceback (most recent call last):
        ...
    ValueError: Value must be a positive integer.

    >>> value_test(5.5)
    Traceback (most recent call last):
        ...
    ValueError: Value must be an integer.

    >>> value_test(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: Value is too large.

    """
    if n < 0:
        raise ValueError('Value must be a positive integer.')
    if int(n) != n:
        raise ValueError('Value must be an integer.')
    if n + 1 == n:
        raise OverflowError('Value is too large.')

# print(least_common_multiple(3,5))
# print(greatest_common_factor(3,5))
print(factorial(5.0))