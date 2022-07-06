# 3등 찾기
n = int(input())
students = []
for _ in range(n):
    info = input().split()
    students.append([info[0], int(info[1])])

students.sort(key=lambda x: x[1], reverse=True)

print(students[2][0])
