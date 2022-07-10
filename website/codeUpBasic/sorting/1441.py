# 버블 정렬
# 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
# 선택 정렬과 기본 개념이 유사하다
# 시간초과
import sys
input = sys.stdin.readline

m = int(input())
num = []
for _ in range(m):
    num.append(int(input()))
"""
for i in range(m):
    for j in range(m):
        if j+1 < m:
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
"""
for i in range(0, m):
    for j in range(i+1, m):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

for i in num:
    print(i)
