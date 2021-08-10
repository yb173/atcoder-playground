def compress(X):
    d = {}
    Y = sorted(list(set(X)))
    for i in range(len(Y)):
        d[Y[i]] = i + 1
    return [d[X[i]] for i in range(len(X))]

H, W, N = map(int, input().split())
A, B = [None] * N , [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

A = compress(A)
B = compress(B)

for i in range(N):
    print('{} {}'.format(A[i], B[i]))
