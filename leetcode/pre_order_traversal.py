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
def preorderTraversalI(root: TreeNode) -> [int]:
    if not root: return []
    res = [root.val]
    res += preorderTraversalI(root.left)
    res += preorderTraversalI(root.right)
    return res

#beats about 90% 28ms
def preorderTraversalII(self, root: TreeNode) -> [int]:
    if not root: return []
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


"""
Iterative Solution: 32ms beats 75%. only pushes right child on temp stack
"""
def preorderTraversalIterative(root: TreeNode) -> [int]:
    stack, res = [], []
    current = root

    while current:
        res.append(current)

        if current.left:
            if current.right: stack.append(current.right)
            res.append(current.left)
            current = current.left
        elif current.right:
            current = current.right
        else:
            if stack: current = stack.pop()
    return res

#beats 90% 28ms, pushes every node onto the stack
def preorderTraversalIterativeII(root: TreeNode) -> [int]:
    if root is None: return []
    stack, res = [root], []

    while stack:
        current = stack.pop()
        res.append(current.val)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return res