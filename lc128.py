from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            temp_long = 0
            if n - 1 not in s:
                temp_long += 1
                while n + temp_long in s:
                    temp_long += 1
            res = max(res, temp_long)
        return res



print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))