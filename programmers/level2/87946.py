# 완저탐색_피로도
def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if visited[i] != True and dungeons[i][0] <= k:
            visited[i] = True
            dfs(k-dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer


answer = 0
k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
