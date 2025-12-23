from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        root_idx = inorder.index(root.val)

        root.right = self.buildTree(inorder[root_idx + 1:], postorder)
        root.left = self.buildTree(inorder[:root_idx], postorder)

        return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

print(Solution().buildTree(inorder, postorder))