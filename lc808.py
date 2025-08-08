class Solution:
    def soupServings(self, n: int) -> float:
        def recurse(a, b, memo={}):
            if (a, b) in memo:
                return memo[(a, b)]
            elif a <= 0 and b <= 0:
                return .5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            first = recurse(a-100, b, memo)
            second = recurse(a-75, b-25, memo)
            third = recurse(a-50, b-50, memo)
            fourth = recurse(a-25, b-75, memo)

            memo[(a,b)] = .25 * (first + second + third + fourth)
            return memo[(a, b)]
        if n >= 4800:
            return 1
        res = recurse(n, n, {})
        return res

print(Solution().soupServings(50))
print(Solution().soupServings(100))