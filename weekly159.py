from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_0, y_0 = coordinates[0]
        x_1, y_1 = coordinates[1]

        dx = x_0 - x_1
        dy = y_0 - y_1

        for i in range(2, len(coordinates)):
            if dx * (y_1 - coordinates[i][1]) != dy * (x_1 - coordinates[i][0]):
                return False
        return True

print(Solution().checkStraightLine([[1, 0], [0, -1], [2, 1], [-1, -2]]))


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for f in folder:
            if not res or not f.startswith(res[-1] + '/'):
                res.append(f)
        return res