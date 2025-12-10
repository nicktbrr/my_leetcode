from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        i = 0
        for num in nums:
            if num not in d:
                d[num] = 1
                nums[i] = num
                i += 1
        return len(d)


