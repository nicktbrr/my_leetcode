from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        res = 0
        s = sorted(nums)
        r = 0
        l = 0
        while r != len(nums):
            if s[r] - s[l] > k:
                res += 1
                l = r
            r += 1
        return res + 1

print(Solution().partitionArray([3,6,1,2,5], 2))