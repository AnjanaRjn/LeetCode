from typing import List
class solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0: #if the current sum is negative, it is set to 0
             curSum = 0
            curSum += n 
            maxSub = max(maxSub, curSum)
        return(maxSub)    
 
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution_instance = solution()
print(solution_instance.maxSubArray(nums))
