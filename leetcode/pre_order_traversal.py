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
        res.append(current.val)

        if current.left:
            if current.right: stack.append(current.right)
            current = current.left
        elif current.right:
            current = current.right
        else:
            if stack:current = stack.pop()
            else:current = None
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

    for e in preorderTraversalI(n1):
        print(e)