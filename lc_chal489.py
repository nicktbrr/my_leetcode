# class Solution:
#     def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
#         lights = {}
#         for b in bulbs:
#             if b not in lights:
#                 lights[b] = True
#             else:
#                 del lights[b]
#         return sorted(list(lights.keys()))

from collections import deque


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_dq = deque()
        min_dq = deque()
        prefix_xor = [0] * (n+1)
        l = 0
        max_val = 0
        for i in range(n):
            prefix_xor[i+1] = prefix_xor[i] ^ nums[i]
        for r in range(n):
            while max_dq and nums[max_dq[-1]] <= nums[r]:
                max_dq.pop()
            max_dq.append(r)

            while min_dq and nums[min_dq[-1]] >= nums[r]:
                min_dq.pop()
            min_dq.append(r)

            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                if max_dq[0] == l:
                    max_dq.popleft()
                if min_dq[0] == l:
                    min_dq.popleft()
                l += 1
            for i in range(l, r + 1):
                current_subarray_xor = prefix_xor[r + 1] ^ prefix_xor[i]
                if current_subarray_xor > max_val:
                    max_val = current_subarray_xor

        return max_val


print(Solution().maxXor(nums = [5,2,5,6,3], k = 2))