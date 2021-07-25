def calc_ans(A):
    global ans
    now = 0
    for i in range(Q):
        if A[b[i]] - A[a[i]] == c[i]:
            now += d[i]
    ans = max(ans, now)

def dfs(A):
    if len(A) == N:
        calc_ans(A)
        return
    A.append(A[-1] if A else 1)
    while A[-1] <= M:
        dfs(A[:])
        A[-1] += 1

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

ans = 0
A = []
dfs(A)
print(ans)
