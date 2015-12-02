# Purpose: Find the largest prime factor of 600851475143 
# Preconditions: None
# Postconditions: Outputs largest prime factor
def main():
    num = 600851475143 
    acc = 2
    
    while acc**2 < num:
        while num % acc == 0:
            num /= acc
        acc += 1
    
    print(int(num))
main()