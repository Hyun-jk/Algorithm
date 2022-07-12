# 나이순 정렬

import sys
import collections
input = sys.stdin.readline

n = int(input())
Member = collections.namedtuple('Member', ['date', 'age', 'name'])
Members = list()

for i in range(n):
    m, c = input().split()
    # 그냥 속성 값만 써줘도 되고, 속성명을 지정한 후에 지정해도 상관없다.
    Members.append(Member(i, int(m), c))


Members.sort(key=lambda x: (x.age, x.date))  # 나이와 가입일로 정렬

for i in range(n):
    print(Members[i].age, Members[i].name)

"""
# 다른 풀이)
n = int(input())
array = []

for _ in range(n):
    age, name = input().split()
    age = int(age)
    array.append(list((age, name)))

array.sort(key=lambda x: x[0])

for i in array:
    print(i[0], i[1])
"""
