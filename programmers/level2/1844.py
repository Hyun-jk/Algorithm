# 게임 맵 최단 거리
from collections import deque


def solution(maps):
    n = len(maps)  # 세로
    m = len(maps[0])  # 가로
    temp = [[-1] * m for _ in range(n)]
    temp[0][0] = 1
    q = deque()
    q.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            return temp[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y] + 1
                    q.append([nx, ny])

    return -1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

print(solution(maps))
