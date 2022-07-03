#미로탐색

from collections import deque

#N,M 크기의 미로
N,M = map(int,input().split()) 

#언제 크기를 +1 하고, 그냥 0,0으로 하고 나중에 -1을 하는게 좋을까??
#미로정보
maze = []
for _ in range(N):
    maze.append(list(map(int,input())))

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    #bfs는 큐를 이용 해야하기 때문에 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때까지 사용
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾는 공간에서 벗어난 경우 무시
            #0 == 벽, N,M는 미로 최대크기
            if nx < 0 or ny <0 or nx >=N or ny>=M:
                continue
            #벽인 경우 무시
            if maze[nx][ny] ==0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] ==1:
                maze[nx][ny] = maze[x][y] +1
                queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단거리 반환
    return maze[N-1][M-1]

print(bfs(0,0))

