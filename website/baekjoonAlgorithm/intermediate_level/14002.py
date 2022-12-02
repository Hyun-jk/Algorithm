# 가장 긴 증가하는 부분 수열4
n = int(input())  # 1 <= n <= 10^3)
array = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)

answer = []
target = max(dp)
for index in range(n-1, -1, -1):
    if dp[index] == target:
        answer.append(array[index])
        target -= 1

answer.reverse()
print(max(dp))
for j in answer:
    print(j, end=" ")

"""
6
10 20 10 30 20 50
4
10 20 30 50
"""
