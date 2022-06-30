#삼각형 출력하기
def star(n):
    if n !=1:
        star(n-1)
    print('*' * n)

star(int(input()))