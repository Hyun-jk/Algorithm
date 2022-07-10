# 데이터 정렬(large)
# 파이썬 라이브러리를 이용

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

result = sorted(array)
for i in result:
    print(i)
