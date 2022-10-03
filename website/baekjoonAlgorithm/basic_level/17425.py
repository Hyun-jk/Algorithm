#약수의 합
#약수의 합2와 동일한 문제이나, 시간초과를 유의해서 문제를 풀어야한다.
#시간초과를 관리하기 위해서 DP로 문제를 해결하였으며,
#약수는 그 약수의 배수에 다 포함되어 있다는 것을 파악하여, DP테이블에 그 약수의 배수에 해당하는 
#DP를 파악하여 다 더해주었다.
#EX) 2는 2의 배수인 수의 약수이다. Ex)4,6,8,10
max = 1000000
dp = [1] * (max+1)
sum_list = [0] * (max+1)
sum_list[1] = 1

for i in range(2,max+1):
    j = 1
    while i*j <= max:
        dp[i*j] += i
        j +=1

for i in range(2,max+1):
    sum_list[i] = sum_list[i-1] + dp[i]

answer = []
t= int(input())
for i in range(t):
    n = int(input())
    answer.append(sum_list[n])

print("\n".join(map(str,answer)))