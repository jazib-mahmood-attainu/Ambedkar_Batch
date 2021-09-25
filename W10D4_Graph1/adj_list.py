graph = dict()

def addEdge(u,v,wt,dir):
    if u not in graph:
        graph[u] = []
    graph[u].append((v,wt))

    if not dir:
        if v not in graph:
            graph[v] = []
        graph[v].append((u,wt))


addEdge(1,2,1,True)
addEdge(0,3,1,True)
addEdge(2,3,1,True)
addEdge(3,2,1,True)
addEdge(2,5,1,True)

print(graph)
    