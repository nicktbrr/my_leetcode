from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        for n in nums[1:]:
            pre.append(pre[-1] * n)
        post = [nums[-1]]
        for n in reversed(nums[:-1]):
            post.insert(0, n * post[0])
        pre.insert(0, 1)
        post.append(1)
        res = []
        for i in range(1, len(nums) + 1):
            res.append(pre[i - 1] * post[i])
        return res

nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))