N = int(input())
A = list(map(int, input().split()))

B = [None] * N
for i in range(N):
    B[i] = (A[i], i)
B.sort(key=lambda x: x[0])

left_median = B[N // 2 - 1][0]
right_median = B[N // 2][0]

C = [None] * N
for i in range(N):
    median = right_median if i <= N // 2 - 1 else left_median
    C[i] = (median, B[i][1])
C.sort(key=lambda x: x[1])

for i in range(N):
    print(C[i][0])
