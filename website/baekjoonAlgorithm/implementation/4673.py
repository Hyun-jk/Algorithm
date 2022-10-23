# 셀프 넘버
n = 10000
answer = set(range(1, 10001))
remove_set = set()

for i in range(1, n+1):
    a = i
    for j in str(i):
        a += int(j)
    remove_set.add(a)

for k in sorted(answer - remove_set):
    print(k)
