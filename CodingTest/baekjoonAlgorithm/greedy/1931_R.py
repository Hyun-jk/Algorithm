#회의실 배정
n = int(input())
room = []

for _ in range(n):
    room.append(list(map(int,input().split())))

print(f'정렬 전 {room}')
#회의가 끝나는 시간, 회의가 시작하는 시간 정렬
room.sort(key = lambda x:(x[1],x[0]))

print(f'정렬 후 time {room}')


cnt = 1
end = room[0][1]
for i in range(1,n):
    if room[i][0] >= end:
        cnt +=1
        end = room[i][1]
    
print(cnt)


"""
1.sort
->원본을 변형시켜 정렬한다.

2.sorted
->정렬된 결과를 반환, 원형을 변형시키지 않는다.

3.key
->정렬을 목적으로 하는 함수를 값으로 넣는다
-> lambda를 이용가능
"""