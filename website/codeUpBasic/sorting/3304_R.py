# 데이터 재정렬
"""
n = int(input())
array = list(map(int, input().split()))
result = sorted(array)
[2중 반복문 시간초과]
for i in array:
    for j in range(len(array)):
        if i == result[j]:
            print(j, end=' ')

result = sorted(array)
answer = [[] for _ in range(len(result))]

[python index()함수는 시간복잡도가 O(N)이므로 시간초과가 발생한다.]
for i in range(len(result)):
    answer[i].append(array[i])
    answer[i].append(result.index(array[i]))

for i in range(len(answer)):
    print(answer[i][1], end=' ')

"""

# 이진 탐색을 이용해서 index를 찾아야한다.
n = int(input())
data = list(map(int, input().split()))


# binary search 함수
def binary_search(data, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(data, start, mid-1, target)
    else:
        return binary_search(data, mid+1, end, target)


def resort(data):
    index_memo = ""
    sorted_data = sorted(data)
    for i in data:
        index_memo += str(binary_search(sorted_data, 0, len(data)-1, i)) + " "

    return index_memo


print(resort(data))
