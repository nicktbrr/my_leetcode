from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def dfs(self, node):
        if not node:
            return -1
        l_height = self.dfs(node.left) + 1
        r_height = self.dfs(node.right) + 1
        if l_height + r_height > self.res:
            self.res = l_height + r_height
        return max(l_height, r_height)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(Solution().diameterOfBinaryTree(root))