from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # left = 0
        # right = left + 1
        # max_left = nums[0]
        # min_right = min(nums[right:])
        # while right != len(nums):
        #     if max_left <= min_right:
        #         break
        #     right += 1
        #     max_left = max(nums[right - 1], max_left)
        #     if min_right < nums[right]:
        #         min_right = min(nums[right:])
        # return right
        max_l, max_r = nums[0], nums[0]
        current = 0
        for i in range(1, len(nums)):
            max_r = max(max_r, nums[i])
            if nums[i] < max_l:
                current = i
                max_l = max_r
        return current + 1

print(Solution().partitionDisjoint([5,0,3,8,1,6,9]))
print(Solution().partitionDisjoint([1,1,1,0,6,12]))


