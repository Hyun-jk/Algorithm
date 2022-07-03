#배수
from collections import deque

def bfs(n,s):
    queue = deque([s])

    while queue:
        t = queue.popleft()
        print(f't  = {t}')

        #unsigned long long형의 범위에 없을 경우 0을 출력한다.
        if t >= 2**64:
            return 0
        elif t % n == 0:
            return t
        
        queue.append(t*10)
        queue.append(t*10 +1)
        print(f'queue = {queue}')

n = int(input())
print(bfs(n,1))

        
        
        