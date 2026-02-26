class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_sum = [(sum(r), idx) for idx, r in enumerate(mat)]
        temp = sorted(row_sum, key=lambda x: [x[0], x[1]])
        return [t[1] for t in temp[:k]]

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        tot = counter.total()
        curr_tot = 0
        nums = set()
        n = len(arr)
        for k,v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
            curr_tot += v
            nums.add(k)
            if curr_tot >= n // 2:
                break
        return len(nums)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        sums = []

        def split_sum(root, total_sum):
            if not root:
                return 0
            l_sum = split_sum(root.left, total_sum)
            r_sum = split_sum(root.right, total_sum)
            total_sum = root.val + l_sum + r_sum
            sums.append(total_sum)
            return total_sum

        split_sum(root, total_sum)
        total_sum = sums[-1]
        res = 0
        for i in range(len(sums) - 1):
            res = max(res, ((total_sum - sums[i]) * sums[i]))
        return res % (10 ** 9 + 7)


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = {i:-1 for i in range(n)}
        def path(i):
            res = 1
            if memo[i] != -1:
                return memo[i]
            for l in range(1, d + 1):
                if i - l >= 0 and arr[i-l] < arr[i]:
                    res = max(res, path(i-l) + 1)
                else:
                    break
            for r in range(1, d + 1):
                if i + r < n and arr[i+r] < arr[i]:
                    res = max(res, path(i+r) + 1)
                else:
                    break
            memo[i] = res
            return res
        for i in range(n):
            path(i)
        return max(memo.values())
