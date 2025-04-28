from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        temp_min = -1
        temp_max = -1
        invalid = -1
        count = 0
        for idx, num in enumerate(nums):
            if num == minK:
                temp_min = idx
            if num == maxK:
                temp_max = idx
            elif maxK < num or minK > num:
                invalid = idx
            if maxK != -1 and minK != -1:
                count += max(min(temp_min, temp_max) - invalid, 0)
        return count


s = Solution()
nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
nums = [1,1,1,1]
minK = 1
maxK = 1
print(s.countSubarrays(nums, minK, maxK))