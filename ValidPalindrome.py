class Solution:
    def isPalindrome(self, s:str) -> bool:   #Example "A man, a plan, a canal: Panama" ->  "amanaplanacanalpanama" is a palindrome.
                                             # convert all uppercase letters into lowercase letters and removing all non-alphanumeric characters 
        n = len(s)       
        L = 0 # Left pointer at the beginning of the string
        R = n-1 # Right pointer at the end of the string

        while L < R: 
            if not s[L].isalnum(): # if the character at L is not alphanumeric, move one step ahead
                L +=1
                continue

            if not s[R].isalnum(): # if the character at R is not alphanumeric, move one step down
                R +=1
                continue

            if s[L].lower() != s[R].lower(): # after converting them to lower case, if the current characters at which both the pointers are placed are not same, return false.
                return False
            
            L += 1  # if they are the same, move L and R one step until they reach the same character
            R -= 1

        return True    