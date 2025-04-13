class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if len(str(i)) % 2 == 1:
                continue
            else:
                num_len = len(str(i))
                l = str(i)[(num_len // 2):]
                r = str(i)[:(num_len // 2)]
                sum_r = sum([int(c) for c in r])
                sum_l = sum([int(c) for c in l])
                if sum_r == sum_l:
                    count += 1
        return count



s = Solution()
print(s.countSymmetricIntegers(1200, 1230))