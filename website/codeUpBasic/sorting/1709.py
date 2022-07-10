# 내림차순 정렬
n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)

for i in array:
    print(i, end=' ')
