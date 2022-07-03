#럭키스트레이트
N = input()
sum =0
sum1 = 0

#ex)len(N) ==6
for i in range(len(N)):
   #i =0,1,2 
    if i < len(N)//2:
        sum += int(N[i])
    else:
        sum1 += int(N[i])
if sum == sum1:
    print('LUCKY')
else:
    print('READY')

"""
n = input()
length = len(n)
summary = 0

#왼쪽 부분의 자릿수 합 더하기
for i in range(length //2)
    summary += int(n[i])

#오른쪽 부분의 자릿수 합 빼기
for i in range(length //2 , length):
    summary -= int(n[i])

#왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary ==0:
    print('LUCKY')
else:
    print('READY')
"""



