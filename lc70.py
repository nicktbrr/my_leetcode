class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            next = dp[-1] + dp[-2]
            dp.append(next)
        return dp[n - 1]


print(Solution().climbStairs((5)))