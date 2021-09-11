# """
# BT -  at max two children
# complete
# perfect
# full


# traversals-
# preorder - Root L R
# in - L root R
# post - L R Root


# """

# class Node:
#     def __init__(self,val):
#         self.data = val
#         self.left = None
#         self.right = None


# def preorder(root):
#     if root is None:
#         return
#     print(root.data,end = " ")
#     preorder(root.left)
#     preorder(root.right)

# def inorder(root):
#     if root is None:
#         return
#     inorder(root.left)
#     print(root.data)
#     inorder(root.right)

# def postorder(root):
#     if root is None:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.data)

    
# root = Node(5)
# root.left = Node(10)
# root.right = Node(15)

# root.left.left = Node(20)
# root.left.right = Node(30)

# preorder(root)
# print()

class Node: 
    def __init__(self,x): 
        self.data = x 
        self.next = None 
def printList(head): 
    cur = head 
    while cur!=None: 
        print(cur.data, end = " ") 
        cur = cur.next 
        new_head = None 
def reverse_LL_rec(head,prev): 
    global new_head 
    if head is None: 
        return 
    if head.next is None: 
        head.next = prev 
        return head 
    new_head = reverse_LL_rec(head.next,head) 
    head.next = prev 
    return new_head 
if __name__ == "__main__": 
    head = Node(5) 
    head.next = Node(15)
    head.next.next = Node(25) 
    head.next.next.next = Node(35) 
    printList(head) 
    print() 
    head_rev = reverse_LL_rec(head,None) 
    printList(head_rev) 
    print() 
