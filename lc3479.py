from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        def make_seg_tree(baskets):
            n = len(baskets)
            N = 1
            while N <= n:
                N <<= 1

            segTree = [0] * (2 * N)

            for i in range(n):
                segTree[N + i] = baskets[i]

            for i in range(N - 1, 0, -1):
                segTree[i] = max(segTree[2 * i], segTree[2 * i + 1])
            return segTree

        def search_update(seg_tree, fruit, n):
            if fruit > seg_tree[1]:
                return 0
            i = 1
            while i < N:
                if seg_tree[i * 2] >= fruit:
                    i = i * 2
                else:
                    i = i * 2 + 1
            seg_tree[i] = 0
            while i > 1:
                i //= 2
                seg_tree[i] = max(seg_tree[i * 2], seg_tree[i * 2 + 1])
            return 1

        sef_tree = make_seg_tree(baskets)
        res = 0
        n = len(baskets)
        N = 1
        while N <= n:
            N <<= 1
        for fruit in fruits:
            res += search_update(sef_tree, fruit, N)
        return len(fruits) - res


print(Solution().numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
print(Solution().numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))
print(Solution().numOfUnplacedFruits([2,16,53,100,61],[46,7,78,30,30]))