# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return []
        queue = [root]
        def BFS(queue):
            connect_queue = []
            while queue:
                node = queue.pop(0)
                if not node.right and not node.left:
                    continue
                if node.left:
                    connect_queue.append(node.left)
                if node.right:
                    connect_queue.append(node.right)
            if len(connect_queue) >= 2:
                for i in range(1, len(connect_queue)):
                    connect_queue[i - 1].next = connect_queue[i]
            if not connect_queue:
                return
            BFS(connect_queue)
        BFS(queue)
        return root



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
print(Solution().connect(root))