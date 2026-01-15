from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sub_tree_sum = []
        def sub_sum(root):
            if not root:
                return 0
            curr_sum = root.val + sub_sum(root.left) + sub_sum(root.right)
            sub_tree_sum.append(curr_sum)
            return curr_sum
        sub_sum(root)
        total_sum = sub_tree_sum[-1]
        res = 0
        for s in sub_tree_sum[:-1]:
            res = max(res, (total_sum - s) * s)
        return res % (10**9 + 7)



root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().maxProduct(root))