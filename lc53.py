from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for n in nums[1:]:
            if curr_sum + n > n:
                max_sum = max(max_sum, curr_sum + n)
                curr_sum = curr_sum + n
            else:
                curr_sum = n
                max_sum = max(max_sum, n)
        return max_sum






t = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
t = Solution().maxSubArray([5,4,-1,7,8])
print(t)