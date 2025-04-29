from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        my_sum = 0
        l, r = 0, 0
        count = 0
        while l < len(nums):
            while r < len(nums) and (my_sum + nums[r]) * (r - l + 1) < k:
                my_sum += nums[r]
                r += 1
            count += r - l
            if l == r:
                r += 1
            else:
                my_sum -= nums[l]
            l += 1
        return count






s = Solution()

print(s.countSubarrays([1,2,3,4,5], 10))