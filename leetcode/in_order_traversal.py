class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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

if __name__=="__main__":
    n1 = TreeNode(47)
    n2 = TreeNode(23)
    n3 = TreeNode(80)
    n4 = TreeNode(21)
    n5 = TreeNode(30)
    n6 = TreeNode(64)
    n7 = TreeNode(85)
    n8 = TreeNode(15)
    n9 = TreeNode(22)
    n10 = TreeNode(99)

    n1.left = n2
    n1.right = n3

    n2.left = n4
    n2.right = n5

    n4.left = n8
    n4.right = n9

    n3.left = n6
    n3.right = n7

    n7.right = n10

    for e in inorderTraversal(n1):
        print(e)
