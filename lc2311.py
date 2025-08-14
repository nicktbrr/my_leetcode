class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        max_num = 0
        my_pow = len(s) - 1
        zeros = 0
        ones = 0
        for idx, bit in enumerate(s):
            if bit == "1":
                max_num += 2**(my_pow - idx)
                ones += 1
            else:
                zeros += 1

        for idx, bit in enumerate(s):
            if max_num <= k:
                return ones + zeros
            elif bit == "1":
                max_num -= 2**(my_pow - idx)
                ones -= 1
        return ones + zeros

print(Solution().longestSubsequence(s = "1001010", k = 5))
print(Solution().longestSubsequence(s = "00101001", k = 1))
print(Solution().longestSubsequence(s = "1001010", k = 5))
