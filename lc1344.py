class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_to_m = ((hour + (minutes / 60) ) % 12) * 5
        op1 = ((h_to_m - minutes) * 6) % 360
        op2 = ((minutes - h_to_m) * 6) % 360
        return min(op1, op2)


# print(Solution().angleClock(hour = 3, minutes = 15))
# print(Solution().angleClock(hour = 3, minutes = 30))
# print(Solution().angleClock(hour = 12, minutes = 30))
print(Solution().angleClock(hour = 1, minutes = 57))