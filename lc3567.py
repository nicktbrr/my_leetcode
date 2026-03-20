from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        res = []
        m,n = len(grid), len(grid[0])
        for r in range(0, m - k + 1):
            temp_list = []
            for c in range(0, n - k + 1):
                t = [row[c:c+k] for row in grid[r:r+k]]
                l = sorted(set(sum(t, [])))
                temp_res = float('inf')
                for i in range(1, len(l)):
                    temp_res = min(temp_res, abs(l[i] - l[i-1]))
                if temp_res == float('inf'):
                    temp_res = 0
                temp_list.append(temp_res)
            res.append(temp_list)

        return res

print(Solution().minAbsDiff(grid = [[1,-2,3],[2,3,5]], k = 2))