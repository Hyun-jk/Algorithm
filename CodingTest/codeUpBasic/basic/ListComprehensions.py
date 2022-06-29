#2차열 리스트 초기화
baduk = [[0]* 20 for _ in range(20)]

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    baduk[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(baduk[i][j], end=' ')
    print()