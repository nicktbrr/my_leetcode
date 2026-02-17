class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        seen = {}
        res = 0
        while r < len(s):

            seen[s[r]] = seen.get(s[r], 0) + 1
            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return res

l = [1]
l.insert(1,2)
print(l)