class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows, max_x = 0, None
        for i in range(0, len(points)):
            if max_x is None or points[i][0] > max_x or points[i][1] < max_x:
                arrows += 1
                max_x = points[i][1]
        return arrows



s = Solution()
print(s.findMinArrowShots([[-2147483648,2147483647]]))
