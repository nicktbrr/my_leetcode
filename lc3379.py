class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None] * n
        for idx, num in enumerate(nums):
            res[idx] = nums[((num + idx) + 100 * n) % n]
        return res
