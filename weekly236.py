class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunction(x):
            if x == 0:
                return 0
            elif x > 0:
                return 1
            else:
                return -1

        prod = 1
        for x in nums: prod *= x
        return signFunction(prod)


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1, n+1)]
        pos = 0
        while len(friends) > 1:
            pos = (pos + k - 1) % len(friends)
            friends.remove(friends[pos])
            pos = pos % len(friends)
        return friends[0]

from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(obstacles))]
        dp[0][0], dp[0][2] = 1, 1
        for n, o in enumerate(obstacles):
            if n == 0:
                continue
            for lane in range(3):
                if obstacles[n] == lane + 1:
                    dp[n][lane] = float('inf')
                else:
                    dp[n][lane] = dp[n-1][lane]

            best_reach = min(dp[n])
            for lane in range(3):
                if obstacles[n] != lane + 1:
                    dp[n][lane] = min(dp[n][lane], best_reach + 1)
        return min(dp[-1])