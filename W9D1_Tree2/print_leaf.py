class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None

def print_leaf(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data)

    print_leaf(root.left)
    print_leaf(root.right)
    


root = Node(50)

root.left = Node(60)
root.right = Node(100)

root.right.left = Node(20)
root.right.right = Node(80)

print_leaf(root)

