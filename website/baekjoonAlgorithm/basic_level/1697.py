#숨바꼭질(BFS)
from collections import deque
"""
q에 (이동할수 있는 좌표, 이동한 횟수)를 넣고
bfs(x+1,횟수),bfs(x-1,횟수),bfs(2*x,횟수)를 각각 실행을 시키는 식으로
코드를 짰는데, 메모리 초과가 나왔다.
"""
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1,x+1,x*2):
             if 0<= nx <= Max and not dist[nx]: #리스트의 값이 0이면 False를 반환
                 dist[nx] = dist[x] +1
                 q.append(nx)

n ,k = map(int,input().split())
Max = 10 ** 5 
dist = [0] *(Max+1) #반복되는 작업을 최소화하기 위해(메모리)
bfs()





