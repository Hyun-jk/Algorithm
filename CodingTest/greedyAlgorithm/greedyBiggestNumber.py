#큰 수의 법칙
n,m,k  = map(int, input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:  #for 반복문 탈출
           break
        result += first
        m -= 1
    if m == 0:  #while 반복문 탈출
        break
    result += second
    m -= 1
print(result)

#M(더하는 숫자의 갯수 )가 100억 이상일 경우 시간초과 판정을 받는다


