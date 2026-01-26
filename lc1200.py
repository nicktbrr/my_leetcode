from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        d = {}
        min_diff = float('inf')
        temp = sorted(arr)
        for i in range(1, len(temp)):
            min_diff = min(min_diff, abs(temp[i - 1] - temp[i]))
            d.setdefault(abs(temp[i - 1] - temp[i]), []).append([temp[i - 1], temp[i]])
        return d[min_diff]

