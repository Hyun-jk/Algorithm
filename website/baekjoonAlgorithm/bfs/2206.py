#벽 부수고 이동하기
from collections import deque

n,m = map(int(input().split()))
graph = [list(map(int,input())) for _ in range(n)]

#상하좌우
dx = [-1,1,0,0]
dy  = [0,0,-1,1]

        
