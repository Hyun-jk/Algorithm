# 영역 구하기
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < M and 0 <= nx < N and paper[ny][nx] == 0:
                paper[ny][nx] = 1
                q.append((ny, nx))
                cnt += 1
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
            answer.append((bfs(i, j)))

print(len(answer))
print(*sorted(answer))


# 돌면서 넓이 구하기
