class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1        
    l = count_nodes(root.left)
    r = count_nodes(root.right)
    return l+r+1


    


root = Node(50)

root.left = Node(60)
root.right = Node(100)

root.right.left = Node(20)
root.right.right = Node(80)

res = count_nodes(root)
print(res)

