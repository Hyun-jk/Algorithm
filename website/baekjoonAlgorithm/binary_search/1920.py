# 수 찾기
n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))
array.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


for i in data:
    result = binary_search(array, i, 0, n-1)
    if result == None:
        print(0)
    else:
        print(1)
