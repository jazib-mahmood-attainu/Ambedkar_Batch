heap = [1,9,3,7,6,5,4,8,2]
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

    
heapify(0)

print(heap)
