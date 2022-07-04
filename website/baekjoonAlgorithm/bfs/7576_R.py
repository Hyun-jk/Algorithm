# 토마토
"""
풀이)
1. 먼저 토마토가 존재하는 좌표를 전부 찾아 리스트에 저장해둔다
2. 리스트 안의 좌표들을 하나씩 bfs로 탐색을 하여 익지않은 토마토가 있는 경우 현재 좌표의 값을 1을 더해준다
3. 최종적으로 다시한번 graph를 탐색하여 0이 존재하면 -1, 그렇지 않으면 graph안의 최대값에서 1을 빼서 출력한다

"""
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(lst):
    q = deque()
    for i in lst:
        q.append(i)
        print(f'q는 {q}')
    while q:
        x, y = q.popleft()
        print(f'x = {x} y ={y}')
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1
                print(q)
                print(graph[nx][ny])


# 이 부분이 이해가 잘안된다.
# 왜 토마토가 있는 부분을 먼저 리스트에 넣고 코드를 진행을 하는걸까?
lst = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            lst.append((i, j))
print('토마토가 있는 위치 리스트에 추가')
print(lst)
bfs(lst)


def result():
    anwser = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return print(-1)
            anwser = max(anwser, graph[i][j])
    return print(anwser-1)


result()
