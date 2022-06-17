pasta = []
juice = []

pasta.append(int(input()))
pasta.append(int(input()))
pasta.append(int(input()))
juice.append(int(input()))
juice.append(int(input()))

pasta_min_price = min(pasta)
juice_min_price = min(juice)
sum_price = pasta_min_price + juice_min_price
print(sum_price + sum_price*0.1)
