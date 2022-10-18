import sys
sys.setrecursionlimit(10000)

def dfs(now,group):
    visit[now] = group
    for i in arr[now]:
        #안 가본 곳
        if visit[i] == 0:
            if not dfs(i,-group):
                return False
        #가봤는데 색깔이 같으면
        elif visit[i] == visit[now]:
            return False
    return True

num = int(input())
for _ in range(num):
    n,m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    ans = True
    for i in range(1,n+1):
        if visit[i] == 0:
            ans = dfs(i,1)
            if not ans:
                break
    print("YES" if ans else "NO")