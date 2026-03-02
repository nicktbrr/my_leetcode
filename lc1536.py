from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        trailing_zeros = []
        m, n = len(grid), len(grid[0])
        for idx, row in enumerate(grid):
            temp = []
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    temp.append(0)
                else:
                    break
            trailing_zeros.append(len(temp))
        res = 0
        for i in range(m):
            target = m - i - 1
            found_idx = -1
            for j in range(i,m):
                if trailing_zeros[j] >= target:
                    found_idx = j
                    break
            if found_idx == -1:
                return -1
            val = trailing_zeros.pop(found_idx)
            trailing_zeros.insert(i, val)
            res += found_idx-i
        return res