from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        v_temp = [1] + vFences + [n]
        h_temp = [1] + hFences + [m]

        h_diff = []
        for i, h1 in enumerate(h_temp):
            for h2 in h_temp[i + 1:]:
                h_diff.append(abs(h1 - h2))
        v_diff = []
        for i, v1 in enumerate(v_temp):
            for v2 in v_temp[i + 1:]:
                v_diff.append(abs(v1 - v2))
        temp = set(v_diff).intersection(h_diff)
        return -1 if not temp else max(temp)**2 % (10**9 + 7)

print(Solution().maximizeSquareArea(m = 6, n = 7, hFences = [2], vFences = [4]))
print((Solution().maximizeSquareArea( m = 4, n = 3, hFences = [2,3], vFences = [2])))

