class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def printLL(head):
    cur = head
    while cur!=None:
        print(cur.data, end = " ")
        cur = cur.next

def addNodeAtEnd(head,x):
    if head is None:
        head = Node(x)
        
        return head
    cur = head
    while cur.next!=None:
        cur = cur.next
    new_node = Node(x)
    cur.next = new_node
    return head

def rev_swp(head):
    cur = head
    ctr = 0
    while cur!=None:
        ctr+=1
        cur = cur.next
    
    cur = head
    last = cur
    start = 0
    end = ctr-1
    
    while (start != end) and (start+1!=end):
        for i in range(start):
            cur = cur.next
        for i in range(end):
            last = last.next
        cur.data,last.data = last.data,cur.data
        start+=1
        end-=1    
        
    return head
    



head = None
head = addNodeAtEnd(head,1)
addNodeAtEnd(head,2)
addNodeAtEnd(head,3)
addNodeAtEnd(head,4)

printLL(head)
print()

printLL(rev_swp(head))
print()

