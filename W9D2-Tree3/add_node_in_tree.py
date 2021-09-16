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



def addNodesatlevel(root,l,val):
    if l==1 and root is None:
        # print(val)
        return Node(val)
    addNodesatlevel(root.left,l-1,val)
    addNodesatlevel(root.right,l-1,val)

def addlevelwise(root,val):
    
    ht = count_ht(root)+1
    for l in range(1,ht+1):
        addNodesatlevel(root,l,val)
        print(root)
    return root




def preorder(root):
    if root is None:
        return
    print(root.data,end = " ")
    preorder(root.left)
    preorder(root.right)



root = None
root = addlevelwise(root,5)
preorder(root)
