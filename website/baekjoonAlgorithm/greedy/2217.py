#로프
"""
잘한점)
로프의 최소 무게 * 갯수가 최대 중량이라는 개념은 이해하고 문제 풀이를 시작하였다.
유의사항)
최소 무게를 먼저 이용하여 최대 중량을 구하는 방향으로 문제 풀이를 진행하긴 하였지만,
먼저 최대 중량을 구하고 나머지를 비교를 하였기 때문에 코드가 복잡해졌다.
다만 최대 중량을 구하면 break를 하여서 진행시간은 단축이 되었다
반면에 최소값을 구하고 반대로 진행을 하게 되면 코드는 단축되는 대신에
전부 다 비교를 하여야 하기 때문에 시간이 늘어났다.
"""

n = int(input())
rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort()
cnt = rope[0] * n

for i in range(1,n):
    if rope[i] * (n-i) > cnt:
        cnt = rope[i] * (n-i)
print(cnt)

"""
n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
m.sort(reverse=True)
result = []

for j in range(n):
    result.append(m[j]*(j+1))

print(max(result))

"""