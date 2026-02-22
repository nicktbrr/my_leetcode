class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        last_idx = -1
        for i in range(32):
            if (n >> i) & 1:
                if last_idx != -1:
                    res = max(res, i -last_idx)
                last_idx = i
        return res
