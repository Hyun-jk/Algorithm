# 저울
# intertools로 각각 순열을 조합해서, 합을 리스트에 넣어서 풀이를 하려고 하였는데
# 시간제한이 1초라서 다른 방법을 찾아야했다.

import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))

# 추의 무게 오름차순 정렬
w.sort()
# target의 초기값(양의 정수의 최소값은 1이기 때문에)
target = 1
for i in w:
    if target < i:
        break
    target += i
    print(target, i)

print(target)
