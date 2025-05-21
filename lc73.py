from typing import List

class Solution:
    def set_row(self, matrix, row):
        for i in range(0, len(matrix[row])):
            matrix[row][i] = 0

    def set_col(self, matrix, col):
        for j in range(0, len(matrix)):
            matrix[j][col] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros[(r,c)] = 1
        for (r,c), _ in zeros.items():
            self.set_row(matrix, r)
            self.set_col(matrix, c)

s = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
print(matrix)
