class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = 0
        r = 2
        res = 0
        if r > len(nums):
            return res
        else:
            while r < len(nums):
                if nums[l] + nums[r] == (nums[l+1] / 2):
                    res += 1
                r += 1
                l += 1
            return res