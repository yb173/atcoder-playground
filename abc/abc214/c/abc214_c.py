INF = 1 << 60

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

F = [INF] * (2 * N)

for i in range(2 * N):
    F[i % N] = min(T[i % N], F[(i - 1) % N] + S[(i - 1) % N])

for i in range(N):
    print(F[i])
