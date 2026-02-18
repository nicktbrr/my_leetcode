class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = (n & 1)
        n >>= 1
        while n != 0:
            if prev == (n & 1):
                return False
            prev = (n & 1)
            n >>= 1
        return True



