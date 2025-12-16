from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum == target:
                return [l + 1, r + 1]

            if curr_sum < target:
                l += 1
            else:
                r -= 1
        return []

numbers = [2,7,11,15]
numbers = [-1000,-1,0,1]
target = 9
target = 1

print(Solution().twoSum(numbers, target))