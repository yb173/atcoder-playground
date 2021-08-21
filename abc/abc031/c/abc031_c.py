INF = 1 << 60

def sum_taka(x, y, A):
    if y < x:
        y, x = x, y
    return sum(A[i] for i in range(x, y + 1) if (i - x) % 2 == 0)

def sum_aoki(x, y, A):
    if y < x:
        y, x = x, y
    return sum(A[i] for i in range(x, y + 1) if (i - x) % 2 == 1)

N = int(input())
A = list(map(int, input().split()))

ans = []
for t in range(N):
    aoki_max = -INF
    taka = -INF
    for a in range(N):
        if a == t: continue
        aoki = sum_aoki(t, a, A)
        # 同じの複数あったら左を取るので，等号はつけない
        if aoki_max < aoki:
            aoki_max = aoki
            taka = sum_taka(t, a, A)
    ans.append(taka)

print(max(ans))
    