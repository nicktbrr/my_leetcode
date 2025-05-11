class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        num_odd = 0
        for n in arr:
            if n % 2 == 1:
                num_odd += 1
            else:
                num_odd = 0
            if num_odd == 3:
                return True
        return False