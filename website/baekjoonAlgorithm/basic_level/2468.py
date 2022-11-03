# 안전영역
from collections import deque


def bfs(i, j, height):
    visited[i][j] = -1
    q = deque()
    q.append((i, j))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] <= height:
                    visited[nx][ny] = -1
                    q.append((nx, ny))
    return visited


def count_safe(visited):
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, max_height)
                count += 1

    print(visited)
    print(count)
    return count


n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
max_height = 0

for i in range(n):
    info = list(map(int, input().split()))
    max_height = max(max_height, max(info))
    graph.append(info)

height = 0
answer = 0
while height <= max_height:
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= height and visited[i][j] == 0:
                bfs(i, j, height)
    print(f'height={height}')
    print(visited)
    count = count_safe(visited)
    answer = max(answer, count)
    visited = [[0]*n for _ in range(n)]
    height += 1

print(answer)
