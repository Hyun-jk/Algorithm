#AC
#n의 최대 크기가 100,000이기 때문에 매번 reverse를 사용하면 
#시간초과가 발생한다. 그래서 reverse 와 flag를 이용하여 reverse를 최소화 시켰다.
from collections import deque

t = int(input())

for _ in range(t) :
    p = input()
    n = int(input())
    data = input()[1:-1].split(',') #list보다 빠른 deque사용, popleft()를 사용하기 위해서
    q = deque(data)
    

    if n == 0 :
        q = []

    reverse = 0
    flag = 0
    for value in p :
        if value == 'R' :
            reverse += 1
        elif value == 'D' :
            if q :
                if reverse % 2 == 0 : # 그대로
                    q.popleft()
                else : # 거꾸로
                    q.pop()
            else :
                flag = 1
                print('error')
                break

    if flag == 0 :
        if reverse % 2 == 0 : # 그대로
            print('[' + ','.join(q) + ']')
        else : # 거꾸로
            q.reverse()
            print('[' + ','.join(q) + ']')