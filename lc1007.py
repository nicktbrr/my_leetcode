from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        min_swap = float('inf')
        for target in [tops[0], bottoms[0]]:
            m_top, m_bottom = 0, 0
            valid = True
            for idx, (top, bottom) in enumerate(zip(tops, bottoms)):
                if not (top == target or bottom == target):
                    valid = False
                    break
                if top != target:
                    m_top += 1
                if bottom != target:
                    m_bottom += 1
            if valid:
                min_swap =  min(min_swap, m_top, m_bottom)
        return -1 if min_swap == float('inf') else min_swap






s = Solution()
tops = [1,2,1,1,1,2,2,2]
bottoms = [2,1,2,2,2,2,2,2]
print(s.minDominoRotations(tops, bottoms))