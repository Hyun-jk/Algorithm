#계단 오르기

n = int(input())

#계단의 점수 
s = [0 for i in range(301)]
#계단을 오를때마다 계단 점수의 합
dp = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0]+ s[2])

for i in range(3,n):
    dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] +s[i])

print(dp[n-1])