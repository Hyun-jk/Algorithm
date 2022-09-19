#카드 놓기
from itertools import permutations
n, k = int(input()), int(input())

#입력받은 숫자를 합쳐야 하기 때문에 String으로 받는다.
nums = [input() for _ in range(n)]
result = set()
for per in permutations(nums, k):
    result.add(''.join(per))
    
print(len(result))