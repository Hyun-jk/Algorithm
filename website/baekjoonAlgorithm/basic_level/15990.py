#1,2,3 더하기 5
import sys
input = sys.stdin.readline

dp = [[0 for _ in range(3)] for _ in range(100001)]

# N이 1일때 2일때 3일때 각각 1,2,3으로 끝나는 상황의 개수 미리 초기화
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # 만약 i가 6이라면
    
    # 5에서 2와 3으로 끝난 횟수에 1을 더하면 6이므로 그 두개의 횟수를 더해주어 대입.
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    # 4에서 1과 3으로 끝난거에 2를 더하면 6이므로 그 두개의 횟수를 더해주어 대입.
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    # 3에서 1과 2로 끝난거에 3을 더하면 6이므로 그 두개의 횟수에 더해주어 대입.
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

T = int(input())
for i in range(T):
    n = int(input())
    print(sum(dp[n]) % 1000000009)