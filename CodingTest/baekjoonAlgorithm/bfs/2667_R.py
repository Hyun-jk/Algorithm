#단지번호 붙이기
import sys
from collections import deque

#sys 라이브러리를 사용할 때는 한 줄 입력을 받고 rstrip()함수를 꼭 호출해야한다.
#readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력이 되는데, 이 공백 문자를 제거하려면
#restrip()함수를 사용해야한다.
input = sys.stdin.readline
N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

#한 점을 기준으로 (상 하 좌 우) 으로 한칸 씩 이동할 좌표 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,x,y):
    queue = deque()  # 큐 선언
    queue.append((x,y)) # x,y가 제일 먼저 시작하는 시작점이여서 큐에 추가한다
    graph[x][y] = 0 #첫번째 집 x,y를 방문 처리해준다
    count = 1  #첫번째 집 x,y를 방문했기 때문에 count값을 1로 시작한다

    while queue:
        x, y = queue.popleft()
        
        for i in range(4): #각 좌표마다 상,하,좌,우로 이동
            nx = x + dx[i]
            ny = y + dy[i]

            #좌표를 이동했는데 그래프 범위를 벗어 나는 경우
            if nx <0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1: #만약 1이라면(집을 방문을 안했다면)
                graph[nx][ny] = 0 #방문했던 곳은 0으로 만들어 버린다.
                queue.append((nx,ny)) # 새로운 x,y 좌표를 큐에 추가
                count +=1 #count값 증가
    return count
        
#그래프가 원소가 1일때 bfs로 집을 방문한다
for i in range(N):
    for j in range(N):
        if graph[i][j] ==1:
            count = bfs(graph,i,j)
            result.append(count)

result.sort() #오름차순으로 정렬

print(len(result)) #총 단지수 출력
for k in result: #각 단지마다 집의 수 출력
        print(k)




