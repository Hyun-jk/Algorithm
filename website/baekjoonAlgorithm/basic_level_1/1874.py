#스택 수열
n = int(input())
s = []
op = []
temp = True
count = 1
for i in range(n):
    num = int(input())

    while count <= num:
        s.append(count)
        count +=1 
        op.append('+')

    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)

