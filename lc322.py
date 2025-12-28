from typing import List

#take 2 almost got it

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf') for i in range(amount + 1)]
        memo[0] = 0
        for coin in sorted(coins):
            for i in range(coin, len(memo)):
                memo[i] = min(memo[i], memo[i - coin] + 1)
        return memo[amount] if memo[amount] != float('inf') else -1


coins = [1,2,5]
amount = 11

print(Solution().coinChange(coins, amount))

