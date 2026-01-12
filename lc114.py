from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def LRootR(root, prev):
            if not root:
                return
            LRootR(root.right, prev)
            LRootR(root.left, prev)
            root.right = self.prev
            root.left = None
            self.prev = root
        LRootR(root, None)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().flatten(root))