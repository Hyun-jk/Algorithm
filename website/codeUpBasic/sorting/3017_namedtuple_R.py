# 정렬 기준
# namedtuple 사용
"""
collections 모듈의 nmaedtuple
-문자 그대로 이름이 있는 tuple 자료형이다. tuple 자료형에 이름을 붙여서 객체처럼 사용하는 방식
"""
import collections
# namedTuple의 구조를 선언, Student라는 이름의 속성은id,math,comp를 가진다.
# 이 때 속성은 항상 string 자료형으로 선언해야한다.
Student = collections.namedtuple('Student', ['id', 'math', 'comp'])
Students = list()

n = int(input())
for i in range(n):
    m, c = map(int, input().split())
    # 그냥 속성 값만 써줘도 되고, 속성명을 지정한 후에 지정해도 상관없다.
    Students.append(Student(i, m, c))

print(Students)


def chg_idx(j):
    temp = Students[j]
    Students[j] = Students[j+1]
    Students[j+1] = temp


for i in range(1, n):
    for j in range(n-i):
        if Students[j].math < Students[j+1].math:
            chg_idx(j)
        elif Students[j].math == Students[j+1].math:
            if Students[j].comp < Students[j+1].comp:
                chg_idx(j)

# tuple 자료형이기 때문에 인덱스를 지정하여 속성 호출가능
# 또한 객체이기도 하기 때문에 '객체명, 속성명'의 방식으로도 호출 가능
for i in range(n):
    print((Students[i].id)+1, Students[i].math, Students[i].comp)
