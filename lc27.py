from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r = 0, len(nums)
        while l < r:
            if nums[l] == val:
                r -= 1
                while nums[r] == val and r > l:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1
        return l

print(Solution().removeElement([3,2,2,3], 3))