# 두 배열의 원소 교체
N, K = map(int, input().split())  # N,K를 입력받기
A = list(map(int, input().split()))  # 배열 A의 모든 원소를 입력받기
B = list(map(int, input().split()))  # 배열 B의 모든 원소를 입력 받기

A.sort()  # 배열 A는 오름차순 정렬 수행
B.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

for i in range(K):
    if A[i] < B[i]:  # A의 원소가 B의 원소보다 작은 경우
        # 두 원소를 교체(스와프)
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
