# class Solution:
#     def totalMoney(self, n: int) -> int:
#         start = 1
#         res = 0
#         for i in range(n):
#             dow = i % 7
#             if i > 0 and dow == 0:
#                 start += 1
#             res += start + dow
#
#         return res
#
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         def calc_points(s, pair, points):
#             if s == "":
#                 return 0, ""
#             stack = [s[0]]
#             res = 0
#             for c in s[1:]:
#                 if stack and stack[-1] + c == pair:
#                     stack.pop()
#                     res += points
#                 else:
#                     stack.append(c)
#             return res, "".join(stack)
#         s1 = ""
#         if x > y:
#             res1, s1 = calc_points(s, "ab", x)
#             res2, _ = calc_points(s1, "ba", y)
#             return res1 + res2
#         else:
#             res1, s1 = calc_points(s, "ba", y)
#             res2, _ = calc_points(s1, "ab", x)
#             return res1 + res2
#
#
# from typing import List
#
#
# class Solution:
#     def constructDistancedSequence(self, n: int) -> List[int]:
#         largest = 2 * n - 1
#         arr = [0] * largest
#         used = set()
#
#         def fill(idx):
#             if idx == len(arr):
#                 return True
#             if arr[idx] != 0:
#                 return fill(idx + 1)
#             for num in range(n, 0, -1):
#                 if num in used:
#                     continue
#                 if num > 1:
#                     if idx + num < len(arr) and arr[idx] == 0 and arr[idx + num] == 0:
#                         arr[idx] = arr[idx + num] = num
#                         used.add(num)
#                         if fill(idx + 1):
#                             return True
#                         arr[idx] = arr[idx + num] = 0
#                         used.remove(num)
#                 else:
#                     arr[idx] = 1
#                     used.add(1)
#                     if fill(idx + 1):
#                         return True
#                     arr[idx] = 0
#                     used.remove(1)
#
#         fill(0)
#         return arr
#
#

from collections import defaultdict
from typing import List


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # 1. Build Adjacency Sets
        adj = defaultdict(set)
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)

        # 2. Sort nodes by degree (descending)
        # Higher degree nodes are higher up in the potential tree
        nodes = sorted(adj.keys(), key=lambda x: len(adj[x]), reverse=True)
        n = len(nodes)

        # 3. Root Check
        # The first node must be connected to every other node
        if len(adj[nodes[0]]) != n - 1:
            return 0

        res = 1
        # 4. Process each node and find its parent
        for i, u in enumerate(nodes):
            # Find the best candidate for u's parent:
            # It must be a neighbor with the smallest degree that is >= len(adj[u])
            parent = -1
            min_parent_degree = float('inf')

            # We look at nodes that appeared EARLIER in the sorted list
            for j in range(i - 1, -1, -1):
                v = nodes[j]
                if v in adj[u]:
                    # Because the list is sorted by degree, the neighbor
                    # appearing closest to 'u' in the list has the smallest degree >= u
                    parent = v
                    break

            if parent == -1:
                # If we aren't the root and have no parent, this is impossible
                if i == 0: continue
                return 0

            # 5. The Subset Rule
            # Every neighbor of 'u' (except the parent) MUST be a neighbor of the parent
            for neighbor in adj[u]:
                if neighbor == parent:
                    continue
                if neighbor not in adj[parent]:
                    return 0

            # 6. Check for Multiple Ways
            # If the degrees are equal, the nodes are interchangeable
            if len(adj[u]) == len(adj[parent]):
                res = 2

        return res


print(Solution().checkWays([[1, 5], [1, 2], [1, 3], [2, 3], [1, 4], [2, 4]]))