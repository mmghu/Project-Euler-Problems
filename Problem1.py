# Purpose: Find the sum of all the multiples of 3 or 5 below 1000
# Preconditions: None
# Postconditions: Program outputs correct sum

def main():
    # counter variable for while loop
    counter = 1000
    sum = 0
    
    while counter != 0: # counting backwards by 1
        counter = counter - 1
        if(counter % 3 == 0): # if divisible by 3
            sum += counter # add to sum
        else: # if not divisible by 3
            if(counter % 5 == 0): # let see if divisible by 5
                sum += counter # add to sum
        
    print(sum)
main()