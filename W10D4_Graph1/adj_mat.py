n = 5
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

# for i in range(n+1):
#     for j in range(n+1):
#         print(graph[i][j], end = " ")
#     print()

def addEdge(u,v,wt,dir):
    graph[u][v] = wt
    if not dir:
        graph[v][u] = wt
    
    

addEdge(1,2,1,False)
addEdge(0,3,1,False)
addEdge(2,3,1,False)
addEdge(3,2,1,False)
addEdge(2,5,1,False)

print("col    0 1 2 3 4 5")
for i in range(n+1):
    print("row",i,end = "->")
    for j in range(n+1):
        print(graph[i][j], end = " ")
    print()
