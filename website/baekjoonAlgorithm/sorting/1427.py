# 소트인사이드
import sys
input = sys.stdin.readline

array = list(map(int, input().rstrip()))
array.sort(reverse=True)
for i in array:
    print(i, end='')
