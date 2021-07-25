import itertools

N, M, Q = map(int, input().split())

a, b, c, d = [], [], [], []
for i in range(Q):
    _a, _b, _c, _d = map(int, input().split())
    _a -= 1
    _b -= 1
    a.append(_a)
    b.append(_b)
    c.append(_c)
    d.append(_d)

l = [v for v in range(1, M + 1)]
ans = 0
for A in itertools.combinations_with_replacement(l, N):
    now = 0
    for i in range(Q):
        if A[b[i]] - A[a[i]] == c[i]:
            now += d[i]
    ans = max(ans, now)

print(ans)
