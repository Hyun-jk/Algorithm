# 숫자 카드
# 계속 오류난 이유 >>> 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있다!!!
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
card = list(map(int, input().split()))

for i in card:
    result = binary_search(array, i, 0, n-1)
    if result == None:
        print(0, end=" ")
    else:
        print(1, end=" ")
