class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i, c in enumerate(s):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r + 1) - l > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if s[l] == s[r] and (r + 1) - l > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res


print(Solution().longestPalindrome("aacabdkacaa"))