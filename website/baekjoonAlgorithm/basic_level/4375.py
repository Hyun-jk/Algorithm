def solution(n):
    answer = 1
    while answer % n != 0:
        answer = (answer * 10) + 1
    answer = len(str(answer))
    return answer

while True :
  try :
    n = int(input())
    print(solution(n))
  except :
    break