# Purpose: Calculate which number under one million has the longest Collatz sequence chain
# Preconditions: None
# Postconditions: Outputs number with the longest chain
def getLength(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = 3 * num + 1
            count += 1

    return count
    
def main():
    largest = 13
    largestVal = 10
    
    # Loop through possible values
    for i in range(2,1000000):
        temp = getLength(i)
        
        # Compare values and store largest so far
        if(temp > largestVal):
            largest = i
            largestVal = temp
    
    # Output largest value seen
    print(largest)
    
main()