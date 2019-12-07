class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBalanced(root: TreeNode) -> bool:
    if not root: return True

    lh = get_depth(root.left)
    rh = get_depth(root.right)

    return abs(lh - rh) <= 1 and isBalanced(root.left) and isBalanced(root.right)




def get_depth(root: TreeNode) -> int:
    if not root: return 0
    return 1 + max(root.left,root.right)
