from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        d = {}
        for p in power:
            d[p] = d.get(p, 0) + p
        pows = sorted(d.keys())

        dp = [0] * (len(pows) + 1)
        j = 0
        for i in range(len(pows)):
            while pows[j] < pows[i] - 2:
                j += 1
            dp[i + 1] = max(dp[i], d[pows[i]] + dp[j])

        return dp[len(pows)]


        # pows = sorted(d.items(), key=lambda x: x[0])
        # memo = {}
        # def max_at_idx(idx):
        #     if idx >= len(pows):
        #         return 0
        #     if idx in memo:
        #         return memo[idx]
        #     valid_idx = idx + 1
        #     while valid_idx < len(pows) and pows[idx][0] + 2 >= pows[valid_idx][0]:
        #         valid_idx += 1
        #     max_dmg = max(pows[idx][1] + max_at_idx(valid_idx), max_at_idx(idx + 1))
        #     memo[idx] = max_dmg
        #     return max_dmg
        # return max_at_idx(0)

print(Solution().maximumTotalDamage(power = [7,1,6,6]))