#삽입 정렬
"""
삽입정렬은 데이터를 하나씩 확인하여, 각 데이터를 적절한 위치에 삽입하는 정렬이다.
삽입정렬은 선택정렬보다 구현 난이도가 높은 편이지만
실행 시간 측면에서 더 효율적인 알고리즘이다.

삽입 정렬은 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬 되어 있을 때 효율적이다'
선택 정렬은 현재 데이터의 상태와 상관없이 무조건 모든 원소를 비교하고 위치를 바꾸는 반면
삽입정렬은 그렇지 않다

삽입정렬은 이동한 단계를 보면 항상 오름차순으로 정렬된 상태이다.
삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추면 된다.
"""

#간단한 삽입 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1) : #인덱스 i부터 1까지 감소하며 반복하는 문법(역순으로)
        if array[j] < array[j-1]: # 왼쪽으로 한 칸씩 이동
            array[j], array[j-1] = array[j-1] , array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

"""
삽입 정렬의 시간 복잡도)
삽입 정렬의 시간 복잡도는 O(N**2) 마찬가지로 반복문이 2번 중척되어 있다.

꼭 기억할 내용은)
삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다는 점이다.
최선의 경우 O(N)의 시간 복잡도를 가진다.

보통 삽입 정렬은 퀵 정렬보다 비효율적이나 정렬이 거의 되어 있는 상황에서는
퀵 정렬 알고리즘보다 효율적이다.
그래서 거의 정렬되어 있는 상태로 입력이 주어지는 문제라면 퀵 정렬등의
여타 정렬 알고리즘을 이용하는 것보다 삽입 정렬을 이용하는 것이 정답 확률을 높일 수 있다
"""
