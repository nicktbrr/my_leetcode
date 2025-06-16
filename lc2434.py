class Solution:
    def findSmallest(self, s):
        return min(s)
    def robotWithString(self, s: str) -> str:
        smallest = self.findSmallest(s)
        stack = []
        res = ""
        for idx, c in enumerate(s):
            if c <= smallest:
                stack.append(c)
                while stack:
                    res += stack.pop(-1)
                if idx != len(s) - 1:
                    smallest = self.findSmallest(s[idx + 1:])
            else:
                stack.append(c)
        while stack:
            res += stack.pop(-1)
        return res

s = "bydizfve"
print(Solution().robotWithString(s))