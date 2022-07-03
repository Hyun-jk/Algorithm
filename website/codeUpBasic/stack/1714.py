#숫자 거꾸로 출력하기
"""
n = input()
answer = []
for i in range(len(n)):
    answer.append(int(n[i]))

for _ in range(len(n)):
    a = answer.pop()
    print(a,end='')
"""
#range --> 시작, 끝, 증가,감소 지정할 수 있다. 코드가 훨씬 간단한데 
# 나 처럼 하면 for문을 두 번 실행 시켜야 한다.
n = input()
for i in range(len(n)-1, -1, -1):
    print(n[i], end='')
    