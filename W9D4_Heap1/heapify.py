heap = [8,5,6,3,9,8,3,9,1,8]
def heapify(i):
    global heap

    left_idx = 2*i+1
    right_idx = 2*i+2

    if left_idx>len(heap)-1 and right_idx>len(heap)-1:
        ##leaf node
        return
    
    max_idx = i

    if left_idx<len(heap) and heap[left_idx]>heap[i]:
        max_idx = left_idx

    if right_idx<len(heap) and heap[right_idx]>heap[max_idx]:
        max_idx = right_idx

    if max_idx!=i:
        heap[i],heap[max_idx] = heap[max_idx],heap[i]
        heapify(max_idx)


def heapsort():
    global heap
    while(len(heap)!=0):
        print(heap[0], end = " ")
        heap[0],heap[-1] = heap[-1],heap[0]
        heap.pop()
        heapify(0)
    
    
if __name__=="__main__":
    n = len(heap)
    print(heap)
    for i in range(n-1,-1,-1):
        heapify(i)
    print(heap)    
    heapsort()

