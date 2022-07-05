# 연결 요소의 개수
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# 첫째 줄에 연결 요소의 개수를 출력한다. >>이게 무슨 말일까?

from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph,visited,start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

m, n = map(int, input().split())  # m = 정점의 개수, n = 간선의 개수
graph = [[] for _ in range(m+1)]

# 연결된 노드 정보를 2차 리스트 graph에 넣는다.
for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (m+1)
count = 0

for i in range(1, m+1):
    if not visited[i]:      # 만약 방문하지 않았다면
        if not graph[i]:    #만약 그래프가 비어있다면
            count += 1
            visited[i] = True
        else: #만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(graph,visited,i) #해당 i를 시작노드로 bfs를 돈다
            count += 1 #연결 요소 를 +1개 해준다.
print(count)            

