from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_value = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, v = stack.pop()
                start = idx
                max_value = max(max_value, v * (i - idx))
            stack.append((start, h))
        for i, h in stack:
            max_value = max(max_value, h * (len(heights) - i))
        return max_value


heights = [2,1,5,6,2,3]
s = Solution()
print(s.largestRectangleArea((heights)))
















# stack = []
#         max_area = 0
#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 idx, val = stack.pop()
#                 max_area = max(max_area, val * (i - idx))
#                 start = idx
#             stack.append((start, h))
#         for i, h in stack:
#             max_area = max(max_area, h * (len(heights) - i))
#         return max_area
