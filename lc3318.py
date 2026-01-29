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
    # def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    #     answer = []
    #     for index in range(len(nums) - k + 1):
    #         subarray = nums[index:index + k]
    #         counts = {num: subarray.count(num) for num in set(subarray)}
    #         sorted_counts = sorted(counts.items(), key=lambda item: (item[1], item[0]))
    #         m_sum = 0
    #         for sub_index in range(x):
    #             cur_item = sorted_counts[-(sub_index + 1)]
    #             m_sum += cur_item[0] * cur_item[1]
    #         answer.append(m_sum)
    #     return answer




print(Solution().findXSum(nums = [9,2,2], k = 3, x = 3))
