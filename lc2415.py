from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def p_DFS(l_root, r_root, level):
            if l_root is None:
                return level - 1
            c_level = p_DFS(l_root.left, r_root.right, level + 1)
            if c_level % 2 == 1:
                # print(l_root.val, r_root.val)
                l_root.val, r_root.val = r_root.val, l_root.val
                # print(l_root.val, r_root.val)
            c_level = p_DFS(l_root.right, r_root.left, level + 1)
            return level - 1
        p_DFS(root.left, root.right, 1)
        return root

def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

n3 = TreeNode(val = 8)
n4 = TreeNode(val = 13)
n5 = TreeNode(val = 21)
n6 = TreeNode(val = 34)
n1 = TreeNode(val = 3, left=n3, right=n4)
n2 = TreeNode(val = 5, left=n5, right=n6)
root = TreeNode(val = 2, left=n1, right=n2)
s = Solution()
print_tree(root)
print(s.reverseOddLevels(root))
print_tree(root)