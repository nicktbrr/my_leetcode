class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c =='{':
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ")":
                if stack.pop() != "(":
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

print(Solution().isValid("(]"))