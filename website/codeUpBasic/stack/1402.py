#거꾸로 출력하기3
n = int(input())
m = list(map(int,input().split()))

for _ in range(len(m)):
    a = m.pop()
    print(a, end=' ')