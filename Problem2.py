# Purpose: Find the sum of the even valued terms
# Preconditions: None
# Postconditions: Prints sum of even valued terms to the user
def main():
    twoStep = 1 # number two steps before current number
    oneStep = 2 # number one step before current number
    current = 0 # variable to represent current number
    
    sum = 2
    
    while current < 4000000:
        # generate a fibonacci sequence
        current = twoStep + oneStep
        twoStep = oneStep
        oneStep = current
        
        # check if even number
        if(current % 2 == 0):
            sum += current #add to current
        
    print(sum)
    
main()