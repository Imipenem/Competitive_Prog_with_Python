class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
145. Binary Tree Postorder Traversal : Left-Right-Root ; Recursive :28 ms, faster than 89.98% 
"""
def postorderTraversal(root: TreeNode) -> [int]:
    if not root: return []
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


"""
145. Binary Tree Postorder Traversal : Left-Right-Root ; Iterative: 24 ms, faster than 96.43%
"""
def postorderTraversalIterative(root: TreeNode) -> [int]:
    if not root: return []
    s1, s2 = [root], []

    while s1:
        current = s1.pop()
        s2.append(current.val)
        if current.left: s1.append(current.left)
        if current.right: s1.append(current.right)

    s2.reverse()

    return s2

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.right = n2
    n2.left = n3

    print(postorderTraversalIterative(n1))