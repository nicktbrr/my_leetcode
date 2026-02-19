from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def BFS(r, c):
            q = [(r, c)]
            seen[r][c] = True
            while q:
                curr_r, curr_c = q.pop()
                for dx, dy in dirs:
                    new_r = curr_r + dx
                    new_c = curr_c + dy
                    if 0 <= new_r < m and 0 <= new_c < n:
                        if grid[new_r][new_c] == '1' and seen[new_r][new_c] == False:
                            q.insert(0, (new_r, new_c))
                            seen[new_r][new_c] = True
            return 1

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and seen[r][c] == False:
                    res += BFS(r, c)
        return res



print(Solution().numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))