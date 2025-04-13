class Solution:
    def minTimeToType(self, word: str) -> int:
        start = 0
        result = 0
        letters = 'abcdefghijklmnopqrstuvwxyz'
        lookup_char = {c: i for i, c, in enumerate(letters)}
        for c in word:
            clockwise = (lookup_char[c] - start + 26) % 26
            counter_clockwise = (start - lookup_char[c] + 26) % 26
            if clockwise < counter_clockwise:
                result += clockwise
            else:
                result += counter_clockwise
            start = lookup_char[c]
            result += 1
        return result

s = Solution()

print(s.minTimeToType("bza"))