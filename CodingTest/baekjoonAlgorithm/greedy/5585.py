#거스름돈
n = 1000- int(input())
money_types = [500,100,50,10,5,1]
count = 0
for i in money_types:
    count += n // i
    n = n % i
    if n ==0:
        print(count)
        break

    