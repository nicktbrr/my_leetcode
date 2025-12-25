from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

print(Solution().searchInsert(nums, target))