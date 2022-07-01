#DFS 와  BFS
from collections import deque

#N =정점의 개수 M = 간선의 개수 V = 시작할 정점의 번호
N,M,V = map(int,input().split())

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (N+1)

#각 노드가 연결된 정보를 리스트 자료형으로 표현
graph =[[]  for _ in range(N+1)]
for i in range(1,M+1):
    x, y  = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()


def dfs(graph,v,visited):
    visited[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visted):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visted[i]:
                queue.append(i)
                visited[i] = True

dfs(graph,V,visited)
visited = [False] * (N+1)
print()
bfs(graph,V,visited)