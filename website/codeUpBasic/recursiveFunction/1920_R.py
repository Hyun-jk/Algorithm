#재귀함수 2진수 변환

def d(n):
    if n//2 == 0:
        return str(n%2)
    return d(n//2) +str(n%2)

n = int(input())
print(d(n))