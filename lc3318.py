from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            sub = nums[i: i + k]
            counter = {}
            for num in sub:
                counter[num] = counter.get(num, 0) + 1
            temp = sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)[:x]
            temp2 = sum([k*v for k,v in temp])
            res.append(temp2)
        return res


print(Solution().findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
