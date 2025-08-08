from typing import List


class Solution(object):
    def maxCollectedFruits(self, grid):
        n = len(grid)
        diag = 0

        # Diagonal
        for i in range(n):
            diag += grid[i][i]

        # Bottom left child
        dp = [[-inf] * (n + 1) for _ in range(n + 1)]  # Padding
        dp[n - 1][0] = grid[n - 1][0]  # Base case
        for col in range(1, n):  # Dont include start (1, ...)
            for row in range(col + 1, n):  # Avoid the diag
                dp[row][col] = max(
                    dp[row + 1][col - 1] + grid[row][col],  # Go up
                    dp[row][col - 1] + grid[row][col],  # Go mid
                    dp[row - 1][col - 1] + grid[row][col]  # Go down
                )

        # Top right child
        dp[0][n - 1] = grid[0][n - 1]  # Padding
        for row in range(1, n):  # Dont include start (1, ...)
            for col in range(row + 1, n):  # Avoid the diag
                dp[row][col] = max(
                    dp[row - 1][col - 1] + grid[row][col],  # Go left down
                    dp[row - 1][col] + grid[row][col],  # Go down
                    dp[row - 1][col + 1] + grid[row][col]  # Go right down
                )

        # return diag + left child + right child
        return diag + dp[n - 1][n - 2] + dp[n - 2][n - 1]





    # print(Solution().maxCollectedFruits( fruits = [[1,1],[1,1]]))
# print(Solution().maxCollectedFruits( fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]))
# print(Solution().maxCollectedFruits( fruits = [[27,86,54],[13,92,95],[7,99,61]]))
print(Solution().maxCollectedFruits( [[4,18,19,9,20,14],[16,4,4,16,15,16],[2,11,15,6,8,9],[6,7,11,17,7,6],[17,17,2,13,2,14],[16,9,6,14,7,16]]))