# 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while (start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        if x > mid:
            total += x-mid
        # 자르는 도중 목표한 나무의 양이 넘어가면 멈춘다
        # 이 코드를 넣지 않으면 시간초과가 난다
        if total > m:
            break
    # 나무의 양이 부족한 경우(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 나무를 너무 많이 자른 경우(오른쪽 부분 탐색)
    else:
        start = mid + 1  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        result = mid

print(result)
