from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remain = sum(nums) % p
        if remain == 0:
            return 0
        seen = {0: -1}
        curr_sum = 0
        res = len(nums)
        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) % p
            prefix = (curr_sum - remain + p) % p
            if prefix in seen:
                dist = i - seen[prefix]
                res = min(res, dist)
            seen[curr_sum] = i
        return -1 if res == len(nums) else res

print(Solution().minSubarray(nums = [3,1,4,2], p = 6))




