def dfs(graph,visited,start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph,visited,i)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (1+n)
count =0

for i in range(1, n+1):
    if not visited[i]:
        if not graph[i]:
            count +=1
            visited[i] = True
        else:
            dfs(graph,visited,i)
            count +=1
print(count)            
