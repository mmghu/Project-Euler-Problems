# Purpose: Find the smallest positive number that is evenly divisible by numbers [1,20]
# Preconditions: None
# Postconditions: Outputs number to the user
def isDivisible(counter):
    divisible = True
    for i in range(11,21): # Only need to check 11-20 b/c anything divisible by them is also divisible by 1-10
        if (counter % i) != 0:
            divisible = False
    
    return divisible # return whether or not a number is evenly divisible by all the numbers
        
def main():
    found = False # flag
    counter = 2520
    answer = -1
    
    while not found:
        if(counter % 19) == 0: # Less things are divisible by 19 so less operations
            if isDivisible(counter): # if it is divisible
                found = True
                answer = counter  # store the value
        counter += 20 # increment by the largest value 
    
    print(answer)

main()