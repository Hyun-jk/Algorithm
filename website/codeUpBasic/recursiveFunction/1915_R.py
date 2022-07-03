#피보나치 수열
n = int(input())
def fib(n):
    if n<= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(n))

"""
반복문으로 피보나치 수열 구현
def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr
"""

