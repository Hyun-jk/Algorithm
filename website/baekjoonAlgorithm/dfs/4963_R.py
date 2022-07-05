#섬의 개수
#일반적인 dfs에서 대각선만 구할 수 있으면 문제 없이 풀 수 있다.
import sys
input = sys.stdin.readline

def dfs(x,y):
    dx = [1,1,-1,-1,1,-1,0,0]
    dy = [0,1,0,1,-1,-1,1,-1]
    
    graph[x][y] =0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < h and 0<= ny < w and graph[nx][ny] ==1:
            dfs(nx,ny)

while True:
    w,h = map(int,input().split())
    if w == 0 and h ==0:
        break
    graph = []
    count =0

    for _ in range(h):
        graph.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] ==1:
                dfs(i,j)
                count +=1
    print(count)

