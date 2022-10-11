#경사로
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def check_line(line):
    for i in range(1, n):
        #경사로가 1이상인 경우
        if abs(line[i] - line[i - 1]) > 1:
            return False
        #경사로의 차이가 1이고, 경사로가 낮아진 경우
        if line[i] < line[i - 1]:
            for j in range(l):
                #범위가 벗어나거나, 놓는 곳의 높이가 같지 않거나, 이미 발판이 놓여져있거나
                if i + j >= n or line[i] != line[i + j] or slope[i + j]:
                    return False
                #높이가 같은 경우에 발판을 놓는다
                if line[i] == line[i + j]:
                    slope[i + j] = True
        #경사로가 높아진 경우
        elif line[i] > line[i - 1]:
            for j in range(l):
                #???
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = True
    return True


for i in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    slope = [False] * n
    if check_line([graph[i][j] for i in range(n)]):
        ans += 1

print(ans)
