from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        my_set = {0}
        target_sum = sum(nums) // 2
        if sum(nums) % 2 == 1:
            return False
        for n in reversed(nums):
            temp_set = set()
            for item in my_set:
                if n + item == target_sum:
                    return True
                else:
                    temp_set.add(n + item)
            my_set = my_set.union(temp_set)
        return False

