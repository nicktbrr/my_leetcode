class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def scan(row, col):
            tot = 0
            for r in range(len(mat)):
                tot += mat[r][col]
            for c in range(len(mat[0])):
                tot += mat[row][c]
            return tot - 2
        res = []
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    if scan(r, c) == 0:
                        res.append((r,c))
        return len(res)