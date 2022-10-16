#이분 그래프
#이분 그래프는 그래프 형태의 자료구조인데 정점을 2그룹으로 나눌 수 있으되 같은 
#그룹의 정점끼리는 간선으로 이어지지 않은 경우를 의미한다

from collections import deque

def bfs(num):
    q = deque()
    q.append(num)
    visit[num] = 1
    while q:
        x = q.popleft()
        for i in board[x]:
            if visit[i] == 0:
                visit[i] = -visit[x]
                q.append(i)
            else:
                if visit[i] == visit[x]:
                    return False
    return True


num1 = int(input())
for i in range(num1):
    n,m = map(int, input().split())
    board = [[] for _ in range(n+1)]
    visit = [0] * (n + 1)
    flag = 1
    for _ in range(m):
        a,b = map(int,input().split())
        board[a].append(b)
        board[b].append(a)

    for i in range(1,n+1):
        if visit[i] == 0:
            if not bfs(i):
                flag = -1
                break
    print('YES' if flag == 1 else 'NO')