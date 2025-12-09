class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        my_max = -1
        if len(num) < 3:
            return res
        for i in range(3, len(num) + 1):
            sub = num[i - 3:i]
            if sub[0] == sub[1] == sub[2] and int(sub[0] * 3) > my_max:
                res = sub[0] * 3
                my_max = int(sub[0] * 3)
        return res


print(Solution().largestGoodInteger("0111"))
