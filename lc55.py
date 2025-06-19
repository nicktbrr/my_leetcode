from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finish = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= finish:
                finish = i
        return True if finish == 0 else False


nums = [3,2,1,0,4]
nums = [2,3,0,1,4]
print(Solution().canJump(nums))