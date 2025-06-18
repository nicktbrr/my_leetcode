from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        s = sorted(nums)
        res = []
        prev = 0
        for i in range(2, len(nums), 3):
            if s[i] - s[prev] > k:
                return []
            res.append(s[prev:i + 1])
            prev = i + 1
        return res

nums = [1,3,4,8,7,9,3,5,1]
k = 2
print(Solution().divideArray(nums, k))