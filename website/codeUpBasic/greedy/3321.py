#최고의 피자
n = int(input())
dough_price, topping_price = map(int,input().split())
dough_calories = int(input())
topping_calories = []

for x in range(n):
    topping_calories.append(int(input()))

#토핑 칼로리 내림차순
topping_calories.sort(reverse=True)
#기본 가격(처음 가격)
price = dough_price
#처음 칼로리
total_calories = dough_calories
#처음 1달러당 칼로리
rate = total_calories/price

for calories in topping_calories:
    add_topping_rate = (total_calories + calories ) / (price+topping_price) 
    if rate < add_topping_rate:
        total_calories += calories
        price += topping_price
        rate = add_topping_rate
    else:
        break
print(int(rate))



