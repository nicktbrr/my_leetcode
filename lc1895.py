from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def check_square(i,j, l) -> bool:
            my_sum = sum(grid[i][j:j+l])
            for row in range(i, i+l):
                if sum(grid[row][j:j+l]) != my_sum:
                    return False
            for c in range(j, l + j):
                column_sum = sum(grid[r][c] for r in range(i, i + l))
                if column_sum != my_sum:
                    return False
            sum_d1 = sum(grid[i + k][j + k] for k in range(l))
            sum_d2 = sum(grid[i + k][j + l - 1 - k] for k in range(l))
            if sum_d1 != my_sum or sum_d2 != my_sum:
                return False
            return True

        rows, cols = len(grid), len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                for l in range(res + 1, min(rows - i, cols - j) + 1):
                    if check_square(i,j,l):
                        res = max(res, l)
        return res


print(Solution().largestMagicSquare(grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
print(Solution().largestMagicSquare(grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]))