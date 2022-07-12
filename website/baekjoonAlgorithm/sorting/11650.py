# 좌표 정렬하기
n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key=lambda x: (x[0], x[1]))  # 이게 이해가 잘 안된다...

for i in range(len(array)):
    for j in array[i]:
        print(j, end=' ')
    print()
