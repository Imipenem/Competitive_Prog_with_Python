#LEETOCDE: 104. Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    if not root: return 0
    else: return max(1+maxDepth(root.left), 1+maxDepth(root.right))


#TODO: Implement iterative way for a O(1) space solution
def maxDepthII(root: TreeNode) -> int:
    print("PLACEHODLER")


if __name__ == "__main__":

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1.left = n2
    n2.left = n3

    print(maxDepth(n1))