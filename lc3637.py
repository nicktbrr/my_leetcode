from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 1

        while i < n and nums[i] > nums[i - 1]:
            i += 1
        inc1 = i - 1

        while i < n and nums[i] < nums[i - 1]:
            i += 1
        dec = i - 1

        while i < n and nums[i] > nums[i - 1]:
            i += 1
        inc2 = i - 1

        return inc1 < dec < inc2 and (inc1 != 0) and (inc1 != dec) and (inc2 == n - 1)



print(Solution().isTrionic([8,9,4,6,1]))