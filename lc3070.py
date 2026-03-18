from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        pre = [[0] * n for _ in range(m)]
        for row in range(m):
            row_sum = 0
            for col in range(n):
                row_sum += grid[row][col]
                if row - 1 >= 0:
                    pre[row][col] = row_sum + pre[row-1][col]
                    continue
                pre[row][col] = row_sum
        for row in range(m):
            for col in range(n):
                if pre[row][col] <= k:
                    res += 1
        return res

print(Solution().countSubmatrices(grid = [[7,2,9],[1,5,0],[2,6,6]], k = 20))
# print(Solution().countSubmatrices([[7,6,3],[6,6,1]], k = 18))