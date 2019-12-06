########## Unterstützender Code ##########
class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None

########## Lösung ##########

def delete(root, delete):
    return deleteI(root,delete.key)

def deleteI(root, key):

    if not root: return root

    elif key < root.key:
        root.left = deleteI(root.left, key)

    elif key > root.key:
        root.right = deleteI(root.right, key)

    else:
        if not root.left:
            temp = root.right
            if temp: temp.parent = root.parent
            root = None
            return temp

        elif not root.right:
            temp = root.left
            if temp: temp.parent = root.parent
            root = None
            return temp

        else:
            node = inorderSucc(root.right)
            root.key = node.key
            root.right = deleteI(root.right,node.key)
    return root


def inorderSucc(root):
    current = root

    while current.left:
        current = current.left
    return current