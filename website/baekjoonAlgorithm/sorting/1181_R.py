# 수 정렬하기
# 길이가 짧은 것부터, 길이가 같으면 사전 순으로
"""
나는 입력 받을 때 중복 체크를 하였는데, set을 통해서 중복체크를 할 수 있다.
for _ in range(n):
    name = input()
    if name not in array:
        array.append(name)
#sort(key=len)

array.sort(key=lambda x: len(x)) #길이 체크만 하였다

String 함수)
strip[chars] : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거
rstrip[chars] : 인자로 전달된 문자를 String의 오른쪽에서 제거
lstript[chars] : 인자로 전달된 문자를 String의 왼쪽에서 제거
-인자를 전달하지 않을 수도 있으며, 인자를 전달하지 않으면 String에서 공백을 제거

"""

import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    array.append(input().strip())
array = list(set(array))  # set을 통해서 중복제거

array.sort(key=lambda x: (len(x), x))  # 길이,알파벳 순서로 정렬
result = "\n".join(array)
print(result)
