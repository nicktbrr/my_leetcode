from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d = {}
        res = []
        for digit in digits:
            if digit in d:
                d[digit] += 1
            else:
                d[digit] = 1
        for i in range(100, 1000, 2):
            temp_d = {}
            num = str(i)
            for c in num:
                if int(c) not in temp_d:
                    temp_d[int(c)] = 1
                else:
                    temp_d[int(c)] += 1
            flag = True
            for k, v in temp_d.items():
                if k not in d or d[k] < temp_d[k]:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res


s = Solution()
print(s.findEvenNumbers([2,1,3,0]))



