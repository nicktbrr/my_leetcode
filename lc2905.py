from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        l, r  = 0, indexDifference
        while True:
            if abs(nums[l] - nums[r]) >= valueDifference:
                return [l,r]
            elif r + 1 < len(nums) and nums[r] <= nums[r + 1]:
                r += 1
            elif l - r >= indexDifference:
                l += 1
            else:
                r += 1

print(Solution().findIndices(nums = [1,2,0,3,4,1,3,8,1], indexDifference = 3, valueDifference = 6))