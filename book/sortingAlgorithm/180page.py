#성적이 낮은 순서로 학생 출력하기
n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    #input().split()을 통해서 받은 정보를 리스트로 반환하고
    #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장을 한다.
    array.append((input_data[0], int(input_data[1]))) 

#키(Key)를 이용하여, 점수를 기준으로 정렬 >>>???
#sorted 랑 lambda를 이용해서 정렬하는 법 다시 공부하자!!
array = sorted(array, key = lambda student :student[1])

    #정렬이 수행된 결과를 출력
for student in array:
     print(student[0], end=' ')