#DFS/BFS 알고리즘 같은데
baduk = [[0]*20 for _ in range(20)]


for i in range(20):
    baduk[i] = list(map(int,input().split()))

for j in range(20):
    for k in range(20):
        print(baduk[j][k],end=' ')
    print()