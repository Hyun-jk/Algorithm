# 가장 긴 감소하는 부분 수열
# 6
# 10 30 10 20 20 10
result = 3

n = int(input())
array = list(map(int, input().split()))
array.reverse()
dp = [1] * n

for cur in range(1, n):  # 현재 비교하려고 하는 수의 인덱스
    for prev in range(cur):  # 이전의 인덱스
        if array[cur] > array[prev]:
            dp[cur] = max(dp[cur], dp[prev]+1)

print(max(dp))
