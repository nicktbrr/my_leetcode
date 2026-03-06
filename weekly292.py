# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        avgs = []

        def root_avg(root):
            if not root:
                return 0, 0
            v1, lc = root_avg(root.left)
            v2, rc = root_avg(root.right)
            curr_sum = v1 + v2 + root.val
            curr_count = lc + rc + 1
            if root.val == curr_sum // curr_count:
                avgs.append(root.val)
            return curr_sum, curr_count
        root_avg(root)
        return len(avgs)


root = TreeNode(4)
root.left = TreeNode(8)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.right = TreeNode(6)
print(Solution().averageOfSubtree(root))

