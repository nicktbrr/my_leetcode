from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = []
        for idx, my_k in enumerate(nums):
            if my_k == key:
                keys.append(idx)
        res = []
        for idx, n in enumerate(nums):
            if n == key:
                res.append(idx)
            else:
                for key_idx in keys:
                    if abs(idx - key_idx) <= k:
                        res.append(idx)
                        break
        return res

print(Solution().findKDistantIndices([3,4,9,1,3,9,5], key = 9, k = 1))