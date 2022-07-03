#천단위 구분기호
"""
python format함수를 이용해서 풀었다
근데 스택을 개념을 이용해서 다시 풀어보자.

a = input()
b = int(input())
print(format(b,","))
"""
n = int(input())
number_list = list(input())
number_list.reverse()
sort_number_list = []

for i in range(n):
    sort_number_list.append(number_list[i])
    if (i+1)%3 == 0 and i != n-1:
        sort_number_list.append(",")

sort_number_list.reverse()

print("".join(sort_number_list))