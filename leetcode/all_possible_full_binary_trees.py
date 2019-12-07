class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def allPossibleFBT(N: int) -> [TreeNode]:
    if N % 2 == 0: return []
    elif N == 1: return [TreeNode(0)]

    res = []

    for i in range(1,N,2):
        left_nodes = allPossibleFBT(i)
        right_nodes = allPossibleFBT(N-1-i)

        for l in left_nodes:
            for r in right_nodes:
                root = TreeNode(0)
                root.left = l
                root.right = r
                res.append(root)
    return res

