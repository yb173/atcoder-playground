INF = 1 << 60

N = int(input())

F = []
for i in range(N):
    f = list(map(int, input().split()))
    F.append(f)

P = []
for i in range(N):
    p = list(map(int, input().split()))
    P.append(p)

ans = -INF
for bit in range(1 << 10):
    profit = 0
    c = [0] * N
    ok = False
    for i in range(10):
        if not bit & (1 << i): continue
        ok = True
        for n in range(N):
            c[n] += F[n][i]
    # joisino お姉ちゃんが 1 つも店を開けていない場合はスキップ
    if not ok: continue
    t = 0
    for n in range(N):
        t += P[n][c[n]]
    ans = max(ans ,t)

print(ans)
