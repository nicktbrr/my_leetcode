class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) <= 2:
            return s
        res = s[0] + s[1]
        for c in s[2:]:
            if c == res[-1] and c == res[-2]:
                continue
            else:
                res += c
        return res

# print(Solution().makeFancyString("aaabaaaa"))
print(Solution().makeFancyString("leeetcode"))