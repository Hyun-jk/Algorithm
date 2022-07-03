#최소대금
pasta = []
juice = []

for _ in range(3):
    pasta.append(int(input()))

for _ in range(2):
    juice.append(int(input()))

pasta_min_price = min(pasta)
juice_min_price = min(juice)
sum_price = pasta_min_price + juice_min_price
print(sum_price + sum_price*0.1)
