class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        lower = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                lower = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, len(nums) - 1
        upper = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                upper = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        print(lower, upper)
        return [lower, upper]

