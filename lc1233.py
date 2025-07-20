from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        d = {}
        prev = folder[0]
        d[prev] = 1
        for path in folder[1:]:
            if prev == path[:len(prev)]:
                if len(path) > len(prev) and path[len(prev)] == "/":
                    continue
                else:
                    d[path] = 1
            else:
                d[path] = 1
            prev = path
        return list(d.keys())


print(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))