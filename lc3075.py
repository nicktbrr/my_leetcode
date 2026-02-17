class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        dec = 0
        start = 0
        while k > 0:
            res += max(happiness[start] - dec, 0)
            start += 1
            k -= 1
            dec += 1
        return res