# Purpose: Find the product of the 3 pythagorean triplets where a + b + c = 1000
# Preconditions: None
# Postconditions: Prints product of a, b, and c to the user
from fractions import gcd     

def findTriplets():
    m = 1
    found = False
    answer = -1
    
    while not found:
        m += 1
        # check every n value
        for n in range(m-1, 0, -2):
            a = (m**2 - n**2)
            b = (2*m*n)
            c = (m**2 + n**2) 
            if (a + b + c) == 1000: # if sum of a,b, and c is 100
                answer = a * b * c
                found = True # we found the answer
    return answer

def main():
    print(findTriplets())  
    
main()