from typing import List
from math import ceil

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = ceil(stone_sum / 2)
        dp = {}
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_sum - total))
            if (i, total) in dp:
                return dp[(i, total)]
            t1 = dfs(i + 1, total)
            t2 = dfs(i + 1, total + stones[i])
            dp[(i, total)] = min(t1, t2)
            return dp[(i, total)]

        return dfs(0, 0)


print(Solution().lastStoneWeightII(stones = [2,7,4,1,8,1]))
print(Solution().lastStoneWeightII(stones = [31,26,33,21,40]))
print(Solution().lastStoneWeightII(stones = [1,1,1,1]))
