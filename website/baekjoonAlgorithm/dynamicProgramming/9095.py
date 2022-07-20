#1,2,3 더하기
n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

d=[0] * (max(array)+1)
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, max(array)+1):
    d[i] = d[i-1] + d[i-2] +d[i-3]
    print(d)

for i in array:
    print(d[i]) 