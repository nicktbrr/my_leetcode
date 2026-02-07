from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for col in range(len(strs[0])):
            prev = strs[0][col]
            for s in strs[1:]:
                if s[col] < prev:
                    res += 1
                    break
                prev = s[col]
        return res

print(Solution().minDeletionSize(strs = ["abc", "bce", "cae"]))