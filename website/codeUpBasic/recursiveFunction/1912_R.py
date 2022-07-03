#팩토리얼 계산
n = int(input())

def fucn(n):
    if n <= 1:
        return 1
    return n * fucn(n-1)    
print(fucn(n))