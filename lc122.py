from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = prices[0]
        for p in prices:
            if p > start:
                profit += p - start
            start = p
        return profit
