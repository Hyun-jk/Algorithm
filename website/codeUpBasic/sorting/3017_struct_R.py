# 정렬 기준
# struct 사용
import struct

n = int(input())
stus = list()
# pack()함수를 사용해서 객체를 선언
# 첫 번째 인자값은 객체의 구조(형식)을 의미함
# 속성값의 자료형을 조합해서 문자열 형식으로 지정
for i in range(n):
    m, c = map(int, input().split())
    stus.append(struct.pack('iii', i+1, m, c))


def chg_idx(j):
    temp = stus[j]
    stus[j] = stus[j+1]
    stus[j+1] = temp


for i in range(1, n):
    for j in range(n-i):
        stuj = struct.unpack('iii', stus[j])
        stujj = struct.unpack('iii', stus[j+1])

        if stuj[1] < stujj[1]:
            chg_idx(j)
        elif stuj[1] == stujj[1]:
            if stuj[2] < stujj[2]:
                chg_idx(j)

# 객체의 속성값 호출하기 위해서 unpack()함수를 사용하여 호출해야한다.
# pack()과 마찬가지로 해당 객체의 구조를 지정한 수 호출할 객체명을 지정하면 된다.
# namedtuple과 마찬가지로 인덱스를 지정해서 특정 속성값을 호출할 수 있다.
for s in stus:
    res = struct.unpack('iii', s)
    print(res[0], res[1], res[2])
