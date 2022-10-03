#소수 구하기
#시간 초과가 나서 에라토스테네스의 체를 이용하여
#소수를 구해야 시간 초과가 나지 않는다

n,m = map(int,input().split())
primes = [True] * (m+1)
primes[1] = False

for i in range(2,m+1):
    if primes[i]:
        for j in range(2*i,m+1,i):
            primes[j] = False
    
for k in range(n,m+1):
    if primes[k]:
        print(k)

