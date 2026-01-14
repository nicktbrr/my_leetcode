from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        current = points[0]
        res = 0
        for point in points[1:]:
            temp_x = point[0] - current[0]
            temp_y = point[1] - current[1]
            res += max(abs(temp_x), abs(temp_y))
            current = point
        return res


points = [[1,1],[3,4],[-1,0]]
print(Solution().minTimeToVisitAllPoints(points))