# 전화번호 목록

t = int(input())  # 테스트 케이스의 개수


for _ in range(t):
    n = int(input())  # 전화번호 수
    array = [input() for _ in range(n)]

    # 문자열 정렬
    # ex) 문자열 32, 192,43242,3234, 19256을 정렬을 하면
    # 192,19256,32,3234,43242 사전순으로 정렬이된다.
    array.sort()
    check = 'Yes'

    for i in range(len(array) - 1):

        # 사전순으로 정렬이 되기때문에, 굳이 전체를 비교할 필요가 없고, 그 다음 인덱스만 비교를 하면된다.
        # 비교를 할 때는 문자열 slice를 통해서 i의 길이만큼만 비교를 해준다
        if array[i] == array[i+1][0:len(array[i])]:
            check = "no"

    if check == "no":
        print("NO")
    else:
        print("Yes")
