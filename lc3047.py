from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        res = 0
        for i in range(len(bottomLeft)):
            for j in range(i + 1, len(bottomLeft)):

                max_b_x = max(bottomLeft[i][0], bottomLeft[j][0])
                min_t_x = min(topRight[i][0], topRight[j][0])

                max_b_y = max(bottomLeft[i][1], bottomLeft[j][1])
                min_t_y = min(topRight[i][1], topRight[j][1])

                if max_b_x < min_t_x and max_b_y < min_t_y:
                    area = min(min_t_x - max_b_x, min_t_y - max_b_y)**2
                    res = max(res, area)

        return res



print(Solution().largestSquareArea(bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]))
print(Solution().largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]))

