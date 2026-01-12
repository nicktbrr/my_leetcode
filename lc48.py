from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for row in range(n):
            for col in range(n//2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]
        print(matrix)


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution().rotate(matrix))