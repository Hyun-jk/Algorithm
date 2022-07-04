# 숨바꼭질
# 5, 17 5, 10,9,18,17
# 어떤 식으로 풀어야할까 보통 bfs문제는 2차원 리스트로 위치값을 조정해서 풀었는데
# 이거는 2차원식이 아닌것 같고 그러면 1차원 리스트로 풀면 되려나?
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
move = [1, -1, 2]
result = []


def bfs(v):
    q = deque([v])  # 큐 구현을 위해 deque 사용
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))


def bfs(n, k):
    queue = deque()
    queue.append(n)
    count = 0
    while queue:
        x = queue.popleft()
        print(f'x={x}')
        for i in range(3):
            nx = x + move[i]
            if i == 2:
                nx = x * move[i]
            print(f'i = {i}일때 nx = {nx}')
            if nx == k:
                return count
            if 0 < nx:
                queue.append(nx)


print(bfs(n, k))
