#주유소

N = int(input())

roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

#처음 도시에서 무조건 주유를 해야함으로 기준으로 잡고
min_price = roads[0] * costs[0]
#그 다음 도시랑 가격 비교를 하여 가격이 적으면 그 도시의 가격을 최소 비용으로 잡고 비용에 더한다.
min_cost = costs[0]

for i in range(1,N-1):
    if min_cost > costs[i]:
        min_cost = costs[i]
    
    min_price += min_cost * roads[i]
    print(f'i = {i} min_cost = {min_cost} min_price = {min_price}')

print(min_price)
