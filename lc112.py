# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(root, curr_sum):
            if not root:
                return False
            curr_sum += root.val
            if not root.left and not root.right:
                return targetSum == curr_sum
            return DFS(root.right, curr_sum) or DFS(root.left, curr_sum)

        return DFS(root, 0)

        DFS(root, 0)
        return found_path
