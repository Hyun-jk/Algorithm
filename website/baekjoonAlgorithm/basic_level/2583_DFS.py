# 영역 구하기

def dfs(i, j, cnt):
    paper[i][j] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        ny = i + dy[i]
        nx = j + dx[i]

        if 0 <= ny < N and 0 <= nx < M and paper[ny][nx] == 0:
            cnt = dfs(ny, nx, cnt+1)
    return cnt


M, N, K = map(int, input().split())
locations = []
paper = [[0] * N for _ in range(M)]
for _ in range(K):
    start_x, start_y, end_x, end_y = map(int, input().split())

    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            paper[i][j] = 1

answer = []

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            paper[i][j] = 1
            answer.append((dfs(i, j, 1)))
