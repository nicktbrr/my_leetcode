from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0] * (len(nums) + 1)
        curr_sum = 0
        q_pos = 0
        for i, n in enumerate(nums):
            while curr_sum + diff[i] < nums[i]:
                if q_pos == len(queries):
                    return -1
                l, r, v = queries[q_pos][0], queries[q_pos][1], queries[q_pos][2]
                if r < i:
                    continue
                diff[max(l, i)] += v
                diff[r + 1] -= v
                q_pos += 1
            curr_sum += diff[i]
        return q_pos



        # curr_sum = sum(nums)
        # k = 0
        # for l, r, v in queries:
        #     for i in range(l, r + 1):
        #         if curr_sum == 0:
        #             return k + 1
        #         elif nums[i] == 0:
        #             continue
        #         elif nums[i] - v < 0:
        #             curr_sum -= nums[i]
        #             nums[i] = 0
        #         else:
        #             nums[i] -= v
        #             curr_sum -= v
        #     k += 1
        # if curr_sum != 0:
        #     return -1
        # else:
        #     return k




nums = [6,7]
queries = [[1,1,2],[1,1,5],[1,1,1],[0,1,4],[0,1,3],[0,1,2],[1,1,1],[1,1,2],[0,1,1],[0,1,3],[1,1,5],[1,1,5],[0,1,3],[1,1,5],[1,1,5]]

s = Solution()
print(s.minZeroArray(nums, queries))