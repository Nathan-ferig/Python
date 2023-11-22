"""
Solution for Project Euler problem 005
https://projecteuler.net/about

Problem 005 asks for the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

Problem 005 states that 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. Therefore, the smallest number evenly divisible by 1 to 20 is also divisible by 2520 and we can use this information to make solution more efficient.

Solution runs division tests for all numbers multiple of 2520 and verify if they can be evenly divisible by 11 to 20.

Solution were optimized thanks to the insights shared at:
https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
"""

def smallest_multiple(initial: int = 2520) -> str:
    divisors = [11,12,13,14,15,16,17,18,19,20]

    for number in range(initial,999999999,initial):
        if all(number % i == 0 for i in divisors):
            return f'The solution is {number}'
    return 'No solution was found'

print(smallest_multiple())