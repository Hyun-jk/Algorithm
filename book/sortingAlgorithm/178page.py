#위에서 아래로
n = int(input())
graph = []
for _ in range(n):
    graph.append(int(input()))

#파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행
graph.sort(reverse = True)
for i in graph:
    print(i, end=' ')