from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_max = float('-inf')
        d= {float('-inf'): 0}
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > d[my_max]:
                my_max = num
        return my_max


print(Solution().majorityElement([6,5,5]))