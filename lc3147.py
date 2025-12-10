class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy) - 1
        dp = energy[:]
        mx = float("-inf")

        for i in range(n, -1, -1):
            if i + k <= n:
                dp[i] += dp[i + k]
            mx = max(mx, dp[i])
        return mx