# 1부터 n까지 합 구하기
n = int(input())

def func(n):
    global sum
    sum =0
    sum+= n
    if n != 1:
        func(n-1)
    return sum

func(n)
