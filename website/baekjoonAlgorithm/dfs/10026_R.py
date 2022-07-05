#적록색약
import sys
sys.setrecursionlimit(10000)

def dfs(x,y,type):
    done.append((x,y))

    for i in range(4):
        nx = x+ dx[i]
        ny = y +dy[i]

        if(0<=nx <N) and (0 <= ny <N) and ((nx,ny) not in done):
            if type ==0 and colors[nx][ny] == colors[x][y]:
                dfs(nx,ny,0)
            elif type ==1 and colors[nx][ny] == colors[x][y]:
                dfs(nx,ny,1)

N = int(input())
colors = [list(input()) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#정상인 경우
done = []
cnt_1 = 0

#dfs함수를 통해서 같은 색깔의 좌표를 done 리스트에 모두 담는다.
#done리스트에 안담긴 좌표는 색깔이 다른 좌표이다 
for i  in range(N):
    for j in range(N):
        if (i,j) not in done:
            dfs(i,j,0)
            cnt_1 += 1

#적록색맹인 경우
for i in range(N):
    for j in range(N):
        if colors[i][j] =='G':
            colors[i][j] =='R'

done = []
cnt_2 = 0
for i in range(N):
    for j in range(N):
        if (i,j) not in done:
            dfs(i,j,1)
            cnt_2 +=1 

print(cnt_1,cnt_2)
