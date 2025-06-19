from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # IDEA
        # calculate len(nums) choose 3
        # Sort nums array
        # Look at highest and lowest numbers then subtrack from total combinations
        # once we can make a valid triangle stop
        s = sorted(nums)
        res = 0
        N = len(nums)
        for k in range(2, N):
            i, j = 0, k - 1
            while i < j:
                if s[i] + s[j] > s[k]:
                    res += (j - i)
                    j -= 1
                else:
                    i += 1
        return res



# nums = [2,2,3,4]
# nums = [4,2,3,4]
nums = [1,1,3,4]
print(Solution().triangleNumber(nums))