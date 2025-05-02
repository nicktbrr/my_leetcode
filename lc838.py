from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = list(dominoes)
        q = deque()
        start = 0
        finish = len(dominoes)
        for idx, dom in  enumerate(result):
            if dom in {'L', 'R'}:
                q.append((idx, dom))
        while q:
            idx, current = q.popleft()
            if current == "L":
                if idx - 1 >= start and result[idx - 1] == '.':
                    result[idx - 1] = 'L'
                    q.append((idx - 1, "L"))
            else:
                if idx + 2 < finish and result[idx + 2] == '.' and result[idx + 1] == ".":
                    result[idx + 1] = 'R'
                    q.append((idx + 1, 'R'))
                elif idx + 1 == finish - 1 and result[idx + 1] == ".":
                    result[idx + 1] = 'R'
                elif idx + 2 < finish and result[idx + 2] == 'L':
                    q.popleft()
                elif idx + 1 < finish and result[idx + 1] == '.':
                    result[idx + 1] = 'R'
        return "".join(result)




s = Solution()
# print(s.pushDominoes(".L.R...LR..L.."))
# print(s.pushDominoes("RR.L"))
print(s.pushDominoes("R.R.L"))