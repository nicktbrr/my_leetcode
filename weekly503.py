from typing import List

# class Solution:
#     def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
#         d = {}
#         res = []
#         for i in range(len(nums)):
#             d[nums[i]] = d.get(nums[i], 0) + 1
#             if d[nums[i]] <= k:
#                 res.append(nums[i])
#         return res
#
# print(Solution().limitOccurrences([1,1,1,2,2,3], k = 2))


# class Solution:
#     def passwordStrength(self, password: str) -> int:
#         d = {}
#         res = 0
#         for c in password:
#             d[c] = d.get(c, 0) + 1
#             if d[c] <= 1:
#                 asci = ord(c)
#                 if 96 < asci < 123:
#                     res += 1
#                 elif 64 < asci < 91:
#                     res += 2
#                 elif 47 < asci < 58:
#                     res += 3
#                 elif c in '!@#$':
#                     res += 5
#         return res
#
# print(Solution().passwordStrength("aA1!"))

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 0
        dec = sum([1 for i in range(n) if nums[i] > nums[(i + 1) % n]])
        inc = sum([1 for i in range(n) if nums[i] < nums[(i + 1) % n]])
        p = nums.index(0)

        if dec == 1:
            return min(p, n - p + 2)
        elif inc == 1:
            return min(n - p, p + 2)
        else:
            return -1




nums = [4,3,2,1,0]
print(Solution().minOperations(nums))