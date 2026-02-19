class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        temp = []
        curr_len = 1
        prev = s[0]
        for i in range(1, len(s)):
            curr = s[i]
            if prev == curr:
                curr_len += 1
            else:
                temp.append(curr_len)
                curr_len = 1
            prev = curr
        temp.append(curr_len)
        if len(temp) == 0:
            return temp[0]
        res = 0
        for i in range(1, len(temp)):
            res += min(temp[i - 1], temp[i])
        return res


