#바이러스
from itertools import count
import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) #노드의 개수
K = int(input()) #간선의 개수

#간선 입력을 위한 2차 리스트
graph = [[]  for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(K):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(visited,graph,start):
    queue = deque([start])
    visited[start] = True
    count = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] ==False:
                visited[i] = True
                queue.append(i)
                count +=1
        print(count)
    return count


print(bfs(visited,graph,1))    









