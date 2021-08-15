from itertools import product

INF = 1 << 60

N = int(input())
F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -INF
for v in product([0, 1], repeat=10):
    if sum(v) == 0: continue
    profit = 0
    for shop in range(N):
        profit += P[shop][sum(v[i] * F[shop][i] for i in range(10))]
    ans = max(ans, profit)

print(ans)
