class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None


def solve(root):
    if root is None:
        return
    root.left,root.right = root.right,root.left
    solve(root.left)
    solve(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data,end = " ")
    preorder(root.left)
    preorder(root.right)
    


    


root = Node(5)

root.left = Node(6)
root.right = Node(7)

root.right.left = Node(8)
root.right.right = Node(9)

preorder(root)
print("***********")
solve(root)
print("***********")
preorder(root)
print("***********")

    