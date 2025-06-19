from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        mins = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    mins[row][col] = grid[row][col]
                elif row == 0:
                    mins[row][col] = grid[row][col] + mins[row][col - 1]
                elif col == 0:
                    mins[row][col] = grid[row][col] + mins[row - 1][col]
                else:
                    top = mins[row - 1][col]
                    left = mins[row][col - 1]
                    mins[row][col] = min(grid[row][col] + top, grid[row][col] + left)
        return mins[len(grid) - 1][len(grid[0]) - 1]



Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])