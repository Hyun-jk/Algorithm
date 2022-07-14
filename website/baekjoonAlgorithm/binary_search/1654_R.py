# 랜선 자르기
# 다시 고민해보자!
"""

k, n = map(int, input().split())
array = []
for _ in range(k):
    array.append(int(input()))

start = 0
end = max(array)
result = 0
while (start <= end):
    count = 0
    mid = (start + end) // 2
    print(f"mid={mid} count={count}")
    for x in array:
        if min(array) >= mid:
            count += x // mid
            print(f"x = {x} count = {count}")
        else:
            break
    print(f"count={count}")
    # 랜선을 덜 자른 경우
    if count < n:
        end = mid-1
    # 랜선을 더 많이 자른 경우(더 크게 잘라야함)
    elif count == n:
        result = mid
        break
    else:
        start = mid + 1
        result = mid

print(result)
"""

import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan)  # 이분탐색 처음과 끝위치

while start <= end:  # 적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2  # 중간 위치
    lines = 0  # 랜선 수
    for i in lan:
        lines += i // mid  # 분할 된 랜선 수

    if lines >= N:  # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)
