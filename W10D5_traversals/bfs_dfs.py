graph = dict()

def addEdge(u,v,wt,dir):
    if u not in graph:
        graph[u] = []
    graph[u].append((v,wt))

    if not dir:
        if v not in graph:
            graph[v] = []
        graph[v].append((u,wt))

def bfs(src):
    visited = [False]*1000
    queue = []
    queue.append(src)
    visited[src] = True
    while len(queue)!=0:
        x = queue.pop(0)
        print(x)
        for neighbour,_ in graph[x]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True

def dfs(src,visited):
    print(src)
    visited[src] = True
    for neighbour,_ in graph[src]:
        if not visited[neighbour]:
            dfs(neighbour,visited)


                



addEdge(0,2,1,False)
addEdge(2,3,1,False)
addEdge(0,3,1,False)
addEdge(1,3,1,False)
addEdge(0,1,1,False)

print(graph)

bfs(2)
print("*********")
visited = [False]*1000
dfs(2,visited)