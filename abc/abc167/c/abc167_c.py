N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)

ans = 1 << 60
for bit in range(1 << N):
    cost = 0
    rikai = [0] * M
    for i in range(N):
        if not bit & (1 << i): continue
        cost += C[i]
        for j in range(M):
            rikai[j] += A[i][j]
    if sum(v < X for v in rikai): continue
    ans = min(ans, cost)

if ans == 1 << 60:
    print(-1)
    exit()

print(ans)            
