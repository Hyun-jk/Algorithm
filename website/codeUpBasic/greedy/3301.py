#거스름돈
money = int(input())
change_types= [50000,10000,5000,1000,500,100,50,10,]
count = 0

for change in change_types:
    #몫
    count += money //change
   #나머지
    money %= change 
print(count)