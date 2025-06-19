class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 or col == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
        return grid[m - 1][n - 1]

Solution().uniquePaths(3,7)