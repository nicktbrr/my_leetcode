class Solution:
    def countGoodNumbers(self, n: int) -> int:

        if n % 2 == 0:
            counts = 5 ** (n // 2)
            counts *= 4 ** (n // 2)
            return counts % (10 ** 9 + 7)
        else:
            counts = 5 ** ((n + 1) // 2)
            counts *= 4 ** ((n - 1 )// 2)
            return counts % (10 ** 9 + 7)
        # for i in range(n):
        #     if i % 2 == 0:
        #         counts *= 5
        #     else:
        #         counts *= 4
        # return counts % (10 ** 9 + 7)


s = Solution()
print(s.countGoodNumbers(50))
