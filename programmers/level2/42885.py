# 구명보트(그리디)
# 주의 한번에 2명밖에 타지 못한다.

def solution(people, limit):
    people.sort()
    cnt = 0
    start, end = 0, len(people)-1

    while start <= end:
        cnt += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1

    return cnt


people = [70, 50, 80, 50]
limit = 100
