from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        dirs = [[-1,-1],
                [-1,0],
                [-1,1],
                [0,-1],
                [0,1],
                [1,-1],
                [1,0],
                [1,1]]
        def get_neigh(r, c):
            neigh = 0
            for r_t, c_t in dirs:
                if 0 <= r_t + r < m and 0 <= c_t + c < n:
                    neigh += board[r+r_t][c+c_t]
            return neigh
        temp = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                neigh = get_neigh(r,c)
                if neigh < 2:
                    temp[r][c] = 0
                elif 2 <= neigh <= 3 and board[r][c] == 1:
                    temp[r][c] = 1
                elif neigh == 3:
                    temp[r][c] = 1
                elif neigh < 3:
                    temp[r][c] = 0
        for r in range(m):
            for c in range(n):
                board[r][c] = temp[r][c]
        return None


print(Solution().gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))