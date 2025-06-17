class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        right = 0
        abc_set = {'a', 'b', 'c'}
        d = {}
        res = 0
        while right < len(s):
            r = s[right]
            if r in abc_set:
                d[r] = d.get(r, 0) + 1
            while len(d) >= 3:
                res += len(s) - right
                if s[left] in d:
                    if d[s[left]] == 1:
                        d.pop(s[left])
                    else:
                        d[s[left]] -= 1
                left += 1
            right += 1
        return res


print(Solution().numberOfSubstrings("aaacb"))