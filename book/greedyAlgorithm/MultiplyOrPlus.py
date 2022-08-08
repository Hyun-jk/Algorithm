# 곱하기 혹은 더하기

data = input()
result = int(data[0])
print(result)

# 나랑 차이점 --> 굳이 리스트를 만들지 않고, 입력 받은 값을 바로 result 값에다가 넣어주었고
# 그 다음 인덱스를 비교해서 코드를 진행하였다.
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
