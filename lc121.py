class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        start = prices[0]
        for p in prices[1:]:
            if p - start > profit:
                profit = p - start
            elif p < start:
                start = p
        return profit