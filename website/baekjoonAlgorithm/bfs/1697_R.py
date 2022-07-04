# 숨바꼭질

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())


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
# 시작값이 5라고 생각을 하면 , i = 4,6,10이 된다. 이 때
# 1차원 리스트 visited을 이용해서 인덱스 4,6,10을 +1을 해주면 이것을 시간이라고 생각을 하면 된다.
#


n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))
