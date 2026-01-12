from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            temp = s[i:i + len(s)]
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        return dp[0]


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

s = "leetcode"
wordDict = ["leet","code"]
print(Solution().wordBreak(s, wordDict))