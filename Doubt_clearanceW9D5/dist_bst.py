class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None
def dist_root(root,z):#root = 21,x = 25
    if root.data == z:
        return 0
    elif root.data>z:
        return 1+dist_root(root.left,z)
    else:
        return 1+dist_root(root.right,z)

def dist(root,x,y):
    if root is None:
        return 0
    if x<root.data and y <root.data:
        return dist(root.left,x,y)

    if x>root.data and y >root.data:
        return dist(root.right,x,y)

    if root.data>x and y>root.data:
        return dist_root(root,x)+dist_root(root,y)


root = Node(5)
#LST
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left  =  Node(3)

#RST
root.right = Node(12)
root.right.left = Node(9)
root.right.right = Node(21)
root.right.right.left = Node(19)
root.right.right.right = Node(25)


    
res = dist(root,19,25)
print(res)

