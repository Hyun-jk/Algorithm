# 1로 만들기
#바텀업 방식의 개념 다시 한번 확인하기

#탑 다운(재귀함수 사용)
def function(x):
    global count
    print(f'count = {count} x={x}')
    if x ==1:
        return count
    if x %5 != 0 and x%3 !=0:
        if (x-1) % 5 ==0 or (x-1) % 3 ==0:
            x-= 1
            count +=1
            return function(x)
    if x % 5 ==0:
        count +=1
        x = x//5
        return function(x)
    elif x % 3 ==0:
        count += 1
        x = x//3
        return function(x)
    elif x % 2 ==0:
        count +=1 
        x = x//2
        return function(x)
    else:
        x -= 1
        count +=1
        return function(x)

count =0
print(function(int(input())))

#다니아믹 프로그래밍(Dynamic Programming) 진행(보텀업)
#정수 X를 입력받기
x = int(input())
#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001
for i in range(2, x+1):
    #현재의 수에서 1을 빼는 경우
    #보텀업 방식은 아래에서 부터 구하기때문에 문제에서 요구한 -1을 하는 것이 아니라 +1로 코드를 짜준다
    d[i] = d[i-1] +1 
    
    #현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 ==0:
        d[i] = min(d[i],d[i//2]+1) 
    
    #현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 ==0:
        d[i] = min(d[i], d[i //3] +1)
    
    #현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 ==0:
        d[i] = min(d[i], d[i //5] +1)

print(d[x])











