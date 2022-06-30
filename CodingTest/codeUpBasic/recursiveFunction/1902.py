#역순으로 1까지 출력하기
def func(x):
    if x != 0:
        print(x) 
        func(x-1)

func(int(input()))