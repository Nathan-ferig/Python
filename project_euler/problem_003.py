"""
Solution for Project Euler problem 003
https://projecteuler.net/about

Problem 003 asks for the largest prime factor of the number 600851475143.

Solution runs division tests for the number n and verify it the divisors are prime or not.
"""

def IsPrime(n: int) -> bool:
    """Verify if the number is prime and return True or False"""
    if n == 2:          # Tests if the number 2 as a prime factor of n
        return True
    elif n % 2 == 0:    # Tests if the number n is even
        return False

    # tests if the number n has an odd divisor
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

def Largest_Prime_Factor(n: int = 13195) -> int:
    """Find the largest prime factor of number n"""

    LPF = 1

    # tests if the number has 2 as a prime factor
    if n % 2 == 0:
        LPF = 2
        return LPF

    # searches for odd prime factors
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            if IsPrime(i):
                LPF = i
    return LPF

print(Largest_Prime_Factor(600851475143))