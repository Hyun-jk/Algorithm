# 벽 부수고 이동하기
# 잘한점
# 기본적인 BFS는 구현을 하였다.
# 벽을 하나 깨서 최소거리를 구하는 것은 생각하지 못하였다.
# 3차원 행렬을 만들어 마지막 인덱스를 가지고 벽을 깰지 말지 정한다


from collections import deque

# n는 세로 m는 가로
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 3차원 행렬을 통해 벽의 파괴를 파악함, visited[x][y][0] = 0은 벽 파괴 가능, [x][y][0] = 1은 불가능
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
print(visited)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()

        # 끝 점에 도달하면 이동 횟수를 출력
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위가 넘어가면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽 파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이라면
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

    return -1


print(bfs(0, 0, 0))
