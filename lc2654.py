from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        min_gcd = float('inf')
        for i in range(len(nums)):
            temp_min_gcd = 0
            temp_gcd = nums[i]
            for j in range(i + 1, len(nums)):
                if temp_gcd == 1:
                    break
                temp_gcd = gcd(temp_gcd, nums[j])
                temp_min_gcd += 1

            if temp_gcd == 1:
                min_gcd = min(min_gcd, temp_min_gcd)
        if min_gcd != float('inf'):
            return min_gcd
        else:
            return -1


nums = [6,10,15]
nums = [2,10,6,14]
print(Solution().minOperations(nums))