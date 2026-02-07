from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        res = 0
        for r in range(len(nums)):
            while nums[r] > nums[l] * k:
                l += 1
            res = max(res, r -l + 1)
        return len(nums) - res

print(Solution().minRemoval(nums = [2,1,5], k = 2))
print(Solution().minRemoval([1,6,2,9], k = 3))
print(Solution().minRemoval([4,6], k = 2))
print(Solution().minRemoval([20,5,11], k=2))
print(Solution().minRemoval([9,29,13], 2))