#기억력 테스트7

# 1<=n <= 1000000, 1<= m <= 100000
n,m = map(int,input().split())  #n개의 숫자, m개의 질문
array = list(map(int,input().split()))
d = [0] * (n+1)
questions = []
for _ in range(m):
    questions.append(list(map(int,input().split())))

d[0] = 0
d[1] = array[0]

for i in range(2,len(array)+1):
    d[i] = d[i-1] + array[i-1]

for i in questions:
    start, end = i[0],i[1]
    if start != end:
        print(d[end] - d[start -1])
    else:
        print(array[end-1])