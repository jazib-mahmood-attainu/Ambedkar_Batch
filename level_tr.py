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

def printNodesatlevel(root,l):
    if root is None:
        return 
    if l==1:
        print(root.data,end=" ")
        return
    printNodesatlevel(root.left,l-1)
    printNodesatlevel(root.right,l-1)


    
def printlevelwise(root):
    if root is None:
        return 
    ht = count_ht(root)
    for l in range(1,ht+1):
        printNodesatlevel(root,l)


root = Node(50)

root.left = Node(60)
root.right = Node(100)

root.right.left = Node(20)
root.right.right = Node(80)

printlevelwise(root)


    