from typing import List
import heapq

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         res = 0
#         for r in range(len(grid) - 1, -1, -1):
#             for c in range(len(grid[0]) - 1, -1, -1):
#                 if grid[r][c] < 0:
#                     res += 1
#         return res
#
# class ProductOfNumbers:
#
#     def __init__(self):
#         self.stream = []
#
#     def add(self, num: int) -> None:
#         self.stream.append(num)
#
#     def getProduct(self, k: int) -> int:
#         prod = 1
#         for n in self.stream[len(self.stream) - k:]:
#             prod *= n
#         return prod



class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        avail_events = []
        res = 0
        day = 1
        n = len(events)
        i = 0

        while i < n or avail_events:
            while i < n and events[i][0] == day:
                heapq.heappush(avail_events, events[i][1])
                i += 1

            while avail_events and avail_events[0] < day:
                heapq.heappop(avail_events)

            if avail_events:
                heapq.heappop(avail_events)
                day += 1
                res += 1
            elif i < n:
                day = events[i][0]
        return res

print(Solution().maxEvents([[1,2],[2,3],[3,4],[1,2]]))
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)