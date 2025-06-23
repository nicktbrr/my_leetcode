class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d = {}
        for c in word:
            d[c] = d.get(c, 0) + 1
        s = [v for _, v in sorted(d.items(), key=lambda x: x[1])]
        min_sub = float('inf')
        for i in range(len(s)):
            subs = 0
            for j in range(len(s)):
                if j < i:
                    subs += s[j]
                elif s[j] - k > s[i] and j > i:
                    subs += s[j] - (s[i] + k)
            min_sub = min(min_sub, subs)
        return min_sub





print(Solution().minimumDeletions('dabdcbdcdcd', 2))