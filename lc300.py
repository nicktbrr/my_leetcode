from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))

