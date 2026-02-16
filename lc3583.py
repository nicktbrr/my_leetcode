from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        prev = {}
        res = 0
        for n in nums:
            left = prev.get(n * 2, 0)
            prev[n] = prev.get(n, 0) + 1
            right = counts.get(n * 2, 0) - prev.get(n * 2, 0)
            res += left * right
        return res % (10**9 + 7)

print(Solution().specialTriplets( nums = [0,0,0]))