# Purpose: Find the largest palindrome made from the product of two 3-digit numbers
# Preconditions: Minimum and Maximum values
# Postconditions: Outputs palindrome to the user
def maxPalindrome(min,max):
    ans = 0
    for x in range(min,max + 1): # max + 1 b/c range isn't inclusive on the stop step
        for y in range(x + 1, max + 1):
            if x * y > ans and str(x * y)==(str(x * y)[::-1]): # [::-1] is the inverse string operator [start:stop:step]
                ans = x * y
    return ans

def main():
    print(maxPalindrome(100,999)) # [100,999] is the range of any 3 digit number
    
main() 

# Beginning to separate problems into separate functions to experiment with purity