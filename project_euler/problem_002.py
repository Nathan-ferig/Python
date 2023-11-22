"""
Solution for Project Euler problem 002
https://projecteuler.net/about

Problem 002 asks for the sum of all even-valued terms in the Fibonacci sequence whose values do not exceed four million. Two solutions are given:

The fist solution computes all terms of the Fibonacci sequence and verify if they are even or odd.

The second solution uses a property of the Fibonacci sequence: there is always two odd terms between two consecutibe even numbers.
"""

def Even_Fibonacci_Sum(n: int = 1000) -> int:
    """Computes all terms in the sequence and verify if they are even or odd."""
    a: int = 1
    b: int = 2
    EFS: int = 0
    while (b < n):
        if b % 2 == 0: EFS += b
        a, b = b, a + b
    return EFS

def Sum_Even_Fibonnaci(n: int = 1000) -> int:
    """Computes just the even terms in the sequence.
    This is more efficient, because it does not need
    to test the number to know if it is even of odd"""
    a: int = 1
    b: int = 2
    EFS = 0
    while (b < n) or (a < n):
        EFS += b
        a, b = a + 2*b, 2*a + 3*b
    return EFS
    
print(Even_Fibonacci_Sum())
print(Sum_Even_Fibonnaci())