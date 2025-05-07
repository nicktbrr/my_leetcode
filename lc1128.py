from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        res = 0
        for domino in dominoes:
            s_dom = tuple(sorted(domino))
            d[s_dom] = 1 + d.get(s_dom, 0)
        for k, v in d.items():
            if v >= 2:
                res += v * (v -1) // 2
        return res



s = Solution()
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(s.numEquivDominoPairs(dominoes))