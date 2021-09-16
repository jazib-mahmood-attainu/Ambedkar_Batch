class Node:
    def __init__(self,val):
        self.data = val
        self.left  = None
        self.right = None

def checkifValidBST(root):
    if root is None:
        return {
                "min_val":float("inf"),
                "max_val":float("-inf"),
                "isBST":True
                }
    if root.left is None and root.right is None:
        return {
            "min_val":root.data,
            "max_val":root.data,
            "isBST":True
                }
    left_ans = checkifValidBST(root.left)
    right_ans = checkifValidBST(root.right)

    if left_ans["isBST"] and right_ans["isBST"] and root.data>left_ans["max_val"] and root.data<right_ans["min_val"]:
        return {
                "min_val":min(root.data,left_ans["min_val"]),
                "max_val":max(root.data,right_ans["max_val"]),
                "isBST":True
                }
    else:
        return{
                "min_val":min(root.data,left_ans["min_val"]),
                "max_val":max(root.data,right_ans["max_val"]),
                "isBST":False
                }


root = Node(5)
root.left = Node(1)
root.right = Node(15)

root.right.left = Node(10)
root.right.right = Node(30)

res = checkifValidBST(root)
print(res["isBST"])