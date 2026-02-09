from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        def reconstruct(l, h):
            if h < l:
                return None
            mid = (h + l) // 2
            root = TreeNode(val=arr[mid])
            root.left = reconstruct(l, mid - 1)
            root.right = reconstruct(mid + 1, h)
            return root
        temp = reconstruct(0, len(arr) - 1)
        return temp




root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root.right.right.right = TreeNode(4)

print(Solution().balanceBST(root))