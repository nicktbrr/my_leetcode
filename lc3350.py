from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        pairs = []
        n = len(nums)
        curr = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                curr += 1
            else:
                pairs.append(curr)
                curr = 1
        pairs.append(curr)
        res = 1
        for i in range(1, len(pairs)):
            res = max(res, min(pairs[i - 1], pairs[i]), pairs[i - 1] // 2)
        res = max(res, pairs[-1] // 2)
        return res


print(Solution().maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1]))