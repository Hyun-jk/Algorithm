# 로봇 청소기
n, m = map(int, input().split())  # N,M을 입력 받음
d = [[0] * m for _ in range(n)]  # 청소 여부를 List로 생성
x, y, direction = map(int, input().split())  # x,y,direction를 입력받음
d[x][y] = 1  # 현재 위치 청소(0->1)

array = []  # 빈칸, 벽을 입력 받음
for i in range(n):
    array.append(list(map(int, input().split())))  # 입력은 list형태로 array에 append

# 북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction  # global 함수 선언
    direction -= 1
    # 0:북, 1:동, 2:남, 3:서
    if direction == -1:
        direction = 3


count = 1  # 현재 위치는 청소를 했음으로 1
turn_time = 0  # 왼쪽 방향으로 회전하는 횟수 계산, 4번인 경우 다른 조건 실행
while True:
    turn_left()  # 왼쪽으로 방향전환
    # 왼쪽편의 청소여부 및 벽인지 확인을 위한 방향이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 왼쪽편이 청소를 해야하는 곳인데 방문을 하지 않은 경우
        d[nx][ny] = 1  # 청소
        x, y = nx, ny  # 위치로 이동
        count += 1  # 청소를 했음으로 1증가
        turn_time = 0  # 왼쪽 방향 회전 횟수 0으로 초기화
        continue
    else:
        turn_time += 1

    if turn_time == 4:  # 총 4번 회전한 경우 즉 청소가 되어 있거나, 벽이 있는 경우
        nx = x-dx[direction]  # 바라보는 방향에서 뒤로 이동
        ny = y-dy[direction]

        if array[nx][ny] == 0:  # 이동한 위치가 벽이 아니라면,
            x = nx
            y = ny
        else:  # 이동한 위치가 벽이면
            break
        turn_time = 0  # 이동한 위치가 벽이 아닌경우 그 위치로 이동후 다시 4방향 확인을 해야함으로

print(count)
