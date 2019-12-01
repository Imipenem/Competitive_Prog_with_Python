# 701. Insert into a Binary Search Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#112 ms, faster than 95.81%
def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root: return TreeNode(val)

    prev,current = None,root
    while current:
        prev = current
        if current.val < val: current = current.right
        else: current = current.left

    if val > prev.val: prev.right = TreeNode(val)
    else: prev.left = TreeNode(val)

    return root

