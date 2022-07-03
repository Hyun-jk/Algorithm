#재귀함수 우박수(reverse)
def func2(n):
    if n ==1:
        return print(n)
    elif n%2 ==0:
        func2(n//2)
    else:
        func2(3*n +1)
    return print(n)
func2(int(input()))
