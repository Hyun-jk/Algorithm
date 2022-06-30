#피보나치 수열(Large)

"""
재귀로 피보나치 수열을 풀 경우 입력 받은 값아 커지면 커질수록
시간이 너무 오래 걸린다.
그래서 사용하는 것이 메모이제이션(처음 계산한건 기록하고, 계산하기 전에 계산해둔 것이 있으면 사용한다.)

N = int(input())
def fib(n):
    if n <=1 :
        return n
    return fib(n-1)+fib(n-2)

print(fib(N) % 10009)
"""
fibo = [0]*201 # 인덱스 번호가 피보나치의 자릿수 [0 1 1 2 3 5 ...]
fibo[1] = 1 # 초기화 [0,1,0...]
def fast_f(n):
    if n <= 1:
        return n
    if fibo[n] == 0:
        fibo[n] = fast_f(n - 1)+ fast_f(n - 2)
    return fibo[n]
 
def fibonacci(n):
    if n == 1:
        return n
    return fast_f(n)
 
n = int(input()) # 200이하 자연수
print(fibonacci(n)%10009)
