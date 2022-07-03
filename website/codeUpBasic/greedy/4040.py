#n = 여름 성수기 총기간 / m = 펜션이 보유하고 있는 방의 갯수
n, m = map(int,input().split())

#방 번호랑 날짜를 쉽게 하기 위해서 booking[0]을 넣어준다
booking = [['X']* m]

for i in range(n):
    booking.append(list(input()))

#s = 고객이 펜션에 도착하는 날 / t = 펜션을 떠나는 날
s,t = map(int,input().split())
print(f'n는{n} m:{m} s:{s} t:{t}')

def check(n):
    maxday = 0

#그리드는 최대의 수 혹은 최소 값을 구하는 알고리즘인데
#이 문제에서 한 방에 최대한 예약이 가능한 방을 찾는게 중요한데 밑에 코드가 이해가 안간다....
    for i in range(m):
        day = 0
        for j in range(s,t):
            if booking[j][i] == 'O':
                day += 1
            else:
                break
        if maxday < day:
            maxday = day
    return maxday

count = -1
today = s

while today < t:
    stay =check(today)
    if stay ==0:
        count = -1
        break

    count += 1
    today += stay

print(count)






    


