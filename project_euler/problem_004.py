"""
Solution for Project Euler problem 004
https://projecteuler.net/about

Problem 004 asks for the largest palindrome made from the product of two 3-digit numbers.

Solution multiplies all two 3-digit numbers and verify if they are palindrome or not. 
"""

def largest_palindrome():
    palindrome = []
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            mult = i*j
            string = str(mult)
            if (string == string[ : : -1]):
                palindrome.append(mult)
    return max(palindrome)
    
print(largest_palindrome())