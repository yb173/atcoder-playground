N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
left_median = B[N // 2 - 1]
right_median = B[N // 2]

for i in range(N):
    if A[i] < right_median:
        print(right_median)
    else:
        print(left_median)
