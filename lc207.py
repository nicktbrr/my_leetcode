from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_ls = {}
        course_in = [0] * numCourses
        for n2, n1 in prerequisites:
            if n1 not in adj_ls:
                adj_ls[n1] = []
            adj_ls[n1].append(n2)
            course_in[n2] += 1
        q = deque([i for i, v in enumerate(course_in) if v == 0])
        visited = 0
        while q:
            item = q.popleft()
            visited += 1
            for n in adj_ls.get(item, []):
                course_in[n] -= 1
                if course_in[n] == 0:
                    q.append(n)
        return visited == numCourses




print(Solution().canFinish(6, [[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]]))
