class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None

max_level = float("-inf")
def printLeft(root,cur_levl):
    global max_level
    if root is None:
        return
    if cur_levl>max_level:
        print(root.data)
        max_level = cur_levl

    printLeft(root.left,cur_levl+1)
    printLeft(root.right,cur_levl+1)



if __name__=="__main__":
    root = Node(50)

    root.left = Node(60)

    root.right = Node(100)

    root.left.left = Node(70)
    root.left.right = Node(90)
    root.right.left = Node(20)
    root.right.left.left = Node(110)
    root.right.left.right = Node(5)

    root.right.right = Node(80)

    printLeft(root,1)