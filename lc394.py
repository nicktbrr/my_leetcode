class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        t = ""
        result = ""
        for i in range(len(s)):
            if s[i] == "[":
                if len(t) != 0:
                    stack.append(t)
                t = ""
            elif s[i] == "]":
                if len(t) != 0:
                    stack.append(t)
                s1 = stack.pop()
                s2 = stack.pop()
                if s2.isnumeric():
                    stack.append(int(s2) * s1)
                else:
                    stack.append(s2 + s1)
                t = ""
            else:
                if s[i].isnumeric() and t.isnumeric() or s[i].isalpha() and t.isalpha() or len(t) == 0:
                    t += s[i]
                else:
                    stack.append(t)
                    t = s[i]
        if len(t) != 0:
            return stack.pop() + t
        if len(stack):
            return stack.pop()


s = Solution()
print(s.decodeString("3[cd]ef"))
print(s.decodeString("3[a2[b2[c]]]fc"))