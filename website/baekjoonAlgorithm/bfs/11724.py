# 연결 요소의 개수
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# 첫째 줄에 연결 요소의 개수를 출력한다. >>이게 무슨 말일까?

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())  # m = 정점의 개수, n = 간선의 개수
graph = [[] for _ in range(m+1)]

# 연결된 노드 정보를 2차 리스트 graph에 넣는다.
for _ in range(n):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
