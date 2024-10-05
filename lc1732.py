class Solution:
    def largestAltitude(self, gain: [int]) -> int:
        max_alt = 0
        current = 0
        for alt in gain:
            current = alt + current
            max_alt = max(current, max_alt)
        return max_alt


gain = [-4,-3,-2,-1,4,3,2]
s = Solution()
print(s.largestAltitude(gain))