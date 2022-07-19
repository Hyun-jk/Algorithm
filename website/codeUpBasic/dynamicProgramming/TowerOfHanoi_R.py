#하노이탑
#다른 하노이탑 같이 풀어보자
msg_format = "{}번 원반을 {}에서 {}로 이동"

def move(N,start,to):
    print(msg_format.format(N,start,to))

def hanoi(N,start,to,via):
    if N ==1:
        move(1,start,to)
    else:
        hanoi(N-1,start,via,to)
        move(N,start,to)
        hanoi(N-1,via,to,start)

hanoi(3,'A','C','B')