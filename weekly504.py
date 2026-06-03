from typing import List
# class Solution:
#     def digitFrequencyScore(self, n: int) -> int:
#         d = {}
#         for c in str(n):
#             d[c] = d.get(c, 0) + 1
#         ls = d.items()
#         res = 0
#         for d, f in ls:
#             res += int(d) * f
#         return res
#
# print(Solution().digitFrequencyScore(122))
#
#
# class Solution:
#     def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
#         free = []
#         for i in range(len(items)):
#             factor_1, item_1 = items[i]
#             temp = 0
#             for j in range(len(items)):
#                 factor_2, item_2 = items[j]
#                 if factor_2 % factor_1 == 0 and i != j:
#                     temp += 1
#             free.append(temp)
#         dp = [[0] * (len(items) + 1) for _ in range(budget + 1)]
#         for b in range(1, len(dp)):
#             for i in range(1, len(dp[0])):
#                 price = items[i-1][1]
#                 value = 1 + free[i-1]
#                 dp[b][i] = dp[b][i-1]
#                 if price <= b:
#                     dp[b][i] = max(dp[b][i], dp[b-price][i-1] + value)
#
#         minPrice = min(p for _, p in items)  # = 2 here (item 0)
#         n = len(items)  # = 3, the last column index
#         ans = []
#         for b in range(budget + 1):
#             ans.append(dp[b][n] + (budget - b) // minPrice)
#         # answer = max(dp[b][n] + (budget - b) // minPrice for b in range(budget + 1))
#         return max(ans)
#
#
#
#
# items = [[6,2],[2,6],[3,4]]
# budget = 9
# print(Solution().maximumSaleItems(items, budget))


