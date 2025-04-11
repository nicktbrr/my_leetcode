class Node():
    def __init__(self, x, right=None, left=None):
        self.x = x
        self.right = right
        self.left = left


def make_tree(s):
    if not s:
        return 1
    if s[0] == "0":
        return 0
    one = make_tree(s[1:])
    two = 0
    if len(s) > 1 and 10 <= int(s[:2]) <= 26:
        two = make_tree(s[2:])

    return one + two


class Solution:
    def numDecodings(self, s: str) -> int:
        # if not s:
        #     return 0
        # return make_tree(s)
        memo = {}

        def decode(index):
            # Base cases
            if index in memo:
                return memo[index]
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0

            # Try one digit
            result = decode(index + 1)

            # Try two digits if possible
            if index + 1 < len(s) and int(s[index:index + 2]) <= 26:
                result += decode(index + 2)

            memo[index] = result
            return result

        return decode(0)



t = Solution()
print(t.numDecodings("226"))