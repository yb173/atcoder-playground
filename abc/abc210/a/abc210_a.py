N, A, X, Y = map(int, input().split())
if N <= A:
    print(N * X)
else:
    print(A * X + Y * (N - A))
