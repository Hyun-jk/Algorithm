#STL stack

n = int(input())
commander = []

for i in range(n):
    commander.append(input())

stack = []
push = []
for i in commander:
    if 'push' in i :
        push.append(i.split(' ')) #왜 이중리스트로 들어가는지 이유를 모르겟다...?
        stack.append(int(push[0][1]))
        push.pop()
    elif 'top' in i:
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
    elif 'pop' in i:
        if not stack:
            continue
        else:
            stack.pop()
    elif 'size' in i:
        print(len(stack))
    elif 'empty' in i :
        if not stack:
            print('true')
        else:
            print('false')


