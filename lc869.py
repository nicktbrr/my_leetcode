class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        d1 = {}
        for c in str(n):
            d1[c] = d1.get(c, 0) + 1
        curr = 1
        while curr < 10**9:
            d2 = {}
            for c in str(curr):
                d2[c] = d2.get(c, 0) + 1
            if d2 == d1:
                return True
            curr *= 2
        return False