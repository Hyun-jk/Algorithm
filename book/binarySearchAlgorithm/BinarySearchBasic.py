# 이진 탐색
"""
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
- 탐색은 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점이다
- 찾으려는 데이터와 중간점(middle) 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를
  찾는게 이진 탐색의 과정이다.
- 이진 탐색을 구현하는 방법은 재귀 함수, 단순하게 반복문을 이용하는 방법 총 2가지이다.
"""
# 이진 탐색의 시간 복잡도
"""
한 번 확일할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다
"""

# 재귀함수로 구현한 간단한 이진 탐색 소스코드


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


# 반복문으로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1


# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
