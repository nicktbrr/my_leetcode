# class Solution:
#     def checkGoodInteger(self, n: int) -> bool:
#         digit_sum = 0
#         squared_sum = 0
#
#         for d in  str(n):
#             c = int(d)
#             digit_sum += c
#             squared_sum += c * c
#         return squared_sum - digit_sum >= 50
#
#
# print(Solution().checkGoodInteger(1000))
from typing import List

class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            counts = {}
            for j in range(i, n):
                # extend window to nums[i..j]
                counts[nums[j]] = counts.get(nums[j], 0) + 1

                freqs = set(counts.values())
                if len(counts) == 1:
                    # single distinct value → always balanced
                    res = max(res, j - i + 1)
                elif len(freqs) == 2:
                    lo, hi = sorted(freqs)
                    if hi == 2 * lo:
                        # every count is f or 2f, and both occur
                        res = max(res, j - i + 1)
        return res


print(Solution().getLength([1,2,2,1,2,3,3,3]))
