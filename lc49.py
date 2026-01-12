from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        my_d = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in my_d:
                my_d[key] = len(res)
                res.append([word])
            else:
                pos = my_d[key]
                res[pos].append(word)
        return res

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))