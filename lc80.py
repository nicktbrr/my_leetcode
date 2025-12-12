class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d= {}
        i = 0
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > 2:
                continue
            nums[i] = num
            i += 1
        return i