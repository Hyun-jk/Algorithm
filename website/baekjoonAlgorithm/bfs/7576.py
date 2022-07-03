#토마토

#상자의 크기 M = 가로 칸수, N = 세로 칸수 (2<= M,N <= 1000)
#둘째 줄부터 토마토의 정보
#1, 익은 토마토, 0은 익지 않은 토마토 -1 토마토가 들어있지 않은 칸
#토마토가 익지 못하는 상황이면 -1

#문제 방향성)
# 다 못익은 경우 -1를 출력 해야하는데  조건 체크를 어떻게 할까...?
#>>> 먼저 토마토가 존재하는 좌표를 전부 찾아 리스트에 저장해둔다.
# 좌표 값에 1을 더해준다
#조건을 다시 한번 graph탐색을 하여 0이 존재할 시에 -1을 출력한다. 그렇지 않다면 최대 값에 1을 빼서 출력한다.

from collections import deque
m,n = map(int,input().split()) #m = 가로 칸수, n = 세로 칸수
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

#상,하,좌,우
dx = [0,0,-1,0]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    cnt =0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny <0 or nx >= m or ny >= n:
                continue

            if graph[nx][ny] ==1:
                continue

            if graph[nx][ny] ==0:
                 graph[nx][ny] = graph[x][y] +1
                 queue.append((nx,ny))
bfs(0,0)
res = 0
#m = 가로 칸수, n = 세로 칸수
for i in graph:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    res = max(res,max(i))        
    print(res-1)
            



                

