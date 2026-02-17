from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last_seen = nums[0] - k
        res = 1
        for n in nums[1:]:
            placement = max(last_seen + 1, n - k)
            if last_seen < n + k:
                res += 1
                last_seen = placement
        return res




print(Solution().maxDistinctElements([1,1,1,1,1,1,1,1,5,5,5], 3))

