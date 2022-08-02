# 공유기 설치
n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        # 앞 집부터 공유기 설치>>>????
        for i in range(1, len(array)):
            if array[i] >= current + mid:
                count += 1
                current = array[i]

        # 설치할 수 있는 공유기 개수가 c를 넘어가면 더 넓게 설치가 가능하다
        if count >= c:
            global answer
            start = mid + 1  # 설치거리를 mid + 1로 설정하여 다시 앞집부터 설치
            answer = mid
        else:  # c개를 넘어가지 않는다면 더 좁게 설치해야 함으로 mid -1로 설정
            end = mid - 1


start = 1
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)
