# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         s = str(n)
#         neg = False
#         res = 0
#         for c in s:
#             if neg:
#                 res += -int(c)
#             else:
#                 res += int(c)
#             neg = not neg
#         return res
#
# class Solution:
#     def makeStringsEqual(self, s: str, target: str) -> bool:
#         c1 = Counter(s)
#         c2 = Counter(target)
#
#         if "1" in s and "1" in target:
#             return True
#         if s == target:
#             return True
#         return False
#
#

from collections import defaultdict, Counter
from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        dp = [float('inf')] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = k
        for i in range(2, len(dp)):
            right_c = Counter()
            right = 0
            for j in range(i - 1, -1, -1):
                right_c[nums[j]] += 1
                if right_c[nums[j]] == 1:
                    right += 0
                elif right_c[nums[j]] == 2:
                    right += 2
                else:
                    right += 1
                cost = dp[j] + k + right
                if cost < dp[i]:
                    dp[i] = cost
        return dp[-1]


print(Solution().minCost(nums=[1, 2, 1, 2, 1, 3, 3], k=2))

