# function which return reverse of a string 
def reverse(p): 
    return p[::-1] 
  
def isPalindrome(p): 
    # Calling reverse function 
    rev = reverse(p) 
  
    # Checking if both string are equal or not 
    if (p == rev): 
        return True
    return False
  
  
# Driver code 
p = raw_input()
ans = isPalindrome(p) 
  
if ans == 1: 
    print("yes") 
else: 
    print("no")
