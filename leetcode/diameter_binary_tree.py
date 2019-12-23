class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def diameterOfBinaryTree(root: TreeNode) -> int:

    diameterOfBinaryTree_help.diameter = 0
    diameterOfBinaryTree_help(root)
    return diameterOfBinaryTree_help.diameter - 1


def diameterOfBinaryTree_help(root: TreeNode) -> int:

    if not root: return 0

    left_height = diameterOfBinaryTree_help(root.left) #height left subtree
    right_height = diameterOfBinaryTree_help(root.right) #height right subtree

    poss_max_dia = left_height + right_height + 1

    diameterOfBinaryTree_help.diameter = max(diameterOfBinaryTree_help.diameter,poss_max_dia)

    return max(left_height,right_height) + 1


if __name__ == "__main__":
    print()