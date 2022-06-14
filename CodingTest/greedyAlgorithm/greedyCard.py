#숫자 카드 게임
n,m = map(int,input().split())

#min()을 이용해서 구하는 방법
result = 0
for i in range(m):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)
print(result)

#2중 반복문 구조를 이용해서 구하는 방법
for i in range(n):
    data = list(map(int,input().split()))
    min_value = 10001 #각 숫자는 10000이하의 자연수이기 때문에
    for a in data:
        min_value = min(min_value,a)
        result = max(result,min_value)
print(result)
