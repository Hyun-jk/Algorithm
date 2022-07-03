#유기농 배추 나 혼자 한건데 이해가 안된다
from collections import deque
import sys

#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

input = sys.stdin.readline
T  = int(input())

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+dy[i]
            if 0<= nx < m and 0<= ny <n  and graph[ny][nx] ==1:
                graph[ny][nx] ==0
                queue.append((nx,ny))

for _ in range(T):
    m,n,k = map(int,input().split())
    graph =[[0] * m for _ in range(n)]
    result = 0
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] =1
    for i in range(m):
        for j in range(n):
            if graph[i][j] ==1:
                graph[i][j] =0
                bfs(i,j)
                result += 1

    print(graph)