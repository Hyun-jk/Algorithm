#보물
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# S = A[0]XB[0] +..... + A[N-1] X B[N-1]


A.sort()
B.sort(reverse=True)
sum = 0

for i in range(N):
    sum += A[i] * B[i]

print(sum)


