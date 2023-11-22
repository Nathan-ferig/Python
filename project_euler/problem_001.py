"""
Solution for Project Euler problem 001
https://projecteuler.net/about

Problem 001 asks for the sum of all the multiples of 3 or 5 bellow 1000. Two solutions are given.

The first solution tries all numbers bellow 1000 and verifies if they follow the division rule. It's a simple solution and works fine.

The second solution uses arithmetic progression to find the sum of a serie. It is not as simple as the first solution, but it allows for a more generalization without losing performance.

Solutions were generalized to find the sum of all multiples of two given integers bellow any given integer.
"""


def sum_by_trial(n: int = 1000, a: int=3, b: int=5) -> int:
    """This solution tests all integers bellow n and check if they are multiples of a or b"""
    return sum(i for i in range(n) if (i % a ==0 or i % b == 0))

def sum_by_math(n: int = 1000, a: int=3, b: int=5) -> int:
    """This solution uses arithmetic progression the find the sum of a series:
    t1 is the sum of all multiples of a bellow n
    t2 is the sum of all multiples of b bellow n
    t3 is the sum of all commom numbers from t1 and t2
    thus the solution is t1 + t2 - t3
    """
    c = least_common_multiple(a,b)
    t1 = int((a/2)*(int((n-1)/a))*(int((n+a-1)/a)))
    t2 = int((b/2)*(int((n-1)/b))*(int((n+b-1)/b)))
    t3 = int((c/2)*(int((n-1)/c))*(int((n+c-1)/c)))
    return t1 + t2 - t3

def least_common_multiple(a,b):
    """Find the least common multiple of two given numbers"""
    c = greatest_common_factor(a,b)
    return (a*b)/c

def greatest_common_factor(a,b):
    """Find the greatest common factor of two given numbers"""
    n = 0
    if a > b:
        while b != 0:
            n = a % b
            a = b
            b = n
        return a
    else:
        while a != 0:
            n = b % a
            b = a
            a = n
        return b

print(sum_by_trial(1000,3,5))
print(sum_by_math(1000,3,5))