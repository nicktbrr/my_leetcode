from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        start_line = [0 for _ in range(fruits[-1][0] + 1)]
        for fruit in fruits:
            start_line[fruit[0]] = fruit[1]
        l = startPos - k if startPos - k > 0 else 0
        r = k - (startPos - l)
        curr_sum = 0
        if l + r < startPos:
            curr_sum = sum(start_line[l: startPos + 1 ])
        else:
            curr_sum = sum(start_line[l:r + 1])
        res = curr_sum
        l += 1
        while l < startPos:
            pass



print(Solution().maxTotalFruits([[0,9],[4,10],[5,7],[6,2],[7,4],[10,9]], 3, 7))