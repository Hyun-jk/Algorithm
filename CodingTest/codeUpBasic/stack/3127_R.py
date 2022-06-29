#수식 계산1 >>>나머지 풀고 풀자
n = list(input().split())
sum = []

for i in range(len(n)):
    if n[i] == "*" and i-1 >=0 and i-2 >= 0:
        a = n[i-1] * n[i-2]
        sum.append(a)
    elif n[i] == '+' and i-1 >= 0 and i-2 >= 0:
            
