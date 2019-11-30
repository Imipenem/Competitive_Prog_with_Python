#144. Binary Tree Preorder Traversal LEETCODE


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Recursive strategy: Pre-Order is: Root-Left-Right
"""

#beats about 99% 20ms
def preorderTraversal(root: TreeNode) -> [int]:
    if not root: return []
    res = [root.val]
    res += preorderTraversal(root.left)
    res += preorderTraversal(root.right)
    return res

#beats about 90% 28ms
def preorderTraversalII(self, root: TreeNode) -> [int]:
    if not root: return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

