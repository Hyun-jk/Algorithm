# 수 정렬하기3
# 이 문제는 sort()를 사용하면 메모리가 초과된다.
import sys
input = sys.stdin.readline

# 기본 라이브러리 메모리초과
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
for i in array:
    print(i)


# 계수 정렬 메모리초과
n = int(input().rstrip())
array = [0]*(10001)
for _ in range(n):
    array[int(input())] += 1

for i in range(len(array)):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
