# function which return reverse of a string 
def reverse(n): 
    return n[::-1] 
  
def isPalindrome(n): 
    # Calling reverse function 
    rev = reverse(n) 
  
    # Checking if both string are equal or not 
    if (n == rev): 
        return True
    return False
  
  
# Driver code 
n = raw_input()
ans = isPalindrome(n) 
  
if ans == 1: 
    print("yes") 
else: 
    print("no")
