#두 수 사이의 홀수 출력하기
def func(x,y):
    if x <= y:
        if x %2 != 0:
            print(x, end=' ')
        func(x+1,y)

x, y = map(int,input().split())
func(x,y)