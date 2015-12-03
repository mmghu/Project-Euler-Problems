# Purpose: Find the difference between the sum of squares and square of sums of the first hundered numbers
# Preconditions: None
# Postconditions: Outputs answer to the user

def sumOfSquares():
    answer = 0
    for i in range(1,101):
        answer += i**2
    return answer

def squareOfSum():
    answer = 0
    for i in range(1,101):
        answer += i
    return answer

def main():
    print(squareOfSum()**2 - sumOfSquares())
    
main()