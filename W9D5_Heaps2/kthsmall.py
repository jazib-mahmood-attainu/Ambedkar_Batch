import heapq
l = [5,6,2,12,3,9]

heap = []
k = 3

for item in l:
    heapq.heappush(heap,item)

ctr = 0

while ctr<k:
    ans = heapq.heappop(heap)
    ctr+=1
print(ans)



