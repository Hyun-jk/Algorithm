#수 묶기
#생각한 부분
#리스트를 짝수, 홀수로 나눠서 계산을 해야하는 것을 인지
#range의 증가율을 2로 해야한다는 것을 인지
#생각하지 못한 부분
#음수 * 음수 = 양수, 음수 * 0 > 음수 + 양수 인 것을 생각하지 못하여서
#음수,양수를 나눠서 리스트에 담을 생각을 하지 못하였다.

N = int(input())
positive = []  #양수를 저장할 리스트
negative =[]  #음수를 저장할 리스트
max_sum = 0  #최대값을 저장할 변수

for _ in range(N):
    n = int(input())

    if n > 1 : #입력받은 값이 양수인 경우
        positive.append(n)
    elif n == 1 : #1은 어차피 나중에 더해야 함으로 계산을 편하게 하기 위해서 미리 더해준다.
        max_sum += 1 
    else:
        negative.append(n)

positive.sort(reverse = True) #양수는 내림차순
negative.sort() #음수는 오름차순

#양수 리스트 계산
if len(positive) %2 ==0: #양수가 짝수개 일 경우 두개씩 곱해준다.
    for i in range(0, len(positive), 2):
        max_sum += positive[i] * positive[i+1]
    else: #홀수개 일 경우
        max_sum += positive[i] * positive[i+1]
    max_sum += positive[len(positive)-1] #마지막 수는 더해준다.

#음수 리스트 계산
if len(negative) % 2 ==0:  #음수가 짝수개 일 경우 두개씩 곱해준다
    for i in range(0,len(negative),2):
        max_sum += negative[i] * negative[i+1]
else:
    for i in range(0,len(negative)-1,2 ):
        max_sum += negative[i] * negative[i+1]
    max_sum += negative[len(negative)-1] #마지막수는 더해준다.

print(max_sum)




        


