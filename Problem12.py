# Purpose: Calculate first triangle number with over 500 divisors
# Preconditions: None
# Postconditions: Outputs first triangle number with 500 or more divisors
from functools import reduce
from sys import *

def numFactors(n): # returns number of factors using list comprehension  
    return len(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def triangle(n): # return nth triangle number
    return (n * (n + 1))/2

def main():
    # accumulator value
    curr = 1
    
    # While the nth triangle number has less than 500 factors
    while numFactors(triangle(curr)) < 500:
        curr += 1 # keep incrementing
    
    # Output number 
    print(triangle(curr))
    
main()