N, M = map(int, input().split())
S = []
K = []
for i in range(M):
    k, *s = map(int, input().split())
    K.append(k)
    S.append(s)
p = list(map(int, input().split()))

# スイッチ on/off の全てのパターン
on = [[False] * N for _ in range(1 << N)]
for bit in range(1 << N):
    for i in range(N):
        if bit & (1 << i):
            on[bit][i] = True

ans = 0
for bit in range(1 << N):
    ok = True
    for i in range(M):
        total = 0
        for j in range(K[i]):
            if on[bit][S[i][j] - 1]:
                total += 1
        if not total % 2 == p[i]:
            ok = False
            break
    if ok:
        ans += 1

print(ans)
