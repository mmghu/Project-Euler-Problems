# Purpose: Sum all of the primes below two million
# Preconditions: None
# Postconditions: Outputs sum to user
from math import sqrt

def main():
    n = 2000000
    sum = 0
    booleanList = [True] * n
    
    # Use Sieve of Eratosthenese
    for i in range(2,int(sqrt(n))):
        if(booleanList[i]):
            for j in range(i**2,n,i):
                booleanList[j] = False
    
    # Sum all instances of true
    for i in range(2,len(booleanList)):
        if(booleanList[i]):
            sum += i
    
    # Output sum
    print(sum)
    
main()