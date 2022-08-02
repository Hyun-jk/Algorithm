# 평범한 배낭

n, k = map(int, input().split())  # n는 물품의 수, k는 버틸 수 있는 무게
thing = [[0, 0]]
d = [[0] * (k+1) for _ in range(n+1)]  # 의문1 왜 2차원 리스트로 구현을 했지?
print(d)

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):  # k는 무게
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]  # 의문 2
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)  # 의문 3

print(d[n][k])
