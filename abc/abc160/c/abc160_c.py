K, N = map(int, input().split())
A = list(map(int, input().split()))

diff = 0
for i in range(N):
    if i == N - 1:
        diff = max(diff, K + A[0] - A[i])
    else:
        diff = max(diff, A[i + 1] - A[i])

print(K - diff)
