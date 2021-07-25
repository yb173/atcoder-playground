N = int(input())
A = [(int(input()), _) for _ in range(N)]
A = sorted(A, key=lambda x: x[0])

d = {}
for i in range(N):
    if not i == N - 1:
        d[A[i][1]] = A[N - 1][0]
    else:
        d[A[i][1]] = A[N - 2][0]

for i in range(N):
    print(d[i])
