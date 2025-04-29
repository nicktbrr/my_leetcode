from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        ct = 0
        left = 0
        max_count = 0

        for right in range(n):
            # Subarray end is max.
            if nums[right] == m: max_count += 1

            # Shrink until k not met.
            while max_count >= k:
                if nums[left] == m: max_count -= 1
                left += 1

            # Where left ends up is number of valid subarrays.
            # Ex: index 2 = 2 valid starts (index 0 and index 1)
            ct += left

        return ct


print(Solution().countSubarrays([1,3,2,3,3], 2))