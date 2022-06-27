#설탕배달
# 3kg / 5kg >> 봉지 최솟값 구하기
#정확하게 못나누면 -1 출력

n = int(input())
count = 0

while n >= 0:
    if n % 5 ==0:
        count += n //5
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
     

