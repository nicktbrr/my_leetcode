class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = float('inf')
        my_min = -1
        for idx, c in enumerate(capacity):
            if c >= itemSize and c < res:
                res = c
                my_min = idx
        return my_min

from typing import List

class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return -1
        LIMIT = (10**9 * 10**5) + 1
        prods = [0] * (len(nums))
        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            c = nums[i]
            if curr_prod * c < LIMIT:
                curr_prod *= c
                prods[i] = curr_prod
            else:
                prods[i] = LIMIT
        curr_sum = 0
        for i in range(1, len(nums) + 1):
            curr_sum += nums[i-1]
            prod = -1
            if i + 1 >= len(nums):
                prod = 1
            else:
                prod = prods[i + 1]
            if curr_sum == prod:
                return i
        return -1

class Solution:
    def minOperations(self, s: str) -> int:
        ans = sorted(s)
        c = Counter(s)
        n = len(s)
        if "".join(ans) == s:
            return 0
        elif n == 2 and s != "".join(ans):
            return -1
        elif s[0] == ans[0] or s[-1] == ans[-1]:
            return 1
        elif s[0] == ans[-1] and s[-1] == ans[0]:
            if c[s[0]] > 1 or c[s[-1]] > 1:
                return 2
            else:
                return 3
        else:
            return 2