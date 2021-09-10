"""
BT -  at max two children
complete
perfect
full


traversals-
preorder - Root L R
in - L root R
post - L R Root


"""

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return
    print(root.data,end = " ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

    
root = Node(5)
root.left = Node(10)
root.right = Node(15)

root.left.left = Node(20)
root.left.right = Node(30)

preorder(root)
print()