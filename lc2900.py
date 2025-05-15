from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev = groups[0]
        for idx, (w, g) in enumerate(zip(words, groups)):
            if idx == 0 or prev == g:
                continue
            else:
                res.append(w)
                prev = g
        return res


