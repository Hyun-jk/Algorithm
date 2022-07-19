#1로 만들기

n = int(input()) #정수 입력
#d의 값은 index값이 만들어지는 회수
#d[2] = 1이면 2를 만들 수 있는 경우의 수
d = [0] * (n+1)

#바텀업, 반복문 사용
for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i%2 ==0:
        d[i] = min(d[i],d[i//2]+1)
        print(d)
    if i%3 ==0:
        d[i] = min(d[i],d[i//3] +1)

print(d[n])    


