class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = {}

        def postOrder(root, level):
            if not root:
                return
            if level not in levels:
                levels[level] = []
            levels[level].append(root.val)
            postOrder(root.right, level + 1)
            postOrder(root.left, level + 1)

        postOrder(root, 0)
        res = sorted(levels.items(), key=lambda x: x[0])
        res = [sum(v) / len(v) for k, v in res]
        print(res)
        return res

