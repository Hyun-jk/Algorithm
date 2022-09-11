# 스택
import sys
input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        list.append(int(command[1]))
    elif command[0] == 'pop':
        if list:
            a = list.pop()
            print(a)
            continue
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(list))

    elif command[0] == 'empty':
        if list:
            print(0)
        else:
            print(1)

    elif command[0] == 'top':
        if list:
            print(list[-1])
        else:
            print(-1)
