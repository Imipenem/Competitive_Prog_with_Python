# 450. Delete Node in a BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def searchBST(root: TreeNode, val: int):
    current = root
    while current:
        if current.val == val: return current
        elif current.val < val: current = current.right
        else: current = current.left
    return None


def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if not root: return None

    prev = None
    to_del = root

    # search for the node with key and its parent
    while to_del:
        if to_del.val == key:
            break
        elif to_del.val < key:
            prev = to_del
            to_del = to_del.right
        else:
            prev = to_del
            to_del = to_del.left
    if not to_del: return root  # we did not found the key in our BST

    # Our node is a leaf: Case 1
    if not to_del.right and not to_del.left:
        if to_del is root:
            return None  # if node to delete is root (single root element BST)
        elif prev.val < to_del.val:
            prev.right = None
        else:
            prev.left = None
        return root

        # Our Node has only one child (either right or left): Case 2

    elif not to_del.right:
        if not prev:
            return to_del.left  # delete root node with only a left subtree
        else:
            prev.left = to_del.left
            return root

    elif not to_del.left:
        if not prev:
            return to_del.right  # delete root node with only a right subtree
        else:
            prev.right = to_del.right
            return root

    # Our Node has two childs: Case 3

    else:
        print()


