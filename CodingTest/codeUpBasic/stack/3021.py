#큰 수 덧셈
a = int(input())
b = int(input())

print(a+b)

"""
다른 언어 같은 경우에는 큰 수에 대해서 숫자를 문자열로 받아와 뒤집어서 처음부터
마지막까지 모조리 한 자리씩 더한 다음에, 10이 넘는 자리마다 자리올림을 수행해줘야한다.
그러나 python은 BIgInteger에 대한 개념이 내장되어 있다.
"""