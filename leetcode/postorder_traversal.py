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

    for e in postorderTraversal(n1):
        print(e)