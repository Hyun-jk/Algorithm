#괄호
t = int(input())
answer = []


for i in range(t):
    a = input()
    count = 0
    flag = True
    
    for j in a:
        if j == '(':
            count +=1
        else:
            if count == 0:
                flag = False
                break
            count -= 1

    if count == 0 and flag == True:
        print('YES')
    else:
        print('NO')

