from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1

        for i in range(1, rows):
            obstacleGrid[i][0] = 0 if (obstacleGrid[i][0] == 1) or (obstacleGrid[i - 1][0] == 0) else 1
        for i in range(1, cols):
            obstacleGrid[0][i] = 0 if (obstacleGrid[0][i] == 1) or (obstacleGrid[0][i - 1] == 0) else 1

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] == 1:  # If it's an obstacle
                    obstacleGrid[row][col] = 0
                else:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
        return obstacleGrid[-1][-1]



print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]
))


