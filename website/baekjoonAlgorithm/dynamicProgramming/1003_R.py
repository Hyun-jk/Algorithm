#피보나치 함수
#0,1을 카운트 하는 식으로 코드를 진행했더니 시간초과가 나온다
#이 문제는 0,1을 카운트 하는 것이 아니라 
# 0,1이 피보나치 수열의 형태로 사용이 된다.

# 0 이 출력된 횟수
#1, 0 , 1 , 1 ,2 ,3 5 ,8

#1이 출력된 횟수
#0, 1, 1, 2, 3, 5, 8, 13

zero = [1,0,1]
one = [0,1,1]

def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))

a = int(input())
for i in range(a):
    k = int(input())
    cal(k)