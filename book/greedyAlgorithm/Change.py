#(기초)거스름돈 
coin_types = [500,100,50,10]
pay = 1260
count = 0

for coin in coin_types: 
    count += pay //coin 
    pay %= coin

print(count)
