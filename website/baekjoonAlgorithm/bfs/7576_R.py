# 토마토

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(lst):
    q = deque()
    
    #익은 토마토의 위치를 모두 q에 넣는다
    for i in lst: 
        q.append(i)
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y + dy[i]

            if 0<=nx < n and 0<= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1

#토마토 위치 정보를 넣는다.
lst = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            lst.append((i, j))

#인접한 토마토  익힘
bfs(lst)

#결과 확인
def result():
    anwser = 0
    for i in range(n):
        for j in range(m):
            #좌표를 돌면서 안익은 토마토(0)이 발견되면 -1
            if graph[i][j] == 0:
                return print(-1)

            #다 익었으면 제일 오래 걸린 날짜를 출력한다.    
            anwser = max(anwser, graph[i][j])
    
    #graph[nx][ny] = graph[x][y] + 1 로 코드를 짯으니, 날짜를 알고 싶으면, -1을 해서 출력을 해야한다.
    return print(anwser-1) 


result()
