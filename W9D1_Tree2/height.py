class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None


def count_ht(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1        
    l = count_ht(root.left)
    r = count_ht(root.right)
    return max(l,r)+1


    


root = Node(50)

root.left = Node(60)
root.right = Node(100)

root.right.left = Node(20)
root.right.right = Node(80)

res = count_ht(root)
print(res)

    