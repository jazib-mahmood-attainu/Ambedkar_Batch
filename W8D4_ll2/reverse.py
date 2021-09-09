class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

def printLL(head):
    cur = head
    while cur!=None:
        print(cur.data, end = " ")
        cur = cur.next


def rev_LL(head):
    prev = None
    cur = head

    while cur!=None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev

head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = Node(20)

printLL(head)
print()

printLL(rev_LL(head))
print()