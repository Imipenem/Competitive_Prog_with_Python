from .pre_order_traversal import TreeNode
"""
94. Binary Tree Inorder Traversal: InOrder is left-root-right; Recursive 32ms 75%
"""
def inorderTraversal(root: TreeNode) -> [int]:
    if not root: return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

"""
28ms beats 90%
"""
def inorderTraversalII(root: TreeNode) -> [int]:
    if not root: return []
    res = []
    res += inorderTraversalII(root.left)
    res += [root.val]
    res += inorderTraversalII(root.right)
    return res



"""
94. Binary Tree Inorder Traversal: InOrder is left-root-right; Iterative 24ms beats 96%
"""
def inorderTraversalIterative(root: TreeNode) -> [int]:
    if not root: return []

    stack, res = [], []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        res.append(current.val)

        current = current.right

    return res
