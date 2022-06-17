#1이 될 때 까지
#내가 한 알고리즘이 맞는지 모르겠다. 답은 나오는데 
n,k = map(int,input().split())
count = 0

while n != 1:
    if n%k ==0:
        n = n //k
        count += 1
    else:
        n-= 1
        count += 1
print(count)
