from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for l in range(len(nums)):
            r = l
            if l % 2 == 0:
                while nums[r] % 2 == 1:
                    r += 1
            else:
                while nums[r] % 2 == 0:
                    r += 1
            nums[l], nums[r] = nums[r], nums[l]
        return nums

print(Solution().sortArrayByParityII(nums = [4,2,5,7]))