class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        while s != '1':
            s_i = int(s, 2)
            if s[-1] == '0':
                s_i = s_i // 2
            else:
                s_i += 1
            s = bin(s_i)[2:]
            res += 1
        return res
