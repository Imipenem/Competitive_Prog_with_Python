#102. Binary Tree Level Order Traversal aka Breadth-First Search

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root: TreeNode) -> [[int]]:
    if not root: return []
    queue, res = [root], []

    while queue:
        size = len(queue)
        level = []

        for i in range(size):
            current = queue.pop(0)
            level.append(current.val)
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)

        res.append(level)
    return res
