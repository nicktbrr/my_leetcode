from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p2 = 0
        # for i in range(m, len(nums1)):
        #     nums1[i] = nums2[p2]
        #     p2 += 1
        # nums1.sort()

        p1, p2, idx = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1
            idx -= 1

print(Solution().merge([1,2,3,0,0,0], 3, [-1,0,5], 3))