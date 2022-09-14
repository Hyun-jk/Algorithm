#연결요소의 개수(graph)
n,m = map(int,input().split()) #n=노드의 개수, m=간선의 개수
graph =[[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x,y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start):
    visited[start] = True
    
    for i in graph[start]:
        if visited[i] == False:
            dfs(i)

count = 0
for i in range(1,n+1):
    if visited[i] ==False:
        dfs(i)
        count +=1

print(count)

