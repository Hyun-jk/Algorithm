#동전0

n,k = map(int,input().split())
money_types = []

for i in range(n):
    money_types.append(int(input()))

money_types.sort(reverse=True)
count = 0

for x in money_types:
    if x <= k:
        count += k // x
        k %= x
    if k ==0:
        print(count)
        break


"""
시간초과)

n,k = map(int,input().split())
money_types = []

for i in range(n):
    money_types.append(int(input()))

money_types.sort(reverse=True)
count = 0

for x in money_types:
    while x <= k:
        count+=1
        k-=x
    if k ==0:
        print(count)
        break    
"""