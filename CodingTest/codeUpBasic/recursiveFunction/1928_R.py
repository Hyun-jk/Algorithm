#(재귀함수) 우박수
def func(n):
    print(n)
    if n ==1:
        return 1
    if n % 2 == 0:
        return func(n//2)
    else:
        return  func(3*n + 1)
n = int(input())
func(n)


