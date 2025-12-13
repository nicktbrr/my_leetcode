from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp = [0] * len(nums)
        for i, num in enumerate(nums):
            if i + k >= len(nums):
                cp[(i + k) % len(nums)] = num
            else:
                cp[i + k] = num
        for i, num in enumerate(cp):
            nums[i] = num

nums = [1,2,3,4,5,6,7]
k = 3

Solution().rotate(nums, k)