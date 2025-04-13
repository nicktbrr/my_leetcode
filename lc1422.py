class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == "0" else 0
        right = sum(1 for c in s[1:] if c == "1")
        result = left + right

        for i, c in enumerate(s[1:]):
            if i + 1 == len(s) - 1:
                break
            if c == "0":
                left += 1
            else:
                right -= 1
            new = left + right
            if new > result:
                result = new
        return result


s = Solution()
print(s.maxScore("1111"))
