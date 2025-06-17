from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        my_set = {("", 0, 0)}
        res = []
        for i in range(n * 2):
            temp = "("
            temp_set = set()
            for p, o, c in my_set:
                if o + 1 <= n:
                    temp_set.add((p + temp, o + 1, c))
                    if o + 1 == c and o == n:
                        res.append(p + temp)
            temp = ")"
            for p, o, c in my_set:
                if c + 1 <= o:
                    temp_set.add((p + temp, o, c + 1))
                    if c + 1 == o and o == n:
                        res.append(p + temp)
            my_set = my_set.union(temp_set)
        return res


a = Solution().generateParenthesis(3)
print(a)

