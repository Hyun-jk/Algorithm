#ABCDE(그래프)
#다음 친구 관계를 가진 사람ABCDE이 존재하는 확인
#즉 연결된 노드의 최대 개수가 5개이다. 이게 아니면 print(0) 

#dfs 이용
def dfs(idx,depth):
    global result
    visited[idx] = True
    #친구 관계가 4번 이상 연결되어 있다면
    if depth == 4:
        result = True
        return
    #친구 관계가 존재하는지 확인
    for i in relationship[idx]:
        #아직 방문하지 않았다면
        if not visited[i]:
            visited[i] = True
            #재귀적으로 수행
            dfs(i, depth + 1)
            #방문 표시 해제
            visited[i] = False

n,m  = map(int,input().split())
relationship = [[]  for _ in range(n)]

#입력값 받기
for _ in range(m):
    x,y = map(int,input().split())
    relationship[x].append(y)
    relationship[y].append(x)

#방문 표시
visited =[False] *  2001

#정답 변수 생성
result = False

#0번부터 N-1번까지 확인하며
for i in range(n):
    #친구 관계 탐색
    dfs(i,0)
    visited[i] = False
    #친구 관계가 존재한다면
    if result:
        #탈출
        break

#정답이 있다면 1출력
if result:
    print(1)
else:
    print(0)
