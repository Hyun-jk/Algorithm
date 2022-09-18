#이친구 (DP)

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

"""
2차원 리스트로 풀 필요 없었는데 그 전의 DP문제 때문에 너무
어렵게 푼 것 같다.

n = int(input())
dp = [[0] * 2 for _ in range(n+1)]
dp[1][1] = 1
dp[2][0] = 1

for i in range(3,n+1):
    for j in range(2):
        dp[i][j] = dp[i-1][j] + dp[i-2][j]

print(sum(dp[n]))        
"""

