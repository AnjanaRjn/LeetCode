from collections import Counter
class Solution(object):
    def isAnagram(self, s: str, t, str) -> bool :
        if len(s) != len(t): # if the length of the string does not match, there are not an anagram
         return False
        
        s_dict = Counter(s) # Frequency counter of s
        t_dict = Counter(t) # frequency counter of t

        return s_dict == t_dict # if all the key value pairs match, return true
    
