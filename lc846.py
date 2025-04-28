import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = {}
        for h in hand:
            counts[h] = 1 + counts.get(h, 0)
        min_h = list(counts.keys())
        heapq.heapify(min_h)
        while min_h:
            min_val = min_h[0]
            for i in range(min_val, min_val + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    if i != min_h[0]:
                        return False
                    else:
                        heapq.heappop(min_h)
        return True











hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

s = Solution()
print(s.isNStraightHand(hand, groupSize))