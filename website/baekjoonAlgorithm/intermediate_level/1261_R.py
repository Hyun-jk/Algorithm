from collections import deque
#알고스팟
m,n = map(int,input().split()) #m(가로크기), n(세로크기)
maze = [list(map(int,input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

#이동(상하좌우)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = deque()
q.append((0,0))
visited[0][0] = 0

while q:
    x,y = q.popleft()
    for i in range(4):
        nx,ny = x + dx[i], y +dy[i]
        #범위 안에 있는 경우
        if 0<= nx < n and 0<= ny < m:
            if visited[nx][ny] == -1: #아직 방문 안한 경우
                if maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] +1
                    q.append((nx,ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))

print(visited[n-1][m-1])

