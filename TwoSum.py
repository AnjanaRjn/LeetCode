from typing import List

class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]

            if y in h and h[y] != i:
                return [i, h[y]]

solution_instance = Solution()
result = solution_instance.TwoSum([3, 7, 2, 15], 9)
print(result)
