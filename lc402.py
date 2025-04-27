class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_removed = 0
        temp = num
        result = ''
        while num_removed < k:
            min_num = 10
            min_idx = -1
            for idx, c in enumerate(temp):
                if idx >= len(temp) - (k - num_removed):
                    break
                if int(c) < min_num:
                    min_num = int(c)
                    min_idx = idx
            result += temp[min_idx]
            temp = temp[min_idx + 1:]
            num_removed += 1


s = Solution()
print(s.removeKdigits('1432219', 3))