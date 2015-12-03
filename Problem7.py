# Purpose: Find the 10001st prime number
# Preconditions: None
# Postconditions: Outputs 10001s prime to the user
from math import sqrt

def isPrime(acc):
    for i in range(3,int(sqrt(acc))+1,2): # checks odd numbers up to the square root of the number
        if(acc % i == 0):
            return False
    return True

def countPrimes():
    primes = 6
    acc = 13
    
    # Loop through all odd numbers, add up amount of primes
    while primes != 10001:
        acc += 2
        if isPrime(acc):
            primes += 1
    
    return acc

def main():
    print(countPrimes())
    
main()