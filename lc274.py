from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        buckets = [0] * (len(citations) + 1)
        n = len(citations)
        for c in citations:
            if c > n:
                buckets[-1] += 1
            else:
                buckets[c] += 1
        cum_sum = 0
        for i in range(len(buckets) - 1, -1, -1):
            cum_sum += buckets[i]
            if cum_sum >= i:
                return i
        return 0

citations = [3,0,6,1,5]
citations = [1,3,1]
citations = [3,2,6,4,1,1,2,3,9,7,5,4]
# citations = [1]
# citations = [100]

print(Solution().hIndex(citations))