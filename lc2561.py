from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = {}
        for b1, b2 in zip(basket1, basket2):
            freq[b1] = freq.get(b1, 0) + 1
            freq[b2] = freq.get(b2, 0) - 1
        a = []
        for k, v in freq.items():
            if v % 2 == 1:
                return -1
            elif v != 0:
                a += [k] * abs(v // 2)
        temp = sorted(a)
        abs_min = min(min(basket1), min(basket2))
        res = 0
        for n in temp[:len(a) // 2]:
            if n < 2 * abs_min:
               res += n
            else:
                res += 2 * abs_min
        return res



# print(Solution().minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2]))
# print(Solution().minCost(basket1 = [2,3,4,1], basket2 = [3,2,5,1]))
print(Solution().minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]))