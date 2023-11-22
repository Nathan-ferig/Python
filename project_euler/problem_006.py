"""
Solution for Project Euler problem 006
https://projecteuler.net/about

Problem 006 asks for the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solution were generalized to find the answer for any range of natural numbers. 
"""

def Sum_Of_Squares(max_number: int = 10, min_number: int = 1) -> int:
    """Computes the sum of the squares"""
    sum: int = 0
    for i in range(min_number,max_number+1):
        sum += i*i
    return sum

def Square_Of_Sum(max_number: int = 10, min_number: int = 1) -> int:
    """Computes the square of the sum"""
    sum: int = 0
    for i in range(min_number,max_number+1):
        sum += i
    sum *= sum
    return sum

def Difference(max_number: int = 10, min_number: int = 1) -> int:
    """Computes the difference between the square of the sum
    and the sum of the squares"""
    return Square_Of_Sum(max_number,min_number) - Sum_Of_Squares(max_number,min_number)

print(Difference(100))
