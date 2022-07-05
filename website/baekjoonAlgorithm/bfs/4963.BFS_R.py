#섬의 개수
from collections import deque
import sys
read = sys.stdin.readline

def bfs(x,y):
    dx = [1,-1,0,0,1,-1,1,-1]
    dy = [0,0,-1,1,-1,1,1,-1]
    graph[x][y] =0
    queue = deque()
    queue.append([x,y])

    while queue:
        a,b = queue.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < h and 0 <= ny < w and graph[nx][ny] ==1:
                graph[nx][ny] =0
                queue.append([nx,ny])

while True:
  w, h = map(int, read().split())
  if w == 0 and h == 0:
    break
  graph = []
  count = 0
  for _ in range(h):
    graph.append(list(map(int, read().split())))
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        bfs(i, j)
        count += 1
  print(count)