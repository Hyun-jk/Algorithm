#0은 빼!

n = int(input())
answer = []

for _ in range(n):
    num = int(input())
    if num != 0:
        answer.append(num)
    else:
        answer.pop()
    
sum = 0
for i in answer:
    sum += i
print(sum)
