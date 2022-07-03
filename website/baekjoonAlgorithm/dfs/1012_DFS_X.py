#유기농 배추 >>>이해가 안된다
def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx <M) and (0 <= ny <N) :
            if graph[ny][nx] ==1:
                graph[ny][nx] =-1
                dfs(nx,ny)

### 1                    
T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())  # M:가로, N:세로, K:개수
    graph = [[0]*M for i in range(N)]
    cnt = 0

    # 배추 위치에 1 표시
    for j in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

### 3        
    # dfs 활용해서 배추 그룹 수 세기
    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                cnt += 1

    # 정답을 위한 출력
    print(cnt)