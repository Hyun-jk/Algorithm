# 2022 kakao
# 신고 결과받기

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)

    # report를 for으로 돌리면서 user dictionary에 신고자,신고당한사람을 넣는다
    # cnt dict에 신고당한 횟수를 집어넣는다
    for i in report:
        x, y = i.split()
        user[x].add(y)
        cnt[y] += 1

    for j in id_list:
        result = 0
        for l in user[j]:
            if cnt[l] >= k:
                result += 1
        answer.append(result)

    return answer
