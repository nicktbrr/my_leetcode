class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = [0] * (len(s))
        for i in range(len(s) - 2, -1, -1):
            if s[i + 1] == 'a':
                a_count[i] = a_count[i + 1] + 1
            else:
                a_count[i] = a_count[i + 1]
        b_count = 0
        res = len(s)
        for i in range(len(s)):
            res = min(res, b_count + a_count[i])
            if s[i] == 'b':
                b_count += 1
        return res

print(Solution().minimumDeletions(s = "aababbab"))