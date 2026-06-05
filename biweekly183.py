# class Solution(object):
#     def minimumSwaps(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l, r = 0, len(nums) - 1
#         res = 0
#         while l < r:
#             while nums[r] == 0 and l < r:
#                 r -= 1
#             if nums[l] == 0 and nums[r] != 0:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 res += 1
#             l += 1
#         return res
#
# print(Solution().minimumSwaps([0,1,0,3,12]))

# class Solution(object):
#     def minOperations(self, nums, k):
#         even_dist = [0] * k
#         odd_dist = [0] * k
#
#         def min_dist(m, j):
#             d = abs(m - j)
#             return min(d, k - d)
#
#         for i, n in enumerate(nums):
#             temp = even_dist if i % 2 == 0 else odd_dist
#             m = n % k
#             for j in range(k):
#                 temp[j] += min_dist(m, j)
#         best = float('inf')
#         for x in range(k):
#             for y in range(k):
#                 if x != y:
#                     best = min(best, even_dist[x] + odd_dist[y])
#
#         return best
# print(Solution().minOperations([1,4,2,8], k = 3))
# print(Solution().minOperations([1,1,1], k = 3))

class Solution(object):
    def maxScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        max_row = float('-inf')
        max_col = float('-inf')

        for row in grid:
            temp_max = row[0]
            max_row = max(max_row, temp_max)
            for i in range(1, len(row)):
                temp_max = max(row[i], temp_max + row[i])
                max_row = max(max_row, temp_max)

        trans_grid = list(zip(*grid))
        for col in trans_grid:
            temp_max = col[0]
            max_col = max(max_col, temp_max)
            for i in range(1, len(col)):
                temp_max = max(col[i], temp_max + col[i])
                max_col = max(temp_max, max_col)

        return max(max_col, max_row)

print(Solution().maxScore(grid = [[4,-2,-3],[-1,-3,-1],[-4,2,-1]]))