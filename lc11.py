class Solution:
    def maxArea(self, height: [int]) -> int:
        l, r, max_height = 0, len(height) - 1, 0
        while l != r:
            max_height = (r - l) * min(height[l], height[r]) if (r - l) * min(height[l], height[r]) > max_height else max_height
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_height


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))