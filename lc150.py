from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item.isnumeric() or (item[0] == "-" and len(item) > 1):
                stack.append(int(item))
                continue
            else:
                item_2 = stack.pop()
                item_1 = stack.pop()
                res = None
                if item == "+":
                    res = item_1 + item_2
                elif item == "-":
                    res = item_1 - item_2
                elif item == "*":
                    res = item_1 * item_2
                else:
                    res = int(item_1 / item_2)
                stack.append(res)
        return stack[0]
