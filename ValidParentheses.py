class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # create a stack to enter all the characters one by one
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} # create a hashmap with all three kinds of brackets

        for c in s:
            if c in closeToOpen: # if it is a closing bracket, since they are the keys in the hashmap
                if stack and stack[-1] == closeToOpen[c]: #if the stack is non empty and the last value in the stack is an open bracket that matches the upcoming closing bracket
                    stack.pop() # remove the last pair that matched
                else: # if they dont match return false
                    return False
            else:  #if the charcter is an open bracket (they are not in closeToOpen, since they are not keys) 
                stack.append(c) # append it to the stack
        return True if not stack else False  # after this continues and if the stack is empty, since all the matching pairs are removed, return true
                                             # if the stack has brackets with no pair return false
                   
