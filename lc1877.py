from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        nums = sorted(nums)
        my_max = 0
        while l < r:
            my_max = max(my_max, nums[l] + nums[r])
            l += 1
            r -= 1
        return my_max

print(Solution().minPairSum(nums = [3,5,4,2,4,6]))