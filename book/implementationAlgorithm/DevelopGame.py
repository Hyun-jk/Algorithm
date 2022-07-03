# 게임 개발

n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    print(f'direction = {direction}')
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        print(f'x는{x} y는{y} count는 {count} turn_time 는{turn_time}')
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        print(f'네 방향을 다 돌았을 경우')
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            print('뒤로 한 칸 이동이 가능한 경우')
            x = nx
            y = ny
            print(f'x 는{x} y는 {y}')
        else:
            break
        turn_time  = 0
print(count)
