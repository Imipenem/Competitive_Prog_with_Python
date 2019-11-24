#112. Path Sum

class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


#beats 98% of all submissions, much less messy than above
def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root: return False
    if not root.left and not root.right: return sum is root.val
    return (root.left and hasPathSumUtil(root.left, sum - root.val)) or (
                root.right and hasPathSumUtil(root.right, sum - root.val))


def hasPathSumUtil(root: TreeNode, sum: int) -> bool:
    if not root: return False
    if not root.left and not root.right:
        if sum - root.val is 0:
            return True
        else:
            return False

    return hasPathSumUtil(root.left, (sum - root.val)) or hasPathSumUtil(root.right, (sum - root.val))

#beats 95% of all submissions, much less messy than above
def hasPathSumII(self, root: TreeNode, sum: int) -> bool:
    if not root: return False
    if not root.left and not root.right:
        if sum - root.val is 0:
            return True
        else:
            return False

    return self.hasPathSum(root.left, (sum - root.val)) or self.hasPathSum(root.right, (sum - root.val))

if __name__ == "__main__":
    print()