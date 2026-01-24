from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def check_sorted(nums):
            if len(nums) <= 1:
                return True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        res = 0
        while not check_sorted(nums):
            min_idx = -1
            my_min = float('inf')
            for idx in range(1, len(nums)):
                curr_sum = nums[idx] + nums[idx - 1]
                if curr_sum < my_min:
                    min_idx = idx
                    my_min = curr_sum
            p1, p2 = nums[min_idx - 1], nums[min_idx]
            nums.pop(min_idx - 1)
            nums.pop(min_idx - 1)
            nums.insert(min_idx - 1, p1 + p2)
            res += 1
        return res

print(Solution().minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))