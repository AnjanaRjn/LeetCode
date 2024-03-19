from typing import List
class solution:
    def containsDuplicate(self,nums: List[int]) -> bool:
        hashset = set() # Create a set to store unique numbers
        for n in nums:
            if n in hashset:  # If the number is already in the set, it's a duplicate.
                return True
            else:
                hashset.add(n) # Add the number to the set if it's not already present in the set

        return False
    
solution_instance = solution()
nums = [1,2,3,4,2]
print(solution_instance.containsDuplicate(nums))                
