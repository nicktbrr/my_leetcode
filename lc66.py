from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = list(str(int("".join(str(num) for num in digits)) + 1))
        return [int(i) for i in temp]

print(Solution().plusOne(digits = [9]))
