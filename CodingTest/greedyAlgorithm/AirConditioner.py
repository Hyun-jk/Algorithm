"""
current_temperature,set_temperature= map(int,input().split())
differences = abs(set_temperature - current_temperature)
controller1 = [10,5,1]
count = 0
if differences > 0:
    for degree in controller1:
        print(f'온도차이는 {differences}')
        print(f'컨트롤러는 {degree}')
        while differences >= degree:
            differences -= degree
            count +=1
            print(count)
        if differences == 0:
            break 
print(count)

놓친 부분
예를 들어 8,9는 +1을 2번해서 10을 낮추는게 
-5를 한 번, -1 을 3번 하는 것보다 카운트를 적게 쓴다
이 점을 유의해서 다시 코드를 짜보자
"""
current_temperature,set_temperature= map(int,input().split())
difference = abs(set_temperature - current_temperature)
count = 0

#온도 조절이 끝난 후에 while문을 빠져나온다.
while difference != 0:
    if difference >= 10:
        difference -= 10
        count += 1
    #차이가 8,9 일 경우에는 +1을 해서 10을 맞추고 -10을 하는게 카운트가 적다.
    elif difference > 7:
        difference += 1
        count +=1
    elif difference > 4:
        difference-= 5
        count += 1
    elif difference >2:
        difference += 1
        count += 1
    else:
        difference -= 1
        count += 1
print(count)    

    












    




