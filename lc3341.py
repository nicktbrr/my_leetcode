import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        max_h = [(0, 0, 0)]
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = {(0,0): 0}
        N, M = len(moveTime), len(moveTime[0])

        def out_of_bounds(c_row, c_col, n_row, n_col):
            if c_row + n_row >= N or  c_row + n_row < 0:
                return True
            if c_col + n_col >= M or  c_col + n_col < 0:
                return True
            return False

        while max_h:
            val, row, col = heapq.heappop(max_h)
            for r, c in moves:
                if out_of_bounds(row, col, r, c):
                    continue
                c_row = row + r
                c_col = col + c
                if (c_row,c_col) in visited:
                    new = max(visited[c_row,c_col], val + 1)
                    visited[c_row, c_col] = min(new, visited[c_row,c_col])
                else:
                    visited[c_row,c_col] = max(val + 1, moveTime[c_row][c_col] + 1)
                    heapq.heappush(max_h, (max(val + 1, moveTime[c_row][c_col] + 1), c_row, c_col))
            heapq.heapify(max_h)
        return visited[(N-1,M-1)]






s = Solution()
t1 = [[0,1,2],[3,1,6],[4,5,4]]
t2 = [[0,4],[4,4]]
t3 = [[27,7],[60,69]]
print(s.minTimeToReach(t1))