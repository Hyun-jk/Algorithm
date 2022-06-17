#곱하기 혹은 더하기
"""
[내가 한 것]
놓친 부분 
---> 0은 곱하지 말고 더해야 최대 값이 나오는 것은 확인 했으나
        1은 생각하지 못하였다. 0과 마찬가지로 1도 더해야만 최대 값이 나온다.

s = input()
list = []
for i in range(len(s)):
    list.append(int(s[i]))
print(list)
result = 0
for num in list:
    if num ==0:
        result+= num
    elif result ==0:
        result += num
    else:
        result *= num
print(result)
"""

data = input()
result = int(data[0])
print(result)

#나랑 차이점 --> 굳이 리스트를 만들지 않고, 입력 받은 값을 바로 result 값에다가 넣어주었고
#그 다음 인덱스를 비교해서 코드를 진행하였다.
for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
