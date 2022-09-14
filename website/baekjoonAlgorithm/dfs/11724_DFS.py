import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

#간선의 모든 정보를 graph에 입력
for _ in range(m): 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
#반복문을 돌려주고, False인 부분을 찾는다.
#노드의 그룹을 찾기 위해서
#dfs함수를 돌려주고 false인 부분은 다른 노드와 연결이 되어있지 않는다는 소리임으로, count +=1을 해준다.
for i in range(1, n+1): 
    if visited[i] == False:
        count+=1
        dfs(i)

print(count)

