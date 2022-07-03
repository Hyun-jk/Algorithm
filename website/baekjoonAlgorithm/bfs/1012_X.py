#유기농 배추 >>왜 안되는지 이해가 안된다.
# 입력 받은 값이랑  x,y를 바꿔서 체크를 해야하는데 이 부분이 헷갈린다.
import sys
from collections import deque

def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        now = q.popleft()
        for L in range(4):
            hh = now[0] + dh[L]
            ww = now[1] + dw[L]
            if 0 <= ww < w and 0 <= hh <h and graph[hh][ww] ==1:
                graph[hh][ww] =0
                q.append((hh,ww))

if __name__ == "__main__":
    dw = [0,1,0,-1] # 북, 동, 남, 서
    dh = [-1,0,1,0]
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        w, h, k = map(int,read().split())
        graph = [[0]*w for _ in range(h)]
        result = 0
        for _ in range(k): # 배추 위치 입력
            x,y = map(int,read().split())
            graph[y][x] = 1
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    bfs(i,j)
                    result += 1 # 영역 수
        print(result)