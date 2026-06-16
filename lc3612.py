class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c.islower():
                res.append(c)
            elif c == '*':
                if len(res) > 0:
                    res.pop()
                else:
                    continue
            elif c == '#':
                res += res
            else:
                res.reverse()
            print(res)
        return "".join(res)

print(Solution().processStr(s = "a#b%*"))
print(Solution().processStr(s = "z*#"))
print(Solution().processStr(s = "a#b%*"))
