from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num == 2:
                res.append(-1)
                continue
            best_ans = num  # Temporary placeholder
            for x in range(num - 1, -1, -1):
                if (x | (x + 1)) == num:
                    best_ans = x
                else:
                    break
            res.append(best_ans)
        return res

print(Solution().minBitwiseArray(nums = [2,3,5,7]))