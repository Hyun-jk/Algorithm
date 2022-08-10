#BFS 기초 알고리즘
#BFS = 너비 우선 탐색(Breadth-First Search)

from collections import deque
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        print(queue)
        print(visited)
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False] * 9
bfs(graph, 1, visited)

