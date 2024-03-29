#최단 경로 알고리즘
"""
- 말 그대로 가장 짧은 경로를 찾는 알고리즘이다
- 최단 경로 알고리즘 유형에는 다양한 종류가 있는데
- 상황에 맞는 효율적이 알고리즘이 있기 때문에 상황에 맞는 알고리즘을 숙지하고 있어야 한다.
ex) 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 경우
      모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 등
- 최단 경로 문제는 보통 그래프를 이용해 표현, 각 지점은 그래프에서 노드로 표현되고
   지점간 연결된 도로는 그래프에서 간선으로 표현된다.
- 보통 다익스트라 최단경로 알고리즘, 플로이드 워셜, 벨만 포드 알고리즘을 이용한다      
"""
    
#다익스트라 최단 경로 알고리즘
"""
-그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는
  각각의 최단 경로를 구해주는 알고리즘
- '음의 간선'이 없을 때 정상적으로 동작한다
- 음의 간선이란 0보다 작은 값을 가지는 간선을 의미, 현실 세계의 길(간선)은
   음의 간선으로 표현되지 않으므로 실제 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 한다.
- 기본적으로 그리디 알고리즘으로 분류(매번 가장 비용이 적은 노드를 선택해 임의의 과정을 반복하기 때문에)

알고리즘 원리)
1.출발 노드를 설정
2.최단 거리 테이블을 초기화한다
3.방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
4.해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다
5. 위 과정에서 3,4번을 반복

특징)
1.각 노드에 대한 현재까지의 최단 거리 정보를 항상 1차원 리스트에 저장하며 리스트를 계속 갱신해야함
2. 매번 현재 처리하고 있는 노드를 기준으로 주변 간선을 확인
3. 나중에 현재 처리하고 있는 노드와 인접한 노드로 도달하는 더 짧은 경로를 찾으면, 더 짧은 경로로 갱신
4. 방문하지 않은 노드 중에서 현재 최단 거리가 가장 짧은 노드를 확인해 최단 거리 테이블을 갱신한다는 
    점이 그리디 알고리즘으로 볼 수 있다.

시간복잡도)
- 다익스트라 알고리즘은 O(V^2)의 시간 복잡도를 가진다.
   여기서 V는 노드의 개수이다.
-처음에 각 노드에 대한 최단 거리를 담는 1차원 리스트를 선언
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해
  매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)한다.
"""

#간단한 다익스트라 알고리즘 소스코드
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수 입력받기
n,m = map(int,input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n -1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    #도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])




 








