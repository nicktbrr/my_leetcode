def calc(x, s, l):
    prefix_l = len(x) - len(s)
    count = 0
    if len(x) < len(s):
        return 0
    if len(x) == len(s):
        return 0 if x < s else 1
    for i in range(prefix_l):
        d = int(x[i])
        if int(x[i]) > l:
            count += (l + 1) ** (prefix_l - i)
            return count
        count += int(x[i]) * (l + 1) ** (prefix_l - i - 1)
        print()

    if x[-len(s):] >= s:
        count += 1
    return count

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        t = calc(str(finish), s, limit)
        s = calc(str(start - 1), s, limit)
        return t - s



s = Solution()

print(s.numberOfPowerfulInt(15, 215, 6, "10"))