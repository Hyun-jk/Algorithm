#피보나치 수열

#탑다운(재귀함수 이용)
n = int(input())
def fibo(x):
    if x ==1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)
    
print(fibo(n))

#탑다운(재귀함수 이용, 메모이제이션 방식 사용)
d= [0] * 10
def fibo2(x):
    if x ==1 or x ==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]

print(fibo2(n))

#바텀업(반복문, 메모이제이션 방식 사용)
d2 = [0] * 100
d2[0] = 1
d2[1] = 1

for i in range(2,n):
    d2[i] = d2[i-1] + d2[i-2]
print(d2[n-1])
    



