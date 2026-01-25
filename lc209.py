from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                res = min(res, r - l)
                curr_sum -= nums[l]
                l += 1
        return res + 1 if res != float('inf') else 0


print(Solution().minSubArrayLen(target = 4, nums = [1,4,4]))
print(Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))