#전자레인지
T = int(input())
button = [300,60,10]
count = []

for i in button:
    if T >= i:
        count.append(T//i)
        T = T % i
    elif T < i:
        count.append(0)

if T !=0:
    print(-1)    
else:
    for j in count:
        print(j, end=' ')

