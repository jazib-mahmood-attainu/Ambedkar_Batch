class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
head3 = None
def merge(head1,head2):
    p1 = head1
    p2 = head2
    global head3
    cur  = head3

    while (p1 is not None) and (p2 is not None):
        if p1.data<p2.data:
            #if p1.data is smaller
            if head3 is None:
                head3 = Node(p1.data)
                cur = head3
            
            else:
                cur.next = Node(p1.data)
                cur = cur.next
            
            p1 = p1.next

        else:
            #if p2.data is smaller
            if head3 is None:
                head3 = Node(p2.data)
                cur = head3
            
            else:
                cur.next = Node(p2.data)
                cur = cur.next
            
            p2 = p2.next

    while p2!=None:
        cur.next = Node(p2.data)
        cur=cur.next
        p2 = p2.next
    
    while p1!=None:
        cur.next = Node(p1.data)
        cur=cur.next
        p1 = p1.next

    return head3


def printLL(head):
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next


head1 = Node(1)
head1.next = Node(8)
head1.next.next = Node(10)

head2 = Node(5)
head2.next = Node(16)
head2.next.next = Node(17)


printLL(head1)
print("***********")
printLL(head2)

print("***********")
printLL(merge(head1,head2))