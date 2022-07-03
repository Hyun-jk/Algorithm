#ATM
"""
n = int(input())
times = list(map(int,input().split()))

times.sort()
total_time = []
sum = 0

for x in times:
    sum+= x
    total_time.append(sum) 

p = 0
for i in total_time:
    p+=i
print(p)
"""

n = int(input())
p = list(map(int,input().split()))

p.sort()

answer = 0
for i in range(1,n+1):
    answer += sum(p[:i])

print(answer)