from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in d:
                d[key] = len(res)
                res.append([word])
            else:
                pos = d[key]
                res[pos].append(word)
        return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))