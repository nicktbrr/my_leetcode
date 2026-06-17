class Solution:
    def processStr(self, s: str, k: int) -> str:
        res = []
        lengths = [0] * len(s)
        curr_length = 0
        n = len(s)
        for i, c in enumerate(str(s)):
            if c == '*':
                if len(res) > 0:
                    res.pop()
                    curr_length -= 1
            elif c == '#':
                curr_length *= 2
            elif c == '%':
                res.reverse()
            else:
                res.append(c)
                curr_length += 1
            lengths[i] = curr_length
        if k >= lengths[-1]:
            return '.'
        for i in range(n - 1, -1, -1):
            c = s[i]
            L = lengths[i]
            if c == '*':
                continue  # prefix unchanged, k stays
            elif c == '#':
                half = L // 2
                if k >= half:
                    k -= half
            elif c == '%':
                k = L - 1 - k
            else:  # appended char lives at index L-1
                if k == L - 1:
                    return c
        return '.'

print(Solution().processStr(s = "abcd#abc##a", k = 3))