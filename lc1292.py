from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        cum_sum = [[0] * (n + 1) for i in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                cum_sum[r][c] = (cum_sum[r - 1][c] +
                                 cum_sum[r][c - 1] +
                                 mat[r - 1][c - 1] -
                                 cum_sum[r - 1][c - 1])
        def get_sqr_sum(x1, y1 ,x2 ,y2):
            return cum_sum[x2][y2] - cum_sum[x1-1][y2] - cum_sum[x2][y1-1] + cum_sum[x1-1][y1-1]

        l, r, res = 1, min(n, m), 0
        temp = False
        while l <= r:
            mid = (l + r) // 2
            for row in range(1, m - mid + 2):
                for col in range(1, n - mid + 2):
                    sqr_sum = get_sqr_sum(row,col, row + mid - 1, col + mid - 1)
                    if sqr_sum <= threshold:
                        res = max(res, mid)
                        temp = True
            if temp:
                l = mid + 1
            else:
                r = mid - 1
            temp = False

        return res






print(Solution().maxSideLength(mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))

