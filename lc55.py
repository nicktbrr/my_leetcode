from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump_idx = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= can_jump_idx:
                can_jump_idx = i
        return not can_jump_idx


nums = [3,0,8,2,0,0,1]
res = Solution().canJump(nums)
print(res)