# 정렬을 빠르게
"""
풀이) 데이터 값의 범위가 있어서 계수정렬로 풀었다.
메모리초과 발생
(배열의 크기가 제한된 크기보다 크거나, 동적인 자료구조가 잘못된 반복문에 의해 많이 생성된 경우)\
-->아마 한 줄에 많은 수를 입력받게 되면서 메모리 초과가 나는 듯함
-->특정 바이트 수만큼 끊어서 입력받는 걸 반복하는 식으로 처리해야함(어떻게 하지?)

n = int(input())
array = list(map(int, input().split()))

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
"""
