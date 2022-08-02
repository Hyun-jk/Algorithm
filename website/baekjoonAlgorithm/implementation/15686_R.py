# 치킨 배달

# 해결방법 생각
"""
1.도시의 치킨 거리의 최솟값을 구하라
>>>M개의 치킨집을 제외하고 나머지 폐쇄를 할 예정
>>>M개의 치킨집을 도시의 치킨 거리 최소 값에다가 위치를 시키고(이거를 모든 경우의 수를 생각해야한다.)
>>>최소값을 구하자
# k의 개수를 확인하고, 이거를 경우에 수에 맞춰서 계산을 어떻게 해야하는가가 중요한 포인트
>>itertools로 이용해서 경의 수를 계산
"""

import sys
from itertools import combinations

# N*N의 크기의 도시, M개의 치킨집만 유지
n, m = map(int, input().split())
city_map = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []  # 집의 좌표
chick = []  # 치킨집의 좌표

# 집의 좌표, 치킨집의 좌표를 house,chick list에 담기
for i in range(n):
    for j in range(n):
        if city_map[i][j] == 1:
            house.append([i, j])
        elif city_map[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):  # m개의 치킨집 선택
    temp = 0
    for h in house:  # 집의 좌표
        print(chi, h)
        chi_len = 999  # 각 집마다 치킨 거리
        for j in range(m):
            # 치킨 집과의 최소 거리가 그 집의 치킨 거리이다.
            chi_len = min(chi_len, abs(
                h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))

        temp += chi_len
    result = min(result, temp)

print(result)
