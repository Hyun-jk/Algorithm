#동물원
n = int(input())
dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n+1):
    dp[i] = dp[i-1] + 2*i

print(dp[i])
