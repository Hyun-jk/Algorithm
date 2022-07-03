#파스칼의 삼각형2  >>>다시 공부하고 하자
import sys
sys.setrecursionlimit(1000000) # 재귀함수 횟수 제한 라이브러리

r,c = map(int,input().split())
trangle = [[0] * 51 for i in range(51)]

def pascal(r,c):
    if r < 1 or c < 1:
        return 0
    return pascal(r-1,c) + pascal(r,c=1)

print(pascal(r,c))
