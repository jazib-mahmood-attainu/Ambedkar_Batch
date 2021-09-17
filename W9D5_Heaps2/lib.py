"""
by deafult heapq builds a min-heap
"""
import heapq
heap = []

heapq.heappush(heap,2)
heapq.heappush(heap,12)
heapq.heappush(heap,222)
heapq.heappush(heap,1)
heapq.heappush(heap,5)

print(heap)

heap2 = []

#max heap
heapq.heappush(heap2,-2)
heapq.heappush(heap2,-12)
heapq.heappush(heap2,-222)
heapq.heappush(heap2,-1)
heapq.heappush(heap2,-5)
print(heap2)
x = heapq.heappop(heap2)
print(-1*x)

