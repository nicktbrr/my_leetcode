class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if abs(startPos - endPos) % 2 == 0 and k % 2 == 1:
            return 0
        elif abs(startPos - endPos) % 2 == 1 and k % 2 == 0:
            return 0
        elif (abs(startPos - endPos)) > k:
            return 0
        mem = [[0] * (2 * k + 1) for _ in range(k)]
        start = k
        end  = (endPos - startPos) + k if startPos < endPos else (startPos - endPos) + k
        mem[0][start + 1] = 1
        mem[0][start - 1] = 1
        for row in range(1, k):
            for col in range(len(mem[0])):
                top_left =  mem[row - 1][col - 1 if col != 0 else 0]
                top_right = mem[row - 1][col + 1 if col != len(mem[0]) - 1 else 0]
                mem[row][col] = int((top_left + top_right) % (10**9 + 7))

        return mem[-1][end]


print(Solution().numberOfWays(startPos = 989, endPos = 1000, k = 99))