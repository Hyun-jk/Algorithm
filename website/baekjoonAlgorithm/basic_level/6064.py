#카잉 달력
#단순히 완전탐색으로 풀게 되면 시간 초과가 난다 O(MN)
import sys
t = int(input())
m,n,x,y = map(int,input().split())
count = 0
a = 0
b = 0
while True:
    if a == x and b == y:
        print(count)
        break
    if a == n and b == m:
        print(-1)
        break
    if a < m:
        a +=1
    else:
        a = 1
    if b < n:
        b += 1
    else:
        b = 1
    
    print(a,b)
    count+=1
    print(count)
    
def calculate(m, n, x, y):
    k = x #k를 x로 초기화
    while k <= m * n: #k의 범위는 m*n을 넘을 수 없기에
        if (k - x) % m == 0 and (k - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
            return k
        k += m #k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
    return -1


t = int(input())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    print(calculate(m, n, x, y))
    