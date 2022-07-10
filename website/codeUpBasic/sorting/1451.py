# 데이터 정렬(small)
# 파이썬 정렬 라이브러리를 이용
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)
