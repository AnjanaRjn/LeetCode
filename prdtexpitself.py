from typing import List
class solution:
    def productExceptItself(self, nums: list[int]) -> List[int]:
        res = [1] * (len(nums)) # creating a result array with one's having same length as nums
        
        prefix =  1
        for i in range(len(nums)):
            res[i] = prefix #stores the product of all elements before the i-th index.
            prefix *= nums[i]

        postfix = 1
        for i  in range(len(nums)-1, -1, -1): # starting from the end of the input array
            res[i] *= postfix # multiplying the prefix and postfix
            postfix *= nums[i]    

        return res   


nums = [1, 2, 3, 4]
solution_instance = solution()
print(solution_instance.productExceptItself(nums))