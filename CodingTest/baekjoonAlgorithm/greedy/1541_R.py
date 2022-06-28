#잃어버린 괄호
a = input().split('-')
num = []

for i in a:
    cnt = 0
    s = i.split('+')
    print(f's = {s}')
    for j in s:
        cnt += int(j)
        print(f'cnt = {cnt}')
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)