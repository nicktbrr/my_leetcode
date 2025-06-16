from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # if len(nums) < 2:
        #     return -1

        # res = -1
        # for idx in range(len(nums) - 1):
        #     remaining = nums[idx + 1:]
        #     if remaining:
        #         temp = max(remaining) - nums[idx]
        #         if temp > res and temp > 0:
        #             res = temp
        # return res

        if len(nums) < 2:
            return -1
        res = -1
        minN = float('inf')
        for n in nums:
            if n < minN:
                minN = n
            elif n - minN > 0:
                res = max(res, n - minN)
        return res
