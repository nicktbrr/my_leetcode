from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(start: int, end: int) -> None:
            if start >= end:
                return
            pivot = nums[-1]
            l, r = start, end - 1
            while l <= r:
                if nums[l] >= pivot > nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] < pivot:
                    l += 1
                if nums[r] >= pivot:
                    r -= 1
            nums[l], nums[end] = nums[end], nums[l]
            quicksort(start, l - 1)
            quicksort(l + 1, end)
        quicksort(0, len(nums) - 1)


nums = [2,0,2,1,1,0]
Solution().sortColors(nums)
print(nums)