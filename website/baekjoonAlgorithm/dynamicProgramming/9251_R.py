#LCS
m = " " + input()
n = " " + input()

#문자열 m,n을 dp 2차원 리스트에 넣어줌
dp = [[0] * len(n) for i in range(len(m))]

for i in range(1,len(m)):
    for j in range(1,len(n)):
        if m[i] == n[j]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])