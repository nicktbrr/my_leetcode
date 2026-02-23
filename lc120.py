from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]
        for row in range(2, len(triangle)):
            for col in range(len(triangle[row])):
                if col == 0:
                    triangle[row][col] += triangle[row-1][col]
                elif col == len(triangle[row]) - 1:
                    triangle[row][col] += triangle[row-1][col-1]
                else:
                    triangle[row][col] += min(triangle[row-1][col-1], triangle[row-1][col])
        return min(triangle[-1])