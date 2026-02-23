from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        last = {}
        dry = []

        for i, lake in enumerate(rains):
            if lake > 0:
                ans[i] = -1
                if lake in last:
                    prev = last[lake]
                    idx = bisect.bisect_right(dry, prev)
                    if idx == len(dry):
                        return []
                    dry_day = dry[idx]
                    ans[dry_day] = lake
                    dry.pop(idx) 
                last[lake] = i
            else:
                dry.append(i)  
        return ans