from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        r = []
        for idx, n in enumerate(nums):
            res = -1
            b = 1
            while n & b != 0:
                res = n - b
                b <<= 1
            r.append(res)
        return r

print(Solution().minBitwiseArray([2,3,5,7,47]))