def moveZeroes(nums) -> None:
    p0 = 0
    p1 = 1
    while p1 != len(nums):
        if nums[p0] == 0 and nums[p1] != 0:
            nums[p0], nums[p1] = nums[p1], nums[p0]
            p0 += 1
        elif nums[p0] != 0:
            p0 += 1
        p1 += 1



nums = [1,0,1]
moveZeroes(nums)
print(nums)