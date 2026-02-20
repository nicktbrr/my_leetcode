class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[None for i in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dp[0][0] = True
        for i, c in enumerate(s1):
            dp[0][i+1] = s1[i] == s3[i] and dp[0][i]
        for i, c in enumerate(s2):
            dp[i + 1][0] = s2[i] == s3[i] and dp[i][0]
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                if s2[r - 1] == s3[r+c-1] and dp[r-1][c] or s1[c - 1] == s3[r+c-1] and dp[r][c-1]:
                    dp[r][c] = dp[r-1][c] or dp[r][c-1]
                else:
                    dp[r][c] = False
        return dp[-1][-1]



print(Solution().isInterleave(s1 = "aabccx", s2 = "dbbca", s3 = "aadbbcbcacx"))