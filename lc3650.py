from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # We need two sets of adjacency info:
        # 1. Normal: u -> v
        # 2. Reversible: v -> u (which we can turn into u -> v)
        adj_normal = [[] for _ in range(n)]
        adj_reversible = [[] for _ in range(n)]

        for u, v, w in edges:
            adj_normal[u].append((v, w))
            adj_reversible[v].append((u, w))  # If we are at v, we can reverse this to go to u

        distances = [float('inf')] * n
        distances[0] = 0
        pq = [(0, 0)]  # (cost, current_node)

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > distances[u]:
                continue

            # Option 1: Move along a normal directed edge
            for v, w in adj_normal[u]:
                if curr_dist + w < distances[v]:
                    distances[v] = curr_dist + w
                    heapq.heappush(pq, (distances[v], v))

            # Option 2: Use the switch at node 'u' to reverse an incoming edge
            # This "reverses" v -> u into u -> v for a cost of 2 * w
            for v, w in adj_reversible[u]:
                if curr_dist + (2 * w) < distances[v]:
                    distances[v] = curr_dist + (2 * w)
                    heapq.heappush(pq, (distances[v], v))

        return int(distances[-1]) if distances[-1] != float('inf') else -1


# Testing Example 1
print(Solution().minCost(n=4, edges=[[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]))  # Expected: 5