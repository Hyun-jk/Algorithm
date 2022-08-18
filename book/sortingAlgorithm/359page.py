# 국영수
n = int(input())
students = []  # 학생 정보를 담은 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

"""
[정렬기준]
1)두 번째 원소(국어점수)를 기준으로 내림차순 정렬
2)두 번째 원소가 같은 경우, 세 번째 원소(영어점수)를 기준으로 오름차순 정렬
3)세 번째 원소가 같은 경우, 네 번째 원소(수학점수)를 기준으로 내림차순 정렬
4)네 번째 원소가 같은 경우, 첫 번째 원소(이름의 사전 순)를 기준으로 오름차순 정렬
"""
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for studnet in students:
    print(studnet[0])
