from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        s_hbar = sorted(hBars)
        s_vbar = sorted(vBars)
        max_con_h = 1
        con_h = 1
        for i in range(1, len(s_hbar)):
            if s_hbar[i-1] + 1 == s_hbar[i]:
                con_h += 1
                max_con_h = max(max_con_h, con_h)
            else:
                con_h = 1

        max_con_v = 1
        con_v = 1
        for i in range(1, len(s_vbar)):
            if s_vbar[i - 1] + 1 == s_vbar[i]:
                con_v += 1
            else:
                con_v = 1
            max_con_v = max(max_con_v, con_v)
        return (min(max_con_h, max_con_v) + 1)**2

n = 2
m = 3
hBars = [2,3]
vBars = [2,4]
vBars = []

print(Solution().maximizeSquareHoleArea(n, m, hBars, vBars))