#연구소
'''
해결순서)
1. 연구소에서 3개의 벽을 선택하나
2. 벽이 선택된 연구소에서 바이러스를 퍼트린다
3. 바이러스가 퍼지지 않은 안전지역의 갯수를 구한다.
'''

#copy.copy()와 copy.deepcopy()의 차이점
#copy는 object까지만 가능, deepcopy는 element까지 복사 가능

from collections import deque
import copy
import sys
from unittest import result
input = sys.stdin.readline

n,m = map(int,input().split())
lab_map = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0


def bfs():
    queue = deque()
    test_map = copy.deepcopy(lab_map)
    
    #모든 바이러스의 위치를 queue에 대입
    for i in range(n):
        for k in range(m):
            if test_map[i][k] ==2:
                queue.append((i,k))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<= nx < n) and (0 <= ny < m):
                #바이러스 퍼트리기
                if test_map[nx][ny] ==0:
                    test_map[nx][ny] =2
                    queue.append((nx,ny))

    global result
    count = 0
    #바이러스를 퍼트리고, 나머지 안전구역 체크
    for i in range(n):
        for k in range(m):
            if test_map[i][k] ==0:
                count +=1

    result = max(result, count)            


def make_wall(count):
    #벽을 다 세웠으면 바이러스 퍼트리기
    if count ==3:
        bfs()
        return
    #모든 경우의 수를 생각해서, 벽을 세워보기
    for i in range(n):
        for k in range(m):
            if lab_map[i][k] ==0:
                lab_map[i][k] =1
                make_wall(count+1)
                #재귀호출이 끝나면, 다시 0 빈칸으로 만들어줘야 다음 경우의 수가 진행됨
                lab_map[i][k] = 0 

make_wall(0)
print(result)