from typing import List
from collections import Counter

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        zero1 = 0
        for n in nums1:
            if n == 0:
                sum1 += 1
                zero1 += 1
            else:
                sum1 += n
        sum2 = 0
        zero2 = 0
        for n in nums2:
            if n == 0:
                sum2 += 1
                zero2 += 1
            else:
                sum2 += n
        if sum1 > sum2 and zero2 == 0:
            return -1
        elif sum2 > sum1 and zero1 == 0:
            return -1
        return max(sum1, sum2)




nums1 = [18,0,0,21,7,17,2,28,14,0,27,5,24,10]
nums2 = [12,16,0,24,9,0,0,18,16,0,27,1,29,21,1]
s = Solution()
print(s.minSum(nums1, nums2))
