#퀵 정렬 >> 다시 공부하자!!
"""
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다
즉
퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 
리스트르 반으로 나누는 방식으로 동작한다

퀵 정렬에서는 피벗(Pivot)이 사용된다.
피벗 = 큰 숫자와 작은 숫자를 교환할 때 교환하기 위한 '기준'

퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야 한다.

피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러 가지 방식으로 퀵 정렬을 구분할 수 가 있다.
대표적인 분할 방식인 호어 분할(Hoare Partition)

방법)
1.리스트에서 첫 번째 데이터를 피벗으로 정한다
2. 왼쪽에서부터는 피벗보다 큰 데이터를 찾고
3. 오른쪽에서부터 피벗보다 작은 데이터를 찾는다
4.그 다음 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.
5.이러한 과정을 반복하면 '피벗'에 대하여 정렬이 수행된다.
"""

#퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start +1 #피벗 그 다음 수부터,
    right = end

    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left +=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right],array[pivot] = array[pivot],array[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right],array[left]
    
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

#파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] #피벗은 첫 번째 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

"""
퀵정렬의 시간 복잡도
퀵 정렬의 평균 시간 복잡도는 O(NlogN)이다
데이터가 무작위로 입력되는 경우 퀵 정렬은 빠르게 동작할 확률이 높다.
"""
