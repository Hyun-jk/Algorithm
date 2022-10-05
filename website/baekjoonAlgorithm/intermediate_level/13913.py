#숨바꼭질4
from collections import deque

n,k = map(int,input().split())
max = 100001
graph = [0] * max
path = [0] * max

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(graph[x])
            ans = []
            while x != n:
                ans.append(x)
                x = path[x]
            ans.append(n)
            ans.reverse()
            print(' '.join(map(str,ans)))
            return
        for nx in (x-1,x+1,2*x):
            if 0<= nx < max and not graph[nx]:
                graph[nx] = graph[x] + 1
                q.append(nx)
                path[nx] = x

bfs()

