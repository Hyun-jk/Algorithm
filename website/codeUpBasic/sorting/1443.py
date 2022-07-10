# 삽입 정렬
n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            print(f'j={j}, j-1 ={j-1} array={array}')
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:
            break
for i in array:
    print(i)
