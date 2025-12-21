class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if s == "":
            return True
        for c in t:
            if c == s[j]:
                j += 1
            if j == len(s):
                return True
        return False