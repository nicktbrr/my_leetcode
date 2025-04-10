from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dists = [i for i in range(1, n)]
        shortest_dists = []
        d = n - 1
        for u, v in queries:
            while dists[u] < v:
                dists[u], u = v, dists[u]
                d -= 1
            shortest_dists.append(d)
        return shortest_dists


s = Solution()
n = 7
queries = [[0,3],[2,3]]

# queries = [[2,4],[0,2],[0,4]]
# n = 5

print(s.shortestDistanceAfterQueries(n, queries))