N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(M):
    N -= A[i]

print(N if N >= 0 else -1)
