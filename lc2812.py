import heapq
from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def in_bounds(r,c):
            return min(r,c) >= 0 and max(r,c) < N

        def precompute(grid):
            q = deque()
            min_dist = {}
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 1:
                        q.append((r,c,0))
                        min_dist[(r,c)] = 0

            while q:
                r, c, dist = q.popleft()
                neigh = [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]
                for r2, c2 in neigh:
                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2,c2)] = dist + 1
                        q.append((r2,c2,dist + 1))
            return min_dist

        min_dists = precompute(grid)
        max_heap = [(-min_dists[(0, 0)],0, 0)]
        visited = set()
        visited.add((0,0))
        while max_heap:
            dist, r, c = heapq.heappop(max_heap)
            dist = -dist
            if r == N - 1 and c == N - 1:
                return dist
            neigh = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for r2, c2 in neigh:
                if in_bounds(r2, c2) and (r2, c2) not in visited:
                    new_min = min(dist, min_dists[(r2, c2)])
                    heapq.heappush(max_heap, (-new_min, r2, c2))
                    visited.add((r2, c2))








        return 1

s = Solution()
print(s.maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))

