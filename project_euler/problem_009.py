"""
Solution for Project Euler problem 009
https://projecteuler.net/about

Problem 009 asks for the product of the Pythagorean triplet's terms whose sum equals 1000.

Solution uses a direct approach, testing all possible combinations of a and b to find the missing c.
"""

def Special_triplet():
    for a in range(1,500):
        for b in range(a+1,500):
            c_square = a**2 + b**2
            c = c_square**.5
            if c.is_integer():
                sum = a + b + int(c)
                if sum == 1000:
                    return(a,b,c,sum)
    return("Special triplet not found!")

a,b,c,sum = Special_triplet()
print(a)
print(b)
print(c)
print(sum)
print('Product of a*b*c: ', a*b*c)