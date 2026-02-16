from typing import List, Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = Counter(s)
        res = set()

        for c in s:
            right[c] -= 1
            for p in left:
                if right[p] > 0:
                    res.add(p + c)
            left.add(c)
        return len(res)


print(Solution().countPalindromicSubsequence(s = "aabca"))
