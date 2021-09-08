class Node:
    def __init__(self,x) -> None:
        self.data = x 
        self.next = None 

head = None
def addNodeAtEnd(x):
    global head
    if head is None:
        head  = Node(x)
        return
    cur = head
    while cur.next!=None:
        cur = cur.next
    new_node = Node(x)
    cur.next = new_node

def printLL():
    global head
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next

addNodeAtEnd(10)
addNodeAtEnd(20)
addNodeAtEnd(30)
addNodeAtEnd(40)
addNodeAtEnd(50)
addNodeAtEnd(60)

# print(head.data)
# print(head.next.data)
# print(head.next.next.data)

printLL()

    

    
