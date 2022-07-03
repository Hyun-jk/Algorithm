# 1부터 n까지 합 구하기
import sys
sys.setrecursionlimit(1000000) # 재귀함수 횟수 제한 라이브러리
n = int(input())

sum =0
def func(n):
    if n > 0:
        global sum
        sum+=n
        func(n-1)
    return sum

print(func(n))
