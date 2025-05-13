class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        # initial counts
        counts = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            counts[idx] += 1
        for _ in range(t):
            curr = [0] * 26
            if counts[25]:
                curr[0] = (curr[25] + counts[25]) % mod
                curr[1] = (curr[25] + counts[25]) % mod
            for i in range(25):
                if counts[i]:
                    curr[i + 1] = (counts[i] + curr[i + 1]) % mod
            counts = curr
        return sum(counts) % mod


s = Solution()
s1 = "abcyy"
t = 2
print(s.lengthAfterTransformations(s1, t))