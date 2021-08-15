INF = 1 << 60

N = int(input())

F = [list(map(int, input().split())) for i in range(N)]
P = [list(map(int, input().split())) for i in range(N)]

ans = -INF
for bit in range(1 << 10):
    profit = 0
    j = [None] * 10
    for i in range(10):
        j[i] = 1 if bit & (1 << i) else 0
    if sum(j) == 0: continue

    profit = 0
    for shop in range(N):
        profit += P[shop][sum(j[i] * F[shop][i] for i in range(10))]
    ans = max(ans ,profit)

print(ans)
